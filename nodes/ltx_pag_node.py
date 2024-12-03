
import math

from einops import rearrange
import torch
import torch.nn.functional as F

from comfy.ldm.modules.attention import optimized_attention
import comfy.model_patcher
import comfy.samplers


DEFAULT_PAG_LTX = { 'layers': set([14]) }


class LTXPerturbedAttentionNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "scale": ("FLOAT", {"default": 3.0, "min": 0.0, "max": 100.0, "step": 0.01, "round": 0.01}),
                "rescale": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 100.0, "step": 0.01, "round": 0.01}),
                "cfg": ("FLOAT", {"default": 3.0, "min": 0.0, "max": 100.0, "step": 0.01, "round": 0.01}),
            },
            "optional": {
                "attn_override": ("ATTN_OVERRIDE",)
            }
        }

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "patch"

    CATEGORY = "ltxtricks/attn"

    def patch(self, model, scale, rescale, cfg, attn_override=DEFAULT_PAG_LTX):
        m = model.clone()

        def pag_fn(q, k,v, heads, attn_precision=None, transformer_options=None):
            return v

        def post_cfg_function(args):
            model = args["model"]

            cond_pred = args["cond_denoised"]
            uncond_pred = args["uncond_denoised"]

            len_conds = 1 if args.get('uncond', None) is None else 2 
            
            cond = args["cond"]
            sigma = args["sigma"]
            model_options = args["model_options"].copy()
            x = args["input"]

            if scale == 0:
                if len_conds == 1:
                    return cond_pred
                return uncond_pred + (cond_pred - uncond_pred)
            
            for block_idx in attn_override['layers']:
                model_options = comfy.model_patcher.set_model_options_patch_replace(model_options, pag_fn, f"layer", "self_attn", int(block_idx))

            (perturbed,) = comfy.samplers.calc_cond_batch(model, [cond], x, sigma, model_options)

            # if len_conds == 1:
            #     output = cond_pred + scale * (cond_pred - pag)
            # else:
            #     output = cond_pred + (scale-1.0) * (cond_pred - uncond_pred) + scale * (cond_pred - pag)


            output = uncond_pred + cfg * (cond_pred - uncond_pred) \
                + scale * (cond_pred - perturbed)
            if rescale > 0:
                factor = cond_pred.std() / output.std()
                factor = rescale * factor + (1 - rescale)
                output = output * factor

            return output


        m.set_model_sampler_post_cfg_function(post_cfg_function)

        return (m,)

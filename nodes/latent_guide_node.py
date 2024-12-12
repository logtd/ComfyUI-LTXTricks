import torch


from ..utils.latent_guide import LatentGuide


class AddLatentGuideNode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"model": ("MODEL",),
                             "latent": ("LATENT",),
                             "image_latent": ("LATENT",),
                             "index": ("INT", {"default": 0, "min": -1, "max": 9999, "step": 1}),
                             "insert": ("BOOLEAN", { "default": False }),
                }}

    RETURN_TYPES = ("MODEL", "LATENT")

    CATEGORY = "ltxtricks"
    FUNCTION = "generate"

    def generate(self, model, latent, image_latent, index, insert):
        image_latent = image_latent['samples']
        latent = latent['samples'].clone()
        
        # Convert negative index to positive
        if insert:
            # Handle insertion
            if index == 0:
                # Insert at beginning
                latent = torch.cat([image_latent[:,:,0:1], latent], dim=2)
            elif index >= latent.shape[2] or index < 0:
                # Append to end
                latent = torch.cat([latent, image_latent[:,:,0:1]], dim=2)
            else:
                # Insert in middle
                latent = torch.cat([
                    latent[:,:,:index],
                    image_latent[:,:,0:1],
                    latent[:,:,index:]
                ], dim=2)
        else:
            # Original replacement behavior
            latent[:,:,index] = image_latent[:,:,0]
        
        model = model.clone()
        guiding_latent = LatentGuide(image_latent, index)
        model.set_model_patch(guiding_latent, 'guiding_latents')
        
        return (model, {"samples": latent}, )
    


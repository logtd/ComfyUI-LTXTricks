from .nodes.modify_ltx_model_node import ModifyLTXModelNode
from .nodes.latent_guide_node import AddLatentGuideNode
from .nodes.ltx_inverse_model_pred_nodes import LTXForwardModelSamplingPredNode, LTXReverseModelSamplingPredNode
from .nodes.rectified_sampler_nodes import LTXRFForwardODESamplerNode, LTXRFReverseODESamplerNode

NODE_CLASS_MAPPINGS = {
    'ModifyLTXModel': ModifyLTXModelNode,
    'AddLatentGuide': AddLatentGuideNode,
    'LTXForwardModelSamplingPred': LTXForwardModelSamplingPredNode,
    'LTXReverseModelSamplingPred': LTXReverseModelSamplingPredNode,
    'LTXRFForwardODESampler': LTXRFForwardODESamplerNode,
    'LTXRFReverseODESampler': LTXRFReverseODESamplerNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    'ModifyLTXModel': 'Modify LTX Model',
    'AddLatentGuide': 'Add LTX Latent Guide',
    'LTXForwardModelSamplingPred': 'LTX Forward Model Pred',
    'LTXReverseModelSamplingPred': 'LTX Reverse Model Pred',
    'LTXRFForwardODESampler': 'LTX Rf-Inv Forward Sampler',
    'LTXRFReverseODESampler': 'LTX Rf-Inv Reverse Sampler'
}

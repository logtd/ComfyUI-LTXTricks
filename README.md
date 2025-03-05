# ⚠️ DEPRECATED ⚠️

**This repository is no longer maintained. All nodes and functionality have been moved to the official [LTX-Video repository](https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/tricks).**

**Please use the official repository for all future development and updates: https://github.com/Lightricks/ComfyUI-LTXVideo**

---
# ComfyUI-LTXTricks

A set of nodes that provide additional controls for the LTX Video model

## Installation

There are no additional packages required. The [ComfyUI examples page](https://comfyanonymous.github.io/ComfyUI_examples/ltxv/) can get you started if you haven't already used LTX.

## Examples

Example workflows can be found in the `example_workflows` directory.

## RF-Inversion
This is an implementation of [RF-Inversion](https://rf-inversion.github.io/) and an [example workflow can be found here](https://github.com/logtd/ComfyUI-LTXTricks/blob/main/example_workflows/example_ltx_inversion.json).

https://github.com/user-attachments/assets/64a0b25d-1a4d-4bfe-b68a-767cdb5d68e8

## RF-Edit
This is an implementation of [RF-Solver-Edit](https://github.com/wangjiangshan0725/RF-Solver-Edit) and an [example workflow can be found here](https://github.com/logtd/ComfyUI-LTXTricks/blob/main/example_workflows/example_ltx_rf_edit.json).

https://github.com/user-attachments/assets/7a5a62d0-b7cb-4298-bed0-d15ca9477cc3

## FlowEdit
This is an implementation of [FlowEdit](https://github.com/fallenshock/FlowEdit) and an [example workflow can be found here](https://github.com/logtd/ComfyUI-LTXTricks/blob/main/example_workflows/example_ltx_flow_edit.json).




## Image and Video to Video (I+V2V)
This is a method to perform Video to Video while using a reference image.

Use [this example workflow](https://github.com/logtd/ComfyUI-LTXTricks/blob/main/example_workflows/example_ltx_iv2v.json) for getting started. Results may vary.


https://github.com/user-attachments/assets/5a8eeaaa-d3cf-44b4-9ab6-d436c86dfcc7

## Enhance
A portion of [Spatiotemporal Skip Guidance
for Enhanced Video Diffusion Sampling](https://junhahyung.github.io/STGuidance/) (STG) has been implemented. Planning to add the "Restart" feature when time allows.

Use [this example workflow](https://github.com/logtd/ComfyUI-LTXTricks/blob/main/example_workflows/example_ltxv_stg.json) to see how it works.

Left is without STG, and right is with STG.

https://github.com/user-attachments/assets/67454258-fe57-4e3f-9133-af16981b9893




## Interpolation and Frame Setting

Deprecated, since this functionality has been integrated into core ComfyUI. Please use `LTXVKeyFrameConditioning` and `LTXVSequenceConditioning` nodes instead.




## Acknowledgements
RF-Inversion
```
@article{rout2024rfinversion,
  title={Semantic Image Inversion and Editing using Rectified Stochastic Differential Equations},
  author={Litu Rout and Yujia Chen and Nataniel Ruiz and Constantine Caramanis and Sanjay Shakkottai and Wen-Sheng Chu},
  journal={arXiv preprint arXiv:2410.10792},
  year={2024}
}
```
RF-Solver-Edit
```
@article{wang2024taming,
  title={Taming Rectified Flow for Inversion and Editing},
  author={Wang, Jiangshan and Pu, Junfu and Qi, Zhongang and Guo, Jiayi and Ma, Yue and Huang, Nisha and Chen, Yuxin and Li, Xiu and Shan, Ying},
  journal={arXiv preprint arXiv:2411.04746},
  year={2024}
}
```

FlowEdit
```
@article{kulikov2024flowedit,
	title = {FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models},
	author = {Kulikov, Vladimir and Kleiner, Matan and Huberman-Spiegelglas, Inbar and Michaeli, Tomer},
	journal = {arXiv preprint arXiv:2412.08629},
	year = {2024}
	}
```

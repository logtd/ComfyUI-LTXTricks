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


## Image and Video to Video (I+V2V)
This is a method to perform Video to Video while using a reference image.

Use [this example workflow](https://github.com/logtd/ComfyUI-LTXTricks/blob/main/example_workflows/example_ltx_iv2v.json) for getting started. Results may vary.


https://github.com/user-attachments/assets/5a8eeaaa-d3cf-44b4-9ab6-d436c86dfcc7


## Interpolation and Frame Setting
A set of nodes have been included to set specific latents to frames instead of just the first latent. An [example workflow can be found here](https://github.com/logtd/ComfyUI-LTXTricks/blob/main/example_workflows/example_ltx_interpolation.json).

https://github.com/user-attachments/assets/95d7e57b-064e-44e8-befe-3dcdb248ef8d


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

import torch


class LatentGuide(torch.nn.Module):
    def __init__(self, latent: torch.Tensor, index) -> None:
        super().__init__()
        self.index = index
        self.register_buffer('latent', latent)


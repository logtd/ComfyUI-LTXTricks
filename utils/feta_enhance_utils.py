import torch
from einops import rearrange


def _feta_score(query_image, key_image, head_dim, num_frames, enhance_weight):
    scale = head_dim**-0.5
    query_image = query_image * scale
    attn_temp = query_image @ key_image.transpose(-2, -1)  # translate attn to float32
    attn_temp = attn_temp.to(torch.float32)
    attn_temp = attn_temp.softmax(dim=-1)

    # Reshape to [batch_size * num_tokens, num_frames, num_frames]
    attn_temp = attn_temp.reshape(-1, num_frames, num_frames)

    # Create a mask for diagonal elements
    diag_mask = torch.eye(num_frames, device=attn_temp.device).bool()
    diag_mask = diag_mask.unsqueeze(0).expand(attn_temp.shape[0], -1, -1)

    # Zero out diagonal elements
    attn_wo_diag = attn_temp.masked_fill(diag_mask, 0)

    # Calculate mean for each token's attention matrix
    # Number of off-diagonal elements per matrix is n*n - n
    num_off_diag = num_frames * num_frames - num_frames
    mean_scores = attn_wo_diag.sum(dim=(1, 2)) / num_off_diag

    enhance_scores = mean_scores.mean() * (num_frames + enhance_weight)
    enhance_scores = enhance_scores.clamp(min=1)
    return enhance_scores



def get_feta_scores(img_q, img_k, num_heads, transformer_options):
    num_frames = transformer_options['original_shape'][2]
    _, ST, dim = img_q.shape
    head_dim = dim // num_heads
    spatial_dim = ST // num_frames

    query_image = rearrange(
        img_q, "B (T S) (N C) -> (B S) N T C", T=num_frames, S=spatial_dim, N=num_heads, C=head_dim
    )
    key_image = rearrange(img_k, "B (T S) (N C) -> (B S) N T C", T=num_frames, S=spatial_dim, N=num_heads, C=head_dim)
    weight = transformer_options.get('feta_weight', 0)
    return _feta_score(query_image, key_image, head_dim, num_frames, weight)
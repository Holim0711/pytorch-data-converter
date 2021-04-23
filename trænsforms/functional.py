import torch
import numpy as np
from PIL import Image
import cv2

__all__ = [
    'square_resize',
    'gaussian_blur',
]


def square_resize(img, size, interpolation=Image.BILINEAR, background_color=0):
    x, y = img.size

    if x > y:
        x, y = size, size * y // x
    else:
        x, y = size * x // y, size

    img = img.resize((x, y), interpolation)

    new = Image.new('RGB', (size, size), background_color)

    new.paste(img, ((size - x) // 2, (size - y) // 2))

    return new


def gaussian_blur(img, kernel_size, σ=(0.1, 2.0)):
    img = np.array(img)
    σ = σ[0] + (σ[1] - σ[0]) * torch.rand(1).item()
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), σ)

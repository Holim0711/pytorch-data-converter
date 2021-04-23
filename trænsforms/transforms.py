from PIL import Image
from .functional import *

__all__ = [
    'SquareResize',
    'GaussianBlur',
]


class SquareResize():
    def __init__(self, size, interpolation=Image.BILINEAR, background_color=0):
        self.size = int(size)
        self.interpolation = interpolation
        self.bg_color = background_color

    def __call__(self, img):
        return square_resize(img, self.size, self.interpolation, self.bg_color)


class GaussianBlur():
    def __init__(self, kernel_size, σ=(0.1, 2.0)):
        self.kernel_size = kernel_size
        self.σ = σ

    def __call__(self, img):
        return gaussian_blur(img, self.kernel_size, self.σ)

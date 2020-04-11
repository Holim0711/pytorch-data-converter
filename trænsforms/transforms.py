from PIL import Image
from .functional import *

__all__ = [
    'SquareResize',
]


class SquareResize():

    def __init__(self, size, interpolation=Image.BILINEAR, background_color=0):
        self.size = int(size)
        self.interpolation = interpolation
        self.bg_color = background_color

    def __call__(self, img):
        return square_resize(img, self.size, self.interpolation, self.bg_color)

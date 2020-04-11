from skimage.color import gray2rgb
from skimage.color import rgba2rgb
from skimage import img_as_ubyte
import warnings


def any2rgb(image):
    try:
        h, w, c = image.shape
    except ValueError:
        if len(image.shape) == 2:
            return gray2rgb(image)
        if len(image.shape) == 4:
            return toRGB(image[0])
        raise

    if c == 3:
        return image

    image = rgba2rgb(image)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        image = img_as_ubyte(image)

    return image


def invert(image):
    return 255 - image

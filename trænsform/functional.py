from skimage.color import gray2rgb
from skimage.color import rgba2rgb
from skimage import img_as_ubyte
import warnings

from PIL import Image


def toRGB(image, bg=(1, 1, 1)):
    """ convert scikit images to 24-bit RGB

    This function can handle following formats:
        1. Gray scales
        2. RGB formats
        3. RGBA formats

    If the image contains multiple scenes (ex. GIF),
    only the first scene will be processed.
    """

    try:
        h, w, c = image.shape
    except ValueError:
        if len(image.shape) == 2:
            return gray2rgb(image)
        if len(image.shape) == 4:
            return toRGB(image[0], bg)
        raise

    if c == 3:
        return image

    image = rgba2rgb(image, bg)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        image = img_as_ubyte(image)

    return image


def invert(image):
    """ invert 24-bit RGB images read by skimage.io """
    return (255 - image)


def toSquare(img, size=256):
    """ make PIL images to be squares that contain them """
    x, y = img.size

    scale = size / (x if x >= y else y)

    x, y = int(x * scale), int(y * scale)

    new = Image.new('RGB', (size, size))

    box = (size - x) // 2, (size - y) // 2, (size + x) // 2, (size + y) // 2

    new.paste(img, box)

    return new

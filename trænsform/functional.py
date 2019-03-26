from skimage.color import gray2rgb
from skimage.color import rgba2rgb
from skimage import img_as_ubyte
from PIL import Image
import warnings


def toRGB(image, bg=(1, 1, 1)):
    """ convert scikit images to 24-bit RGB

    This function can handle following formats:
    1. Gray scales
    2. RGB formats
    3. RGBA formats
    """
    if len(image.shape) == 2:
        return gray2rgb(image)

    h, w, c = image.shape

    if c == 3: return image

    image = rgba2rgb(image, bg)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        image = img_as_ubyte(image)

    return image


def invert(image):
    """ invert 24-bit RGB scikit images """
    return (255 - image)


def toSquare(img):
    """ make PIL images to be squares that contain them """
    x, y = img.size

    size = x if x >= y else y

    new = Image.new('RGB', (size, size))

    new.paste(img, ((size - x) // 2, (size - y) // 2))

    return new

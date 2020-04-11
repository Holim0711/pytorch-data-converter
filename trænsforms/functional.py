from PIL import Image

__all__ = [
    'square_resize',
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

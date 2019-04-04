from PIL import Image


class SquareResize():

    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError('size should be int: {}'.format(size))
        self.size = size

    def __call__(self, img):
        x, y = img.size

        if x > y:
            x, y = self.size, self.size * y // x
        else:
            x, y = self.size * x // y, self.size

        new = Image.new('RGB', (self.size, self.size))

        new.paste(img, (
            (self.size - x) // 2,
            (self.size - y) // 2,
            (self.size + x) // 2,
            (self.size + y) // 2
        ))

        return new

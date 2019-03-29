from torchvision import transforms as tvtf
from ..functional import toRGB, invert, toSquare


def common(random):
    if random:
        trfm = [tvtf.RandomCrop(224), tvtf.RandomHorizontalFlip()]
    else:
        trfm = [tvtf.CenterCrop(224)]

    trfm += [
        tvtf.ToTensor(),
        tvtf.Normalize(
            [0.485, 0.456, 0.406],  # mean
            [0.229, 0.224, 0.225],  # std
            inplace=True),
    ]

    return trfm


class BasicTrfm(tvtf.Compose):
    def __init__(self, random=True):
        trfm = [
            tvtf.ToPILImage(),
            tvtf.Resize(256),
        ]

        trfm += common(random)

        super().__init__(trfm)


class DirtyTrfm(tvtf.Compose):
    def __init__(self, random=True):
        trfm = [
            tvtf.Lambda(toRGB),
            tvtf.Lambda(invert),
            tvtf.ToPILImage(),
            tvtf.Lambda(toSquare),
        ]

        trfm += common(random)

        super().__init__(trfm)


if __name__ == "__main__":
    from skimage.io import imread
    trfm = DirtyTrfm()
    img = imread("test.jpg")
    img = trfm(img)
    print(img.shape)

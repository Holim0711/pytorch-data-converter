from torchvision import transforms as tvtf
from ..functional import toRGB, invert, toSquare


_normalizer = tvtf.Normalize(
    [0.485, 0.456, 0.406], # mean
    [0.229, 0.224, 0.225], # std
    inplace=True
)


class BasicTrfm(tvtf.Compose):
    def __init__(random=True):
        trfm = [
            tvtf.ToPILImage(),
            tvtf.Resize(256),
        ]

        if random:
            trfm.extend([
                tvtf.RandomCrop(224),
                tvtf.RandomHorizontalFlip(),
            ])
        else:
            trfm.extend([
                tvtf.CenterCrop(224),
            ])

        trfm.extend([
            tvtf.ToTensor(),
            _normalizer,
        ])

        super().__init__(trfm)


class DirtyTrfm(tvtf.Compose):
    def __init__(random=True):
        trfm = [
            tvtf.Lambda(toRGB),
            tvtf.Lambda(invert),
            tvtf.ToPILImage(),
            tvtf.Lambda(toSquare),
            tvtf.Resize(256),
        ]

        if random:
            trfm.extend([
                tvtf.RandomCrop(224),
                tvtf.RandomHorizontalFlip(),
            ])
        else:
            trfm.extend([
                tvtf.CenterCrop(224),
            ])

        trfm.extend([
            tvtf.ToTensor(),
            _normalizer,
        ])

        super().__init__(trfm)


if __name__ == "__main__":
    from skimage.io import imread
    trfm = DirtyTrfm()
    img = imread("test.jpg")
    img = trfm(img)
    print(img.shape)

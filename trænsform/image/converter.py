from torchvision import transforms as tvtf
from ..func import any2rgb, invert
from ..func import SquareResize


rgb_μσ = {
    None: (
        (0.5, 0.5, 0.5),
        (0.5, 0.5, 0.5)),
    "imagenet": (
        (0.485, 0.456, 0.406),
        (0.229, 0.224, 0.225)),
    "cifar10": (
        (0.4914, 0.4822, 0.4465),
        (0.2023, 0.1994, 0.2010)),
    "cifar100": (
        (0.5071, 0.4867, 0.4408),
        (0.2675, 0.2565, 0.2761)),
}


def common(random, normalize):
    if not random:
        tf = [tvtf.CenterCrop(224)]
    else:
        tf = [
            tvtf.RandomCrop(224),
            tvtf.RandomHorizontalFlip(),
        ]

    tf.extend([
        tvtf.ToTensor(),
        tvtf.Normalize(*rgb_μσ[normalize], inplace=True),
    ])

    return tf


class BasicTrfm(tvtf.Compose):
    def __init__(self, random=True, normalize="imagenet"):
        trfm = [
            tvtf.Lambda(any2rgb),
            tvtf.ToPILImage(),
            tvtf.Resize(256),
        ]

        super().__init__(trfm + common(random, normalize))


class InvertTrfm(tvtf.Compose):
    def __init__(self, random=True, normalize=None):
        trfm = [
            tvtf.Lambda(any2rgb),
            tvtf.Lambda(invert),
            tvtf.ToPILImage(),
            SquareResize(256),
        ]

        super().__init__(trfm + common(random, normalize))

import numpy as np
import cv2
import sys

from filters.grayscale import grayscale
from utils.convolve import convolve


def gaussian_kernel(size: int, sigma: float) -> np.ndarray:
    assert size % 2 == 1, "O tamanho do kernel deve ser ímpar."

    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)

    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))

    return kernel / np.sum(kernel)


def gaussian_blur(
    image: np.ndarray, kernel_size: int = 5, sigma: float = 1.0
) -> np.ndarray:
    kernel = gaussian_kernel(size=kernel_size, sigma=sigma)

    return convolve(image=image, kernel=kernel)


def laplacian_filter(image: np.ndarray) -> np.ndarray:
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)

    result = convolve(image=image, kernel=kernel)
    result = np.absolute(result)
    result = np.clip(result, 0, 255).astype(np.uint8)

    return result


def log(image: np.ndarray, kernel_size: int = 5, sigma: float = 1.0) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    blurred_image = gaussian_blur(image=image, kernel_size=kernel_size, sigma=sigma)
    laplacian_image = laplacian_filter(image=blurred_image)

    return laplacian_image


if __name__ == "__main__":
    image = cv2.imread("mock/bobsin.jpg")

    filtered_image = log(image=image, kernel_size=5, sigma=1.0)

    cv2.imshow("LoG Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit(0)

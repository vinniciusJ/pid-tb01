import numpy as np
import sys

from filters.grayscale import grayscale
from utils.correlation import correlation
from utils.normalize import normalize


def mean_correlation(window: np.ndarray, kernel: np.ndarray) -> float:
    return np.mean(window)


def mean_low_pass(image: np.ndarray, kernel_size: int) -> np.ndarray:
    if image.ndim == 3:
        image = grayscale(image=image)

    kernel = np.ones((kernel_size, kernel_size), np.int8)

    result = correlation(image=image, kernel=kernel, correlate_fn=mean_correlation)

    return normalize(image=result)


if __name__ == "__main__":
    import cv2
    import sys

    image = cv2.imread("../mock/bobsin.jpg")

    grayscale_image = mean_low_pass(image=image, kernel_size=3)

    cv2.imshow("Thresholded Image", grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    sys.exit(0)

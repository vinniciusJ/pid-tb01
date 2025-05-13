import numpy as np
import cv2

import sys

from filters.grayscale import grayscale


def basic_high_pass(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    image = grayscale(image=image)

    height, width = image.shape[:2]

    result = np.zeros_like(image)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            region = image[i - 1 : i + 2, j - 1 : j + 2]
            value = np.sum(region * kernel)

            result[i, j] = np.clip(value, 0, 255)

    return result.astype(np.uint8)


if __name__ == "__main__":
    image = cv2.imread("mock/bobsin.jpg")

    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    filtered_image = basic_high_pass(image=image, kernel=kernel)
    # filtered_image = cv2.filter2D(image, -1, kernel)

    cv2.imshow("Thresholded Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    sys.exit(0)

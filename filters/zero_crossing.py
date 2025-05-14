import numpy as np
import cv2
import sys

from filters.grayscale import grayscale


def zero_crossing(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    height, width = image.shape
    result = np.zeros_like(image, dtype=np.uint8)

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            neighborhood = image[i - 1 : i + 2, j - 1 : j + 2]

            min_value = np.min(neighborhood)
            max_value = np.max(neighborhood)

            if min_value < 0 < max_value:
                result[i, j] = 255

    return result.astype(np.uint8)


if __name__ == "__main__":
    image = cv2.imread("mock/bobsin.jpg")

    edges = zero_crossing(image=image)

    cv2.imshow("Zero-Crossing", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit(0)

import numpy as np
import math

from filters.grayscale import grayscale
from utils.normalize import normalize


def log(image: np.ndarray, c: int) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    width, height = image.shape

    result = np.zeros_like(image, dtype=np.float32)

    for i in range(width):
        for j in range(height):
            result[i, j] = c * math.log(1 + image[i, j])

    return normalize(image=result)


if __name__ == "__main__":
    import cv2
    import sys

    image = cv2.imread("../mock/bobsin.jpg")

    filtered_image = log(image=image, c=1)

    cv2.imshow("LoG Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit(0)

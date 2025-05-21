import cv2
import numpy as np
import sys

from filters.grayscale import grayscale
from utils.convolve import convolve

def roberts(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])

    gradient_x = convolve(image=image, kernel=kernel_x)
    gradient_y = convolve(image=image, kernel=kernel_y)

    result = np.sqrt(gradient_x**2 + gradient_y**2)
    result = np.clip(result, 0, 255).astype(np.uint8)

    return result.astype(np.uint8)


if __name__ == "__main__":
    image = cv2.imread("mock/bobsin.jpg")

    filtered_image = roberts(image=image)

    cv2.imshow("Prewitt Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    sys.exit(0)

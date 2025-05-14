import cv2
import numpy as np
import sys

from filters.grayscale import grayscale
from utils.convolve import convolve


def sobel(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float32)

    gradient_x = convolve(image=image, kernel=kernel_x)
    gradient_y = convolve(image=image, kernel=kernel_y)

    result = np.sqrt(gradient_x**2 + gradient_y**2)
    result = np.clip(result, 0, 255).astype(np.uint8)

    return result.astype(np.uint8)


if __name__ == "__main__":
    image = cv2.imread("mock/bobsin.jpg")

    filtered_image = sobel(image=image)

    cv2.imshow("Sobel Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit(0)

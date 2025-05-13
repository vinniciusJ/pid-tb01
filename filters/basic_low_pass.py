import cv2
import numpy as np
import sys

from filters.grayscale import grayscale


def basic_low_pass(image: np.ndarray, kernel_size: int) -> np.ndarray:
    image = grayscale(image=image)

    height, width = image.shape[:2]

    result = np.zeros_like(image)
    
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (
        kernel_size * kernel_size
    )

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            region = image[i - 1 : i + 2, j - 1 : j + 2]
            value = np.sum(region * kernel)

            result[i, j] = np.clip(value, 0, 255)

    return result.astype(np.uint8)


if __name__ == "__main__":
    image = cv2.imread("mock/bobsin.jpg")

    grayscale_image = basic_low_pass(image=image, kernel_size=3)

    cv2.imshow("Thresholded Image", grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    sys.exit(0)

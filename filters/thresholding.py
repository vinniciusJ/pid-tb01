import sys
import cv2
import numpy as np

from filters.grayscale import grayscale


def thresholding(
    image: np.ndarray, threshold: int = 127, max_value: int = 255
) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    copied_image = np.zeros_like(image)

    copied_image[image > threshold] = max_value
    copied_image[image <= threshold] = 0

    return copied_image


if __name__ == "__main__":
    image = cv2.imread("mock/bobsin.jpg")

    thresholded_image = thresholding(image, threshold=127, max_value=255)

    cv2.imshow("Thresholded Image", thresholded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    sys.exit(0)

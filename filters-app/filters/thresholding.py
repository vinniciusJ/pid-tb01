import numpy as np

from filters.grayscale import grayscale


def thresholding(
    image: np.ndarray, threshold: int = 127, max_value: int = 255
) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    result = np.zeros_like(image)

    result[image > threshold] = max_value
    result[image <= threshold] = 0

    return result


if __name__ == "__main__":
    import sys
    import cv2

    image = cv2.imread("mock/bobsin.jpg")

    thresholded_image = thresholding(image, threshold=127, max_value=255)

    cv2.imshow("Thresholded Image", thresholded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    sys.exit(0)

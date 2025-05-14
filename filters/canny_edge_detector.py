import cv2
import numpy as np
import sys

from filters.grayscale import grayscale
from filters.sobel import get_sobel_gradients, sobel
from filters.log import gaussian_blur


def get_angle(image: np.ndarray) -> np.ndarray:
    gradient_x, gradient_y = get_sobel_gradients(image=image)

    angle = np.arctan2(gradient_y, gradient_x) * 180 / np.pi
    angle[angle < 0] += 180

    return angle


def apply_non_maximum_supression(image: np.ndarray, angle: float) -> np.ndarray:
    height, width = image.shape
    result = np.zeros((height, width), dtype=np.float32)
    angle = angle / 45.0
    angle = np.round(angle) % 4

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            q = 255
            r = 255

            if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                q = image[i, j + 1]
                r = image[i, j - 1]
            elif 22.5 <= angle[i, j] < 67.5:
                q = image[i + 1, j - 1]
                r = image[i - 1, j + 1]
            elif 67.5 <= angle[i, j] < 112.5:
                q = image[i + 1, j]
                r = image[i - 1, j]
            elif 112.5 <= angle[i, j] < 157.5:
                q = image[i - 1, j - 1]
                r = image[i + 1, j + 1]

            if (image[i, j] >= q) and (image[i, j] >= r):
                result[i, j] = image[i, j]
            else:
                result[i, j] = 0

    return result


def apply_threshold_histersis(
    image: np.ndarray, low_threshold: float, high_threshold: float
) -> np.ndarray:
    height, width = image.shape
    result = np.zeros((height, width), dtype=np.uint8)

    strong = 255
    weak = 75

    strong_i, strong_j = np.where(image >= high_threshold)
    weak_i, weak_j = np.where((image <= high_threshold) & (image >= low_threshold))

    result[strong_i, strong_j] = strong
    result[weak_i, weak_j] = weak

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if result[i, j] == weak:
                if np.any(result[i - 1 : i + 2, j - 1 : j + 2] == strong):
                    result[i, j] = strong
                else:
                    result[i, j] = 0
    return result


def canny_edge_detector(
    image: np.ndarray, low_threshold: float, high_threshold: float
) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    blurred_image = gaussian_blur(image=image, kernel_size=5, sigma=1.4)

    gradient_magnitude = sobel(image=blurred_image)

    angle = get_angle(image=gradient_magnitude)

    non_maximum_suppression = apply_non_maximum_supression(
        image=gradient_magnitude, angle=angle
    )

    thresholded_image = apply_threshold_histersis(
        image=non_maximum_suppression,
        low_threshold=low_threshold,
        high_threshold=high_threshold,
    )

    return thresholded_image


if __name__ == "__main__":
    image = cv2.imread("mock/example1.jpg")

    filtered_image = canny_edge_detector(
        image=image, low_threshold=50, high_threshold=150
    )

    cv2.imshow("Canny Edge Detector", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit(0)

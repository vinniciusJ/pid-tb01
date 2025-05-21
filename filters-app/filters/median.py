import cv2
import numpy as np
import sys

from filters.grayscale import grayscale

# Passa-baixa mediana
def median_filter(image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    assert kernel_size % 2 == 1

    padding = kernel_size // 2

    padded = np.pad(image, pad_width=padding, mode="edge")
    result = np.zeros_like(image)

    height, width = image.shape[:2]

    for i in range(height):
        for j in range(width):
            window = padded[i : i + kernel_size, j : j + kernel_size]
            result[i, j] = np.median(window)

    return result.astype(np.uint8)


if __name__ == "__main__":
    image = cv2.imread("mock/bobsin.jpg")

    filtered_image = median_filter(image=image, kernel_size=3)

    cv2.imshow("Median Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    sys.exit(0)

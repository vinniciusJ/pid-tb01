import numpy as np

from filters.grayscale import grayscale
from utils.normalize import normalize
from utils.correlation import correlation

def prewitt(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
    kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)

    gx = correlation(image=image, kernel=kernel_x)
    gy = correlation(image=image, kernel=kernel_y)

    result = np.sqrt(gx**2 + gy**2)

    return normalize(image=result)


if __name__ == "__main__":
    import cv2
    import sys

    image = cv2.imread("../mock/bobsin.jpg")

    filtered_image = prewitt(image=image)

    cv2.imshow("Prewitt Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit(0)

import numpy as np

from filters.grayscale import grayscale
from utils.correlation import correlation
from utils.normalize import normalize

def sobel(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float32)

    gx = correlation(image=image, kernel=kernel_x)
    gy = correlation(image=image, kernel=kernel_y)

    result = np.sqrt(gx**2 + gy**2)

    return normalize(image=result)

if __name__ == "__main__":
    import cv2
    import sys

    image = cv2.imread("../mock/bobsin.jpg")

    filtered_image = sobel(image=image)

    cv2.imshow("Sobel Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit(0)

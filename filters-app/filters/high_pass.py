import numpy as np

from filters.grayscale import grayscale
from utils.correlation import correlation
from utils.normalize import normalize

def high_pass(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    if image.ndim == 3:
        image = grayscale(image=image)

    result = correlation(image=image, kernel=kernel)

    return normalize(image=result)

if __name__ == "__main__":
    import cv2
    import sys

    image = cv2.imread("../mock/bobsin.jpg")

    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    filtered_image = high_pass(image=image, kernel=kernel)

    cv2.imshow("Basic high pass image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    sys.exit(0)

import numpy as np

from filters.grayscale import grayscale
from utils.normalize import normalize

def log(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    image = image.astype(np.float32)

    c = 255 / np.log1p(np.max(image))

    result = c * np.log1p(image)

    return normalize(image=result)


if __name__ == "__main__":
    import cv2
    import sys

    image = cv2.imread("../mock/bobsin.jpg")

    filtered_image = log(image=image)

    cv2.imshow("LoG Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    sys.exit(0)

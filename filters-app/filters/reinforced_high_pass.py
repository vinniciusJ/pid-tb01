import cv2
import numpy as np
import sys

from filters.high_pass import high_pass
from filters.grayscale import grayscale
from utils.normalize import normalize


def reinforced_high_pass(
    image: np.ndarray, kernel: np.ndarray, alpha=1.5
) -> np.ndarray:
    grayscale_image = grayscale(image=image)
    high_pass_image = high_pass(image=image, kernel=kernel)

    result = grayscale_image + (alpha * high_pass_image)

    return normalize(image=result)


if __name__ == "__main__":
    import cv2
    import sys

    image = cv2.imread("../mock/bobsin.jpg")

    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    filtered_image = reinforced_high_pass(image=image, kernel=kernel)

    cv2.imshow("Reinforced High Pass Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    sys.exit(0)

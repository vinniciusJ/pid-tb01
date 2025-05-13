import cv2
import numpy as np
import sys

from filters.basic_high_pass import basic_high_pass


def reinforced_high_pass(
    image: np.ndarray, kernel: np.ndarray, alpha=1.5
) -> np.ndarray:
    high_pass_image = basic_high_pass(image=image, kernel=kernel)
    result_image = alpha * high_pass_image

    return result_image.astype(np.uint8)


if __name__ == "__main__":
    image = cv2.imread("mock/bobsin.jpg")

    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    filtered_image = reinforced_high_pass(image=image, kernel=kernel)

    cv2.imshow("Reinforced High Pass Image", filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    sys.exit(0)

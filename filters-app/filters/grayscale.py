import numpy as np


def calculate_default_conversion_matrix(
    red: np.ndarray, blue: np.ndarray, green: np.ndarray
) -> np.ndarray:
    blue_percent = 0.114
    green_percent = 0.587
    red_percent = 0.299

    result = blue_percent * blue + green_percent * green + red_percent * red

    return result.astype(np.uint8)


def grayscale(image: np.ndarray) -> np.ndarray:
    blue = image[:, :, 0].astype(float)
    green = image[:, :, 1].astype(float)
    red = image[:, :, 2].astype(float)

    return calculate_default_conversion_matrix(red, blue, green)


if __name__ == "__main__":
    import sys
    import cv2

    image = cv2.imread("mock/bobsin.jpg")

    grayscale_image = grayscale(image=image)

    cv2.imshow("Thresholded Image", grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    sys.exit(0)

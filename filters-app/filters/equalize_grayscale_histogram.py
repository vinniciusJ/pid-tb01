import numpy as np

from filters.grayscale_histogram import grayscale_histogram
from utils.normalize import normalize


def equalize_grayscale_histogram(image: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    image, histogram = grayscale_histogram(image=image)
    width, height = image.shape
    total_pixels = width * height

    p_r = histogram / total_pixels
    s_k = np.round((len(histogram) - 1) * np.cumsum(p_r)).astype(int)

    equalized_image = normalize(image=s_k[image])
    equalized_histogram = np.bincount(equalized_image.ravel(), minlength=256)

    return equalized_image, equalized_histogram


if __name__ == "__main__":
    import cv2
    import matplotlib.pyplot as plt

    image = cv2.imread("../mock/bobsin.jpg")

    equalized_image, equalized_histogram = equalize_grayscale_histogram(image=image)

    plt.plot(equalized_histogram)
    plt.title("Histograma em escala de cinza")
    plt.xlabel("Valor pixel")
    plt.ylabel("Frequência")
    plt.xlim([0, 255])
    plt.show()

    cv2.imshow("Imagem equalizada", equalized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

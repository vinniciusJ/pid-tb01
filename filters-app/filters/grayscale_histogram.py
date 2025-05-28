import numpy as np

from filters.grayscale import grayscale

def grayscale_histogram(image: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    if len(image.shape) == 3:
        image = grayscale(image=image)

    histogram = np.bincount(image.ravel(), minlength=256)

    return (image, histogram)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import cv2

    image = cv2.imread("../mock/bobsin.jpg")
    _, histogram = grayscale_histogram(image=image)

    plt.plot(histogram)
    plt.title("Histograma em escala de cinza")
    plt.xlabel("Valor pixel")
    plt.ylabel("Frequência")
    plt.xlim([0, 255])
    plt.show()

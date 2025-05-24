import numpy as np

from utils.normalize import normalize


def sum_images(first_image: np.ndarray, second_image: np.ndarray) -> np.ndarray:
    if first_image.shape != second_image.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho.")

    result = first_image + second_image

    return normalize(image=result)


def subtract_images(first_image: np.ndarray, second_image: np.ndarray) -> np.ndarray:
    if first_image.shape != second_image.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho.")

    result = first_image - second_image

    return normalize(image=result)


def multiply_images(first_image: np.ndarray, second_image: np.ndarray) -> np.ndarray:
    if first_image.shape != second_image.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho.")

    result = first_image * second_image

    return normalize(image=result)


def divide_images(first_image: np.ndarray, second_image: np.ndarray) -> np.ndarray:
    if first_image.shape != second_image.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho.")

    result = first_image / second_image

    return normalize(image=result)

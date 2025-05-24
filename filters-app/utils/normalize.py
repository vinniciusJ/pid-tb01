import numpy as np


def normalize_min_max(value: int, min_value: int, max_value: int) -> float:
    return (value - min_value) / (max_value - min_value) * 255


def normalize(image: np.ndarray) -> np.ndarray:
    min_value = np.min(image)
    max_value = np.max(image)

    if np.all(image >= 0) and np.all(image <= 255):
        return image.astype(np.uint8)

    normalized_image = np.zeros_like(image, dtype=np.float32)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            normalized_image[i, j] = normalize_min_max(
                image[i, j], min_value, max_value
            )

    return normalized_image.astype(np.uint8)

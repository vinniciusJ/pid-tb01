import numpy as np


def correlation(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    assert image.ndim == 2, "A imagem deve ser em escala de cinza."
    assert kernel.shape[0] == kernel.shape[1], "O kernel deve ser quadrado."

    height, width = image.shape

    kernel_size = kernel.shape[0]
    padding = kernel_size // 2

    padded_image = np.pad(image, pad_width=padding, mode="edge")

    result = np.zeros_like(image, dtype=np.float32)

    for i in range(height):
        for j in range(width):
            window = padded_image[i : i + kernel_size, j : j + kernel_size]

            result[i, j] = np.sum(window * kernel)

    return result

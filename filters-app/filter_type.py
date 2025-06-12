from enum import Enum

class FilterType(Enum):
    THRESHOLDING = "Limiarização"
    GRAYSCALE = "Escala de Cinza"
    HIGH_PASS = "Passa-Alta básico"
    REINFORCED_HIGH_PASS = "Passa-Alta Alto reforço"
    MEAN_LOW_PASS = "Passa-Baixa Média"
    MEDIAN_LOW_PASS = "Passa-Baixa Mediana"
    ROBERTS = "Operador de Roberts"
    PREWITT = "Operador de Prewitt"
    SOBEL = "Operador de Sobel"
    LOG_TRANSFORM = "Transformacao logaritmica"
    HISTOGRAM = "Histograma (Escala de cinza)"
    HIST_EQUALIZATION = "Equalização de histograma"
    MATH_OPERATIONS = "Operações matemáticas"

    @classmethod
    def list(cls):
        return list(cls)

    @classmethod
    def from_label(cls, label: str):
        for f in cls:
            if f.value == label:
                return f
        raise ValueError(f"Filtro desconhecido: {label}")

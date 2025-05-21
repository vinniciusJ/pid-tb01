from enum import Enum

class FilterType(Enum):
    THRESHOLDING = "Limiarização"
    GRAYSCALE = "Escala de Cinza"
    HIGH_PASS = "Passa-Alta básico"
    HIGH_BOOST = "Passa-Alta Alto reforço"
    LOW_PASS_MEAN = "Passa-Baixa Média"
    LOW_PASS_MEDIAN = "Passa-Baixa Mediana"
    ROBERTS = "Roberts"
    PREWITT = "Prewitt"
    SOBEL = "Sobel"
    LOG_TRANSFORM = "Transformacao logaritmica"
    HISTOGRAM = "Histograma"
    HIST_EQUALIZATION = "Equalização de histograma"

    @classmethod
    def list(cls):
        return list(cls)
    
    @classmethod
    def from_label(cls, label: str):
        for f in cls:
            if f.value == label:
                return f
        raise ValueError(f"Filtro desconhecido: {label}")

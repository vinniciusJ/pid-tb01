from filter_type import FilterType
from filters.thresholding import thresholding
from filters.high_pass import high_pass
from filters.reinforced_high_pass import reinforced_high_pass
from filters.grayscale import grayscale
from filters.mean_low_pass import mean_low_pass
from filters.median_low_pass import median_low_pass
from filters.roberts import roberts
from filters.prewitt import prewitt
from filters.sobel import sobel 
from filters.log import log
from filters.grayscale_histogram import grayscale_histogram
from filters.equalize_grayscale_histogram import equalize_grayscale_histogram

from playground.params.threshold_params import ThresholdParamsWidget
from playground.params.high_pass_params import HighPassParamsWidget
from playground.params.reinforced_high_pass_params import ReinforcedHighPassParamsWidget
from playground.params.low_pas_params import LowPassParamsWidget
from playground.params.log_params import LogParamsWidget

FILTER_REGISTRY = {
    FilterType.THRESHOLDING: {
        "widget": ThresholdParamsWidget,
        "function": thresholding,
    },
    FilterType.GRAYSCALE: {
        "function": grayscale,
    },
    FilterType.HIGH_PASS: {
        "widget": HighPassParamsWidget,
        "function": high_pass,
    },
    FilterType.REINFORCED_HIGH_PASS: {
        "widget": ReinforcedHighPassParamsWidget,
        "function": reinforced_high_pass,
    },
    FilterType.MEAN_LOW_PASS: {
        "widget": LowPassParamsWidget,
        "function": mean_low_pass,
    },
    FilterType.MEDIAN_LOW_PASS: {
        "widget": LowPassParamsWidget,
        "function": median_low_pass,
    },
    FilterType.ROBERTS: {
        "function": roberts,
    },
    FilterType.PREWITT: {
        "function": prewitt,
    },
    FilterType.SOBEL: {
        "function": sobel,
    },
    FilterType.LOG_TRANSFORM: {
        "widget": LogParamsWidget,
        "function": log,
    },
    FilterType.HISTOGRAM: {
        "function": grayscale_histogram,
    },
    FilterType.HIST_EQUALIZATION: {
        "function": equalize_grayscale_histogram,
    },
}

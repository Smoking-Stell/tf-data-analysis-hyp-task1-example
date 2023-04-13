import pandas as pd
import numpy as np
from scipy import stats

chat_id = 461750643 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.02
    control_conversion = x_success / x_cnt
    test_conversion = y_success / y_cnt

    control_std_dev = np.sqrt(control_conversion * (1 - control_conversion) / x_cnt)
    test_std_dev = np.sqrt(test_conversion * (1 - test_conversion) / y_cnt)
    standard_error = np.sqrt(control_std_dev**2 + test_std_dev**2)

    z_statistic = (test_conversion - control_conversion) / standard_error
    p_value = 1 - stats.norm.cdf(abs(z_statistic))

    return p_value / 4 < alpha and z_statistic > 0

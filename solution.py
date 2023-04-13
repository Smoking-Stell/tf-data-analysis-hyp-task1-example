import pandas as pd
import numpy as np
from scipy.stats import ttest_ind_from_stats

chat_id = 461750643 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.02
    control_conversion_rate = x_success / x_cnt
    test_conversion_rate = y_success / y_cnt

    control_std_dev = np.sqrt(control_conversion_rate * (1 - control_conversion_rate) / x_cnt)
    test_std_dev = np.sqrt(test_conversion_rate * (1 - test_conversion_rate) / y_cnt)

    t_statistic, p_value = ttest_ind_from_stats(mean1=control_conversion_rate, std1=control_std_dev, nobs1=control_applications,
                                                mean2=test_conversion_rate, std2=test_std_dev, nobs2=test_applications)

    return p_value < alpha

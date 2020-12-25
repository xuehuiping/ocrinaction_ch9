# -*- encoding: utf-8 -*-
"""
@date: 2020/12/24 10:29 下午
@author: xuehuiping
"""

# 离群值检测
# 代码清单9-3

import numpy as np
from scipy.stats import norm


def detect_outlier(char_probs, thresh=1.4):
    med = np.median(char_probs)
    dev = char_probs - med
    abs_dev = np.absolute(dev)
    med_abs_dev = np.median(abs_dev)
    mod_z_score = abs_dev / med_abs_dev * norm.ppf(0.75)
    error_indices = np.where((mod_z_score > thresh) & (dev < 0))
    return error_indices[0]


if __name__ == "__main__":
    char_probs = [0.9, 0.3, 0.2, 0.4, 0.5, 0.2, -10, -4000]
    print(char_probs)
    r = detect_outlier(char_probs)
    print("离群值所在位置：{}".format(r))
    print("离群值：")
    for i in r:
        print("{} ".format(char_probs[i]), end='')

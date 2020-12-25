# -*- encoding: utf-8 -*-
"""
@date: 2020-12-24 22:22:06
@author: xuehuiping
"""
# 代码清单9-2

import numpy as np


def ngram(seq):
    return np.random.random()


def ngram_char_probs(sentence):
    n = 2
    L = len(sentence)
    assert (L >= n)

    scores = np.zeros(L + n - 1)
    for i in range(L - n + 1):
        seq = sentence[i:i + n]
        scores[i + n - 1] = ngram(seq)
    scores[:n - 1] = scores[n - 1]
    scores[-(n - 1):] = scores[-n]

    avg_scores = np.convolve(scores, np.ones(n) / n, mode='valid')
    return avg_scores


r = ngram_char_probs('我爱你中国')
print (r)

r = ngram_char_probs('ABCDEF')
print (r)
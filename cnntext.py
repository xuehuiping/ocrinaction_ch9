# -*- encoding: utf-8 -*-
"""
@date: 2020/12/25 8:57 上午
@author: xuehuiping
"""
# 代码清单9-5
import torch
import torch.nn as nn
import torch.nn.functional as F


class CNN_Text(nn.Module):
    def __init__(self, vocab_size=100, embed_dim=50, class_num=2, channels=64, ngrams=(2, 3, 4)):
        super(CNN_Text, self).__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.convs1 = nn.ModuleList([nn.Conv2d(1, channels, (size, embed_dim)) for size in ngrams])
        self.fc1 = nn.Linear(len(ngrams) * channels, class_num)

    def forward(self, x):
        x = self.embed(x)
        x = x.unsqueeze(1)
        x = [F.relu(conv(x)).squeeze(3) for conv in self.convs1]
        x = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x]
        x = torch.cat(x, 1)
        logit = self.fc1(x)
        return logit


if __name__ == "__main__":
    model = CNN_Text()
    print(model)

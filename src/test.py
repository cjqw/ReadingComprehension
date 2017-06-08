#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import word2vec
from setting import *

#  http://nbviewer.jupyter.org/github/danielfrg/word2vec/blob/master/examples/word2vec.ipynb

word = input()
model = word2vec.load(BIN_FILE)
index,metrics = model.cosine(word)
# print(model.respo[index])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import word2vec
from setting import *

word2vec.word2phrase(INPUT_FILE, PHRASE_FILE)
word2vec.word2vec(PHRASE_FILE, BIN_FILE, size=100)
word2vec.word2clusters(PHRASE_FILE, CLUSTER_FILE, 100)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import re
import spacy
import ast

import glob
import os

import nltk

def extract_number(string1):
    """
    """
    return re.findall('\d*\.?\d+',string1)


def extract_sentence(string1, keyword):
    """
    """
    return re.findall(r"([^.]*?" + keyword + "[^.]*\.)", string1)


def ngram_to_nlist(string1, n=2):
    """
    """
    ngram = nltk.ngrams(str(string1).split(), n)
    nlist = [" ".join(list(g)) for g in ngram]
    
    return nlist


def ngram_search(search_string, query):
    """
    """
    N = len(query.split(' '))
    query = set([query])
    snlist = set(ngram_to_nlist(search_string, n=N))
    s = list(snlist & query)
    if len(s) > 0:
        x = []
        for S in range(0, len(s)):
            x.append(extract_sentence(search_string, s[S]))
        return (True, query[0], " ; ".join(x[0]))
    else:
        return (False)
    

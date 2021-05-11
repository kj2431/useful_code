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
    ng = len(query.split(' '))
    query = [query]
    nlist = ngram_to_nlist(search_string, n=ng)
    s = list(set(nlist) & set(query))
    if len(s) > 0:
        e1 = []
        for j in range(0, len(s2)):
            e1.append(extract_sentence(search_string, query))
        return True, keyword[0], " ; ".join(e1[0])
    else:
        return False, False, False

    

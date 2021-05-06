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

def ngram_to_nlist(string1, n=2):
    """
    """
    ngram = nltk.ngrams(str(string1).split(), n)
    nlist = [" ".join(list(grams)) for grams in ngram]
    
    return nlist

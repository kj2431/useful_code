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

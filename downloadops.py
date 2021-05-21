import requests
import wget
import urllib.request
import time

import re

import pandas as pd

from tqdm import tqdm 
from multiprocessing.pool import ThreadPool

def parse_pdb_all(url='https://ftp.rcsb.org/pub/pdb/data/structures/all/pdb/'):
    """
    """
    response = requests.get(url)
    s1 = response.text
    s2 = s1.split('\n')
    allpdb = []
    for s in s2:
        i1 = s.find('.ent.gz')
        if i1 != -1:
            allpdb.append(s[i1-7:i1+7])
    return pd.DataFrame({'pdbfile':allpdb, 'url':[url+s for s in allpdb]})

def _download_helper(url, filename):
    wget.download(url+allpdb[i], bar=None, out='pdb/'+filename)

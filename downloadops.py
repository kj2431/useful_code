import requests
import wget
import urllib.request
import time

import re

import numpy as np
import pandas as pd

from tqdm import tqdm 
from multiprocessing.pool import ThreadPool
from joblib import Parallel, delayed

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
    """
    """
    try:
        s = wget.download(url, bar=None, out=filename)
    except:
        print('error-timeout:', url)
    return None



def download_pdb_df(pdb_df):
    """
    """
    s = [_download_helper(pdb_df['url'].iloc[i], pdb_df['pdbfile'].iloc[i]) for i in range(0, len(pdb_df))]
    return None


def download_multiprocess_wrapper(df, processes=64):
    """
    64 async requests for safe downloading; tested with up to 1024 processes (extremely unstable)
    """
    df1n = np.array_split(df, processes)
    cores = list(np.linspace(0, processes-1, processes).astype(int))
    Parallel(n_jobs=processes)(delayed(download_pdb_df)(df_n) for core, df_n in zip(cores, df1n))
    return None


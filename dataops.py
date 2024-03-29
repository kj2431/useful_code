import numpy as np
import pandas as pd

def dataset_count(dataset_ss, countfield='col1', save_csv=False):
    """
    Count all elements in list and drop duplicates.
    
    Parameters
    ----------
    dataset_ss : iterable, list
        The raw data 
    save_csv: boolean, default=False
        Saves csv file
    
    Returns
    -------
    df, pandas.DataFrame object
    """
    
    df = pd.DataFrame({countfield:dataset_ss})
    df['count'] = df.groupby(countfield)[countfield].transform('count')
    if save_csv is True:
        df.drop_duplicates().to_csv('count_'+str(len(dataset_ss))+'.csv', index=False)
    return df.drop_duplicates().sort_values('count', ascending=False)

def dropna_col(df, column='col1'):
    """
    """
    return df[df[column].notna()]

def df_columns_lower(df):
    """
    """
    col_n = [str(i).replace(' ', '').lower() for i in list(df.columns)]
    df.columns = col_n
    return df


def flatten_list(list1):
    """
    Flattens python list
    
    Parameters
    ----------
    list1 : iterable, list
        The raw data containing multiple list of lists
    
    Returns
    -------
    flattened list
    """
    
    return [j for i in list1 for j in i]

def df_list_to_excel(df_list, outputname):
    """
    """
    writer = pd.ExcelWriter(outputname+ '.xlsx')
    for i in range(0, len(df_list)):
        df_list[i].to_excel(writer, sheet_name=str(i), index=False)

    writer.save()
    return 'Done'

### RAY MULTIPROCESSING #############################################################
import time

import ray
ray.init(address='auto')

@timefunc
def to_x():
    """
    """
    df = pd.read_csv('')
    y = df.apply(lambda x: def1(x[0]), axis=1)
    return y

@ray.remote
def to_x_chunk(df):
    """
    """
    y = df.apply(lambda x: def1(x[0]), axis=1)
    return y

@timefunc
def to_x_ray(chunk):
    """
    """
    L = 100000
    df = pd.read_csv('')
    ray_y = ray.get([to_x_chunk.remote(dfc) for dfc in df])
    return ray_y
    

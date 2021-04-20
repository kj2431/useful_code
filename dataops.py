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
    

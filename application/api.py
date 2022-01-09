import numpy as np
import pandas as pd




def create_dataframe1():
    """Create Pandas DataFrame from local CSV."""
    df1 = pd.read_csv('test.txt')
    return df1

def create_dataframe2():
    """Create Pandas DataFrame from local CSV."""
    df2 = pd.read_csv('train.txt',delimiter=';',names=['text','label'])
    return df2

def create_dataframe3():
    """Create Pandas DataFrame from local CSV."""
    df3 = pd.read_csv('val.txt',delimiter=';',names=['text','label'])
    return df3
import pandas as pd
import numpy as np
import sys

def load_df( file_name, ext='csv',):

    ''' 
    This function takes the file extension (only csv and json) and file name as input
    It then loads the data into a pandas data fram and return the dataframe
    
    example:
    load_df(ext='csv', file = 'example.csv')

    returns a pandas dataframe

    '''
  
    if ext == 'csv':
        df = pd.read_csv(file_name)

    elif ext == 'json':
        df = pd.read_json(file_name)


    return df

    
def na_cols(df):
    '''
    this function return the columns containing nans
    
    example:
    na_cols(df)
    
    returns columns containing nan values
    '''
    
    cols = df.loc[:, df.isna().any()].columns
    return list(cols)



def nan_entries_in_col(df):
    
    '''
    This function returns a dict of the total nan entries in each column
    
    example:
    nan_entries_in_col(df)
    
    returns a dict with number of nan entries in each column
    
    '''
    
    col_dict = {}
    
    cols = list(df.columns)
    for col in cols:
        col_dict[col] = np.sum(df[col].isna())
        
    return(col_dict)
        
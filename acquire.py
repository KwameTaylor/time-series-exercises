import numpy as np
import pandas as pd
import requests
import os

def get_opsd_germany():
    """
    Acquires the opsd_germany_daily data from its url,
    caches the data as a csv if there isn't one,
    and reads a csv if there is one present.
    This function returns a DataFrame.
    """
    if os.path.isfile('opsd_germany_daily.csv'):
        df = pd.read_csv('opsd_germany_daily.csv', index_col=0)
    else:
        df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
        df.to_csv('opsd_germany_daily.csv')
    return df

def get_df(name):
    """
    This function takes in the string
    'items', 'stores', or 'sales' and
    returns a df containing all pages and
    creates a .csv file for future use.
    """
    base_url = 'https://python.zach.lol'
    api_url = base_url + '/api/v1/'
    response = requests.get(api_url + name)
    data = response.json()
    
    # create list from 1st page
    my_list = data['payload'][name]
    
    # loop through the pages and add to list
    while data['payload']['next_page'] != None:
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        my_list.extend(data['payload'][name])
    
    # Create DataFrame from list
    df = pd.DataFrame(my_list)
    
    # Write DataFrame to csv file for future use
    df.to_csv(name + '.csv')
    return df

def merge_items_stores_sales(sales_df, stores_df, items_df):
    '''
    This function takes in sales_df, stores_df, and items_df,
    and merges them into one DataFrame.
    '''
    df = pd.merge(sales_df, stores_df, left_on='store', right_on='store_id').drop(columns={'store'})
    df = pd.merge(df, items_df, left_on='item', right_on='item_id').drop(columns={'item'})
    return df
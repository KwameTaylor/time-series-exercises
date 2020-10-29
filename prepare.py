# imports
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from time import strftime

# default viz settings
plt.rc('figure', figsize=(10, 8))
plt.rc('font', size=14)
plt.rc('lines', linewidth=2, c='m')

def prepare_stores_items(df):
    '''
    This function will take in a df and return a df.
    Prepares the stores items data for exploration.
    '''
    # Convert date column to datetime format
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')

    # Set the index to be the datetime variable
    df = df.set_index('sale_date').sort_index()

    # Add 'month' and 'day of week' columns
    df['month'] = df.index.month
    df['weekday'] = df.index.day_name()

    # Add column sales_total
    df['sales_total'] = df.sale_amount * df.item_price

    return df

def prepare_opsd_germany(df):
    '''
    This function will take in a df and return a df.
    Prepares the OPS Germany data for exploration.
    '''
    # Convert date column to datetime format
    df.Date = pd.to_datetime(df.Date, format='%Y-%m-%d')

    # Set the index to be the datetime variable
    df = df.set_index('Date').sort_index()

    # Add month and year columns
    df['month'] = df.index.month
    df['year'] = df.index.year

    # Fill missing values
    df = df.fillna(0)
    
    return df
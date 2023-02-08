#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
'''This is used to identify outliers and then remove them'''
def identify_outlier(df):
    ## Create a vector of 0 of length equal to the number of rows
    temp = np.zeros(df.shape[0])
    ## test each outlier condition and mark with a 1 as required
    for i, x in enumerate(df['engine-size']):
        if (x > 190): temp[i] = 1 
    for i, x in enumerate(df['curb-weight']):
        if (x > 3500): temp[i] = 1 
    for i, x in enumerate(df['city-mpg']):
        if (x > 40): temp[i] = 1      
    df['outlier'] = temp # append a column to the data frame   
    return df

'''Clean the dataframe and then dumped the cleaned data into a CSV file'''
def clean_auto(fileName = "Automobile_price_data_Raw(2).csv", outliers=True):
    ## Load the data  
   
    auto_price = pd.read_csv(fileName)

    ## Convert some columns to numeric values
    cols = ['price', 'bore', 'stroke', 
          'horsepower', 'peak-rpm']
    auto_price[cols] = auto_price[cols].apply(pd.to_numeric, errors='coerce')
    
    ## Replace '?' with nan values
    auto_price.replace('?', np.nan, inplace = True)
    
    ## Checking for missing values
    pd.isnull(auto_price).values.sum()
    
    ## Remove rows with missing values in any columns
    auto_price.dropna(axis = 0, how = 'all', inplace = True)

    # Missing numerical values replaced by their respective column averages and missing categorical with forward fill
    mean = auto_price.mean()






    

    ## Compute the log of the auto price
    auto_price['lnprice'] = np.log(auto_price.price)

    ## Create a column with new levels for the number of cylinders
    auto_price['num-cylinders'] = ['four-or-less' if x in ['two', 'three', 'four'] else 
                                 ('five-six' if x in ['five', 'six'] else 
                                 'eight-twelve') for x in auto_price['num-of-cylinders']]
    ## Removing outliers
    if outliers:
        auto_price = identify_outlier(auto_price)  # mark outliers       
        auto_price = auto_price[auto_price.outlier == 0] # filter for outliers
        auto_price.drop('outlier', axis = 1, inplace = True)

    ### write the data frame into the csv file
    auto_price.to_csv('cleaned_autoprice_data.csv')
    return auto_price


df = clean_auto()

print(df.shape)


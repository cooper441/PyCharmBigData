#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

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
    df['outlier'] = temp  # append a column to the data frame
    return df


'''Clean the dataframe and then dumped the cleaned data into a CSV file'''


def clean_auto(fileName="Automobile_price_data_Raw(2).csv", outliers=True):
    # Load the data

    auto_price = pd.read_csv(fileName)

    # Convert some columns to numeric values
    cols = ['price', 'bore', 'stroke',
            'horsepower', 'peak-rpm']
    auto_price[cols] = auto_price[cols].apply(pd.to_numeric, errors='coerce')

    # Replace '?' with nan values
    auto_price.replace('?', np.nan, inplace=True)

    # Checking for missing values
    pd.isnull(auto_price).values.sum()

    # Remove rows with missing values in any columns
    auto_price.dropna(axis=0, how='all', inplace=True)

    # Missing numerical values replaced by their respective column averages and missing categorical with forward fill
    numdf = auto_price.select_dtypes(include="number")
    catdf = auto_price.select_dtypes(include="category")

    for col in numdf.columns:
        auto_price[col] = auto_price[col].fillna(auto_price[col].mean())

    for col in catdf.columns:
        auto_price[col] = auto_price[col].ffill()

    # Remove duplicate columns
    auto_price.drop_duplicates(subset=["price", "curb-weight", "width", "wheel-base"], inplace=True)

    # Compute the log of the auto price
    auto_price['lnprice'] = np.log(auto_price.price)

    # Create a column with new levels for the number of cylinders
    auto_price['num-cylinders'] = ['four-or-less' if x in ['two', 'three', 'four'] else
                                   ('five-six' if x in ['five', 'six'] else
                                    'eight-twelve') for x in auto_price['num-of-cylinders']]
    # Removing outliers
    if outliers:
        auto_price = identify_outlier(auto_price)  # mark outliers       
        auto_price = auto_price[auto_price.outlier == 0]  # filter for outliers
        auto_price.drop('outlier', axis=1, inplace=True)

    ### write the data frame into the csv file
    auto_price.to_csv('cleaned_autoprice_data.csv')
    return auto_price


# Showing summary stats for outliers and not
# outliers = clean_auto()
# no_outliers = clean_auto(outliers=False)
# print(outliers.describe())
# print("\n\n\n")
# print(no_outliers.describe())


auto_price2 = clean_auto()

## Numeric columns
plot_cols = ["wheel-base",
             "width",
             "height",
             "curb-weight",
             "engine-size",
             "bore",
             "compression-ratio",
             "city-mpg",
             "price",
             "lnprice"]


## Create pair-wise scatter plots
def auto_pairs(plot_cols, df=auto_price2):
    fig = plt.figure(1, figsize=(12, 12))
    fig.clf()
    ax = fig.gca()
    scatter_matrix(df[plot_cols], alpha=0.3, diagonal="kde", ax=ax)
    plt.show()
    return


# auto_pairs(plot_cols)


# Define columns for making a conditioned histogram
plot_cols2 = ["length",
              "curb-weight",
              "engine-size",
              "city-mpg",
              "price"]


# Function to plot conditioned histograms
def cond_hists(df, plot_cols, grid_col):
    # Loop over the list of columns
    for col in plot_cols:
        g = sns.FacetGrid(df, col=grid_col, margin_titles=True)
        g.map(plt.hist, col)
        plt.show()

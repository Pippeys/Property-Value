# Essential packages
import sys
import time
import datetime as dt
from datetime import datetime
import urllib


# Number manipulation
import numpy as np


# Structure manipulation
import pandas as pd
from pandas import Series, DataFrame


# Stats
import scipy as sp
from scipy import stats
from scipy.stats.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import chi2_contingency


# Machine Learning & Preprocessing Package
import sklearn
import sklearn.metrics as sm
from sklearn import preprocessing
from sklearn import decomposition
from sklearn import metrics
from sklearn.preprocessing import scale
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
import pickle

import statsmodels.api as sm
import statsmodels.formula.api as smf

from collections import Counter




def clean_data(x):
    df = x.dropna(axis = 0)
    print(df.head())
    df['sqft'] = df['Bldg SF']
    df['cap'] = df['Cap_Rate'].astype(int)
    df['units'] = df['Number Of Units']
    df['yearbuilt'] = df['Year Built'].astype('str').str[:-3]
    df['yearbuilt'] = df['yearbuilt'].astype(int)
    df['Property Zip Code'] = df['Property Zip Code'].astype('str').str[:-1]
    def remover(s):
        return int(s[-4:])

    df['year'] = [remover(s) for s in df['Sale Date']]
    df['sale_year'] = df['year'].astype('str')
    df['zipper'] = df['Property Zip Code']
    mf = df.loc[df['PropertyType'] == 'Multi-Family']
    mf = mf.loc[mf['sale_year'] != '2007']
    mf = mf.loc[mf['sale_year'] != '2008']
    mf = mf.loc[mf['sale_year'] != '2009']
    mf = mf.loc[mf['sale_year'] != '2010']
    mf = mf.loc[mf['sale_year'] != '2011']
    return(mf)

def regression (mf):
    #Regression Model
    est = smf.ols(formula = 'np.log(Sale_Price) ~ (cap + (np.log(units)/np.log(sqft)) + yearbuilt) * C(zipper)', data = mf)
    results = est.fit()
    # For pickling later
    #joblib.dump(results, 'Property_Estimator.pkl')
    #LinReg = joblib.load('Property_Estimator.pkl')

    # Inputting info for individual estimate
    print('CAP rate: ')
    capper = float(input())
    print('Number of Units: ')
    num_units = int(input())
    print('Square Footage: ')
    sqfts = int(input())
    print('Year Built: ')
    year = input()
    year = int(year[:-1])
    print('Zip Code: ')
    zipped = input()
    zipped = zipped[:-1]

    # Building the DF for the user inputted properties. Could be used in Machine Learning later if users are frequent.
    a = pd.DataFrame({'cap':[capper],'units':[num_units], 'sqft':[sqfts],'yearbuilt':[year], 'zipper':[zipped]})
    ans = results.predict(a)
    price = np.exp(ans).astype(int)
    ppsf = price/a.sqft
    print('Price: ')
    print(price)
    print('Price per SQFT: ')
    print(ppsf.values)


    return(price, ppsf.values)


def main():
    # Loading Data
    # Mac
    #x = pd.read_csv('C:/Users/magicsoccer10/Dropbox/twerk werk/cre_values')
    # Arch
    #x = pd.read_csv('C:/Users/scott/Dropbox/twerk werk/Data/cre_values.csv')
    # Work
    x = pd.read_csv('C:/Users/sstandring/Dropbox/twerk werk/Data/cre_values.csv')


    mf = clean_data(x)
    model = regression(mf)





if __name__ == '__main__':
    main()

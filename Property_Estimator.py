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
from pandas.tools.plotting import scatter_matrix


# Graphing
import seaborn as sb

import matplotlib.pyplot as plt
from matplotlib import rcParams


# Stats
import scipy as sp
from scipy import stats
from scipy.stats.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import chi2_contingency


# Machine Learning & Preprocessing Package
import sklearn
import sklearn.metrics as sm
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LassoCV
from sklearn.linear_model import LassoLarsCV
from sklearn.linear_model import LassoLarsIC
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import preprocessing
from sklearn import decomposition
from sklearn import metrics
from sklearn.cluster import DBSCAN
from sklearn.decomposition import FactorAnalysis
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import scale
from sklearn.preprocessing import LabelEncoder
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
import pickle

import statsmodels.api as sm
import statsmodels.formula.api as smf

from collections import Counter

import networkx as nx



# Parameters for graphs
#%matplotlib inline
#rcParams['figure.figsize'] = 10,10
#sb.set_style('whitegrid')





def clean_data(x):
    x = x.dropna(axis = 0)
    df['sqft'] = df['Bldg SF']
    df['cap'] = df['Cap_Rate'].astype(int)
    df['units'] = df['Number Of Units']
    df['yearbuilt'] = df['Year Built'].astype('str').str[:-3]
    df['yearbuilt'] = df['yearbuilt'].astype(int)

    df['Property Zip Code'] = df['Property Zip Code'].astype('str').str[:-1]
    df['bin_zip'] = num.fit_transform(df['Property Zip Code'].astype('str'))
    df['zipper'] = df['Property Zip Code'].astype('str')
    mf = df.loc[df['PropertyType'] == 'Multi-Family']
    mf = mf.loc[mf['sale_year'] != '2007']
    mf = mf.loc[mf['sale_year'] != '2008']
    mf = mf.loc[mf['sale_year'] != '2009']
    mf = mf.loc[mf['sale_year'] != '2010']
    mf = mf.loc[mf['sale_year'] != '2011']
    return(mf)

def regression (x,y):
    #Regression Model
    est = smf.ols(formula = 'np.log(Sale_Price) ~ (cap + (np.log(units)/np.log(sqft)) + yearbuilt) * C(zipper)', data = mf)
    results = est.fit()
    joblib.dump(results, 'Property_Estimator.pkl')
    LinReg = joblib.load('Property_Estimator.pkl')
    return(LinReg.fit(x,y))

def main():
    # Loading Data
    # Mac
    #x = pd.read_csv('C:/Users/magicsoccer10/Dropbox/twerk werk/cre_values')
    # Arch
    x = pd.read_csv('C:/Users/scott/Dropbox/twerk werk/Data/cre_values.csv')
    # Work
    #x = pd.read_csv('C:/Users/sstandring/Dropbox/twerk werk/cre_values')





if __name__ == '__main__':
    main()

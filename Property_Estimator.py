# Essential packages
import pandas as pd
import numpy as np

# Preprocessing Packages
import sklearn
import sklearn.metrics as sm
from sklearn.preprocessing import scale
from sklearn.preprocessing import LabelEncoder

# Machine Learning Packages
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.svm import SVR

#pickle model
from sklearn.externals import joblib
import pickle

# Loading Data
# Mac
#df = pd.read_csv('C:/Users/magicsoccer10/Dropbox/twerk werk/cre_values')

# Arch
#df = pd.read_csv('C:/Users/scott/Dropbox/twerk werk/cre_values')

# Work



# Transforming data for modeling (based on exploration: (See Jupyter/Learning_Satyrn))
def transform(df):
    df['log_price'] = np.log(df.Sale_Price)
    df['log_sqft'] = np.log(df['Bldg SF'])
    num = LabelEncoder()
    df['Property Zip Code'] = df['Property Zip Code'].astype(str).str[:-2]
    df['bin_zip'] = num.fit_transform(df['Property Zip Code'].astype('str'))
    # Filtering by Multi-Family and Create modelling DataFrame
    mfdf = df.loc[df['PropertyType'] == 'Multi-Family']
    mfquant = mfdf[['log_price','Cap_Rate','log_sqft','bin_zip']]
    return mfquant

def regression (x,y):
    #Regression Model
    LinReg = LinearRegression(normalize=True)
    LinReg.fit(x,y)
    #RFE(LinReg,3)
    #estimator = SVR(kernel='linear')
    #selector = RFE(estimator, 5, step=1)
    #selector.support_
    #selector.ranking_
    joblib.dump(LinReg, 'Property_Estimator.pkl')
    LinReg = joblib.load('Property_Estimator.pkl')
    return(LinReg.fit(x,y))

def main():
    df = pd.read_csv('C:/Users/sstandring/Dropbox/twerk werk/cre_values')
    mfquant = transform(df)
    #Specifying Independent Variables and Dependent Variables
    mf_data = mfquant.ix[:,(1,2,3)].values
    mf_target = mfquant.ix[:,0].values
    mf_data_names = ['Cap','Sqft','bin_zip']
    x, y = scale(mf_data), mf_target
    LinReg = regression(x,y)
    print (LinReg.score(x,y))

if __name__ == '__main__':
    main()

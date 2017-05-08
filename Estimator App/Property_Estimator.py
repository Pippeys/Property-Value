# Essential packages
import pandas as pd
import numpy as np

# Machine Learning & Preprocessing Packages
import sklearn
import sklearn.metrics as sm
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import RFE
from sklearn.svm import SVR
# Loading Data
# Mac
#df = pd.read_csv('/Users/magicsoccer10/Dropbox/twerk werk/Property Value/07-17.csv')

# Arch
#df = pd.read_csv('C:/Users/scott/Dropbox/twerk werk/Property Value/07-17.csv')

# Work
df = pd.read_csv('C:/Users/sstandring/Dropbox/twerk werk/Property Value/07-17.csv')


df['sale_date'] = pd.to_datetime(df['Sale Date'])
df['sale_quarter'] = df['sale_date'].dt.quarter
df['sale_quarter'] = df['sale_quarter'].astype('int')
df['log_price'] = np.log(df.Sale_Price)
df['log_sqft'] = np.log(df['Bldg SF'])
df['log_far'] = np.log(df['Floor Area Ratio'])
num = LabelEncoder()
df['bin_zip'] = num.fit_transform(df['Property Zip Code'].astype('str'))


mfdf = df.loc[df['PropertyType'] == 'Multi-Family']
mfquant = mfdf[['log_price','Cap_Rate','log_sqft','bin_zip']]

mf_data = mfquant.ix[:,(1,2,3)].values
mf_target = mfquant.ix[:,0].values
mf_data_names = ['Cap','Sqft','bin_zip']
x, y = scale(mf_data), mf_target
LinReg = LinearRegression(normalize=True)
LinReg.fit(x,y)
print (LinReg.score(x,y))
RFE(LinReg,3)
estimator = SVR(kernel='linear')
selector = RFE(estimator, 5, step=1)
selector.support_
selector.ranking_

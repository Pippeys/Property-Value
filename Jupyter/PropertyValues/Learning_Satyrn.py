
# coding: utf-8

# # Learning Satyrn

# In[104]:

import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame
from pandas.tools.plotting import scatter_matrix
from matplotlib import rcParams


# In[2]:

df = pd.read_csv('C:/Users/sstandring/Dropbox/twerk werk/Property Value/07-17.csv')
df


# #### Count Missing Values

# In[3]:

df.isnull().sum()


# #### Grouping

# In[4]:

grouped = df.groupby(df['PropertyType'])
grouped.median()


# ### Graphing and Plotting

# In[5]:

#get_ipython().magic('matplotlib inline')
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')


# In[65]:

plt.pie(df['Property Zip Code'])
plt.show()


# In[61]:

x = df['Sale_Price']
y = df['Year Built']
fig = plt.figure()
ax = fig.add_axes([.1, .1, 1,1])
ax.set_xlim([1875,2020])
ax.set_ylim([0,500000000])
ax.plot(df['Year Built'],df['Sale_Price'])


# In[60]:

fig = plt.figure()
fig, (ax1, ax2) = plt.subplots(1,2)

ax1.plot(df['Sale_Price'])
ax2.plot(df['Year Built'])


# In[53]:

plt.bar(df['Year Built'], df['Sale_Price'])


# In[73]:

data = df[['Cap_Rate', 'Floor Area Ratio']]
data.plot()


# In[106]:

cp = df['Cap_Rate']
cp.plot(kind = 'hist')


# In[115]:

df['Sale_Price'].plot(kind = 'hist')


# In[118]:

df['Sale Date'].plot(kind = 'hist')


# #### Coloring

# In[94]:

color =  ['salmon']
plt.bar(df['Year Built'], df['Sale_Price'], color = color)


# In[78]:

color_theme = ['darkgray','powderblue']
data.plot(color = color_theme, ls="--")


# #### Labels

# In[97]:

plt.plot(data, marker = '+')
ax.set_ylim([0,20])
plt.xlabel('record ID')
plt.ylabel('Cap Rate & FAR')


# In[103]:

df['Bldg SF'].plot()
ax.set_xticks(range(32))
ax.set_xticklabels(df.PropertyType, rotation=60, fontsize = 'small')
ax.set_title('Building SquareFootage by Property Type')

ax.set_xlabel('Building Type')
ax.set_ylabel('Square-footage')

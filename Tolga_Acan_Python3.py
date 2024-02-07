#!/usr/bin/env python
# coding: utf-8

# # Python 3
# For this tutorial we'll be using the Iris dataset from sklearn. 
# 
# In this notebook we will:
# 1. Import required modules and dataset
# 2. Define multiple Classification models
# 3. Fit the data to our models
# 4. Use our trained models to predict a class label 
# 5. Evaluate our models and chose the best performing model 
# 
# 

# In[6]:


#Import Pandas to your workspace
import pandas as pd


# In[12]:


#Read the "features.csv" file and store it into a variable
features = pd.read_csv('features.csv')


# In[13]:


#Display the first few rows of the DataFrame
features.head()


# <h1>groupby()</h1>
# 
# <ul>
#     <li>groupby combines 3 steps all in one function:
#         <ol>
#             <li>Split a DataFrame</li>
#             <li>Apply a function</li>
#             <li>Combine the results</li>
#         </ol>
#     </li>
#     <li>groupby must be given the name of the column to group by as a string</li>
#     <li>The column to apply the function onto must also be specified, as well as the function to apply</li>
# </ul>

# <img src="groupbyviz.jfif"/>

# In[29]:


year_CPI = features.groupby(["Year", "Month"])["CPI"].mean().reset_index()


# In[30]:


year_CPI.head()


# In[28]:


year_CPI.sort_values(by="CPI", ascending=False).head()


# In[33]:


#Read the "stores.csv" file and store it into a variable called stores
stores = pd.read_csv('stores.csv')


# In[34]:


#Display the first few rows of the stores DataFrame
stores.head()


# In[42]:


#Convert the values in the Type column from upper to lower case 
stores["Type"] = stores["Type"].str.lower()


# In[43]:


#Rename the 'Size' column to 'Area'
stores.rename(columns = {'Size':'Area'}, inplace=True)


# In[44]:


#Display the first few rows to verify changes
stores.head()


# # <h1>merge()</h1>
# 
# <ul>
#     <li>Merge two DataFrames along common columns</li>
#     <li>Must be provided the DataFrame to merge with, as well as the names of the common columns</li>
#     <li>Will merge and map rows where the values in both DataFrames are equal</li>
# </ul>

# <img src="mergetypes.png"/>

# <img src="mergeinner.png"/>

# In[46]:


features.head()


# In[47]:


stores.head()


# In[49]:


df_merged = features.merge(stores, on="Store")


# In[50]:


df_merged.head()


# In[51]:


print(features.shape)
print(stores.shape)
print(df_merged.shape)


# In[52]:


#Export the final version of our DataFrame to a .csv file named "final_data.csv" 
df_merged.to_csv('final_data.csv', index=False, header=True)

df_merged.to_excel('final_data.xlsx', index=False, header=True)


# <h1>Part 2 - Machine Learning</h1>

# In[68]:


#Import libraries we will need

# numpy
import numpy

# scikit-learn
import sklearn

import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

from sklearn import model_selection

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn import datasets

from IPython.display import display

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)


# In[84]:


dataset['feature_names']


# In[85]:


dataset.feature_names


# In[82]:


#2.2 Load Dataset
dataset = datasets.load_iris()
feature_names = dataset['feature_names']

iris_data = pd.DataFrame(data=dataset.data, columns=feature_names)
target = pd.Series (data=dataset['target'])

print(feature_names)
iris_data.head()


# In[83]:


target.head()


# In[79]:


display(dataset)


# In[86]:


#3. Summarize The Dataset

#3.1 Dimensions of Dataset
print(iris_data.shape)


# In[87]:


#3.2 Peek at the Data
iris_data.head()


# In[88]:


#3.3 Statistical Summary
iris_data.describe()


# In[89]:


#3.4 Class Distribution
#Group target variable by the class column and apply the size function
target.value_counts()


# In[93]:


#4. Data Visualization

#4.1 Univariate Plots

# box and whisker plots
iris_data.plot(kind='box', subplots=True, layout=(2,2),
              sharex = True, sharey = True)

plt.show()


# In[94]:


# histograms
iris_data.hist()
plt.show()


# In[95]:


#4.2 Multivariate Plots

# scatter plot matrix
scatter_matrix(iris_data)
plt.show()


# In[103]:


#5. Evaluate Some Algorithms

#5.1 Create the Test set
X = iris_data[feature_names].values
Y = target.values

test_size = 0.20

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(
    X, 
    Y, 
    test_size = test_size, 
    random_state=7
)


# In[104]:


X_train.shape


# In[105]:


X_test.shape


# In[106]:


LDA = LinearDiscriminantAnalysis()


# In[111]:


LDA.fit (X_train, Y_train)


# In[114]:


LDA.score(X_test, Y_test)


# In[115]:


X_test[:5]


# In[119]:


Y_test


# In[120]:


LDA.predict (X_test)


# In[ ]:





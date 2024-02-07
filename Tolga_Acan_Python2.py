#!/usr/bin/env python
# coding: utf-8

# ## Pandas 
# 
# Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
# built on top of the Python programming language. 
# 
# It will seamlessly bridge the gap between Python and Excel.

# ## Jupyter Notebook 
# 
# This is a web-based application (runs in the browser) that is used to interpret Python code. 
# 
# - To add more code cells (or blocks) click on the **'+'** button in the top left corner
# - There are 3 cell types in Jupyter:
#     - Code: Used to write Python code
#     - Markdown: Used to write texts (can be used to write explanations and other key information)
#     - NBConvert: Used convert Jupyter (.ipynb) files to other formats (HTML, LaTex, etc.) 
#     
# 
# - To run Python code in a specific cell, you can click on the **'Run'** button at the top or press **Shift + Enter**
# - The number sign (#) is used to insert comments when coding to leave messages for yourself or others. These comments will not be interpreted as code and are overlooked by the program
# 

# In[5]:


#Import pandas and assign it to a shorthand name pd 
import pandas as pd


# <h1>Reading CSV Files</h1>
# 
# <ul>
#     <li>Function to use in Pandas: read_csv()</li>
#     <li>Value passed to read_csv() must be string and the <b>exact</b> name of the file</li>
#     <li>CSV Files must be in the same directory as the python file/notebook</li>
# </ul>

# In[22]:


#Read our data into a DataFrame names features_df
#read_excel does the same but for spreadsheet files
features_df = pd.read_csv('features.csv')


# <h1>Basic DataFrame Functions</h1>
# 
# <ul>
#     <li>head() will display the first 5 values of the DataFrame</li>
#     <li>tail() will display the last 5 values of the DataFrame </li>
#     <li>shape will display the dimensions of the DataFrame</li>
#     <li>columns() will return the columns of the DataFrame as a list</li>
#     <li>dtypes will display the types of each column of the DataFrame</li>
#     <li>drop() will remove a column from the DataFrame</li>
# </ul>

# In[23]:


#Display top 5 rows
features_df.head()
#nan values are essentially empty entries


# In[24]:


#Display bottom 5 rows
features_df.tail()


# In[25]:


#Print dimensions of DataFrame as tuple
print(features_df.shape[0])
print(features_df.shape[1])


# In[91]:


#Print list of column values
features_df.columns


# In[95]:


#We can rename all columns at once by reassigning the .columns attribute
#Copy paste output from cell above and change column names accordingly
features_df.columns = ['Store', 'Date', 'Temperature', 'Fuel_Price', 'MD1', 'MD2', 'MD3', 'MD4', 'MD5', 'CPI', 'Unemployment', 'IsHoliday']
features_df.head()



# In[8]:


#To only rename specific columns
features_df.rename (columns={'Temperature':'Temp'}, inplace=True)


# In[96]:


#Print Pandas-specific data types of all columns
features_df.dtypes


# <h1>Indexing and Series Functions</h1>
# 
# <ul>
#     <li>Columns of a DataFrame can be accessed through the following format: df_name["name_of_column"] </li>
#     <li>Columns will be returned as a Series, which have different methods than DataFrames </li>
#     <li>A couple useful Series functions: max(), median(), min(), value_counts(), sort_values()</li>
# </ul>

# In[29]:


#Extract CPI column of features_df
features_df['CPI'].head()


# In[97]:


#We can use the in keyword as seen in Python 1
1 in features_df['Store']


# In[34]:


#Check the number of dimensions of our Data with 'ndim'
#Display the dimensions with 'shape'
#Display the total number of entries with 'shape'
# Example with our DataFrame
print(features_df.ndim)
print(features_df.shape)
print(features_df.size)

print(features_df['CPI'].ndim)
print(features_df['CPI'].shape)
print(features_df['CPI'].size)


# In[37]:


# Example with our a column from our DataFrame
features_df["CPI"].max()


# In[36]:


#Maximum value in Series
features_df["CPI"].min()


# In[35]:


#Median value in Series
features_df['CPI'].median()


# In[40]:


#Minimum value in Series
features_df['CPI'].describe()


# In[39]:





# In[41]:


# To Check if the values in a column are unique 
features_df['Store'].is_unique


# In[42]:


#Print list of unique values
features_df['Store'].unique()


# In[44]:


#Print unique values and frequency
features_df['Date'].value_counts()


# In[48]:


#Return a sorted DataFrame acording to specified column
features_df.sort_values(by=["Store", "Date"], ascending=True).head()


# In[ ]:





# In[52]:


# Drop duplicates for categorical data across a specific column
print (features_df.shape)
print(features_df.drop_duplicates(subset=["Store"]).shape)
features_df.drop_duplicates(subset=["Store"]).head()


# In[99]:


# delete one column
features_df.drop(columns= "MarkDown1").tail()


# In[56]:


#Matrix of missing values
features_df.isnull().head()


# In[57]:


#Find the number of missing values per column
features_df.isnull().sum()


# In[59]:


#Delete any row with missing data (NaN) in it
print(len(features_df.dropna()))
features_df.dropna().head()


# In[60]:


#Delete any column with missing data (NaN) in it
features_df.dropna(axis=1).head()


# In[62]:


#Look along specific columns for NaN
print(len(features_df.dropna(subset=['CPI'])))
print(features_df.shape)


# In[63]:


#Replace NaN (empty) values with 0's
features_df.fillna(0).head()


# In[64]:


# delete multiple columns
features_df.drop(columns=["MarkDown1", "MarkDown2", "MarkDown3", "MarkDown4", "MarkDown5"], inplace=True)


# In[65]:


features_df.drop(columns=["IsHoliday"])


# In[68]:


#Define a function to convert float values to our custom categorical ranges
def temp_categorical (temp) :
    if temp < 50:
        return 'Mild'
    elif temp >= 50 and temp < 80:
        return 'Warm'
    else: 
        return 'Hot'


# In[67]:


#With the apply() function we can apply our custom function to each value of the Series
feature_df['Temp'] = features_df['Temp'].apply(temp_categorical)


# In[70]:


#If we would like to define a 'one time use' anonymous function, we can use the 'lambda' keyord
features_df['Temp'].head()


# In[72]:


features_df['Unemployment'].head()


# In[71]:


features_df['Unemployment'].apply(lambda num: num + 1).head()


# In[73]:


features_df.dtypes


# <h1>Indexing</h1>
# 
# <ul>
#     <li>Because Pandas will select entries based on column values by default, selecting data based on row values requires the use of the iloc method. 
#     </li>
#     <li>
#       Allowed inputs are:
#         <ul>
#             <li>An integer, e.g. 5.</li>
#             <li>A list or array of integers, e.g. [4, 3, 0].</li>
#             <li>A slice object with ints, e.g. 1:7.</li>
#         </ul>
#     </li>
# </ul>

# In[74]:


#Return Fuel_Price to IsHoliday columns of 0-10th rows
#Note how LOC can reference columns by their names
features_df.loc[20:30, "Fuel_Price": "IsHoliday"]


# In[75]:


features_df.loc[100:105]


# In[79]:


features_df.loc[:,["Store", "IsHoliday"]].head()


# In[ ]:





# In[80]:


#Retrieve a couple rows from their ROW index values
features_df.iloc[0, 1]


# In[81]:


#Similar to arrays, we can use splicing to access multiple rows
features_df.iloc[:5]


# In[82]:


#We may also provide specific row/column values to access specific values
features_df.iloc[[0,2], [1,3]]


# In[84]:


#We can also splice multiple rows / columns
features_df.iloc[1:5, 0:3]


# <h1>Formatting Data</h1>
# 
# <ul>
#     <li>To access and format the string values of a DataFrame, we can access methods within the "str" module of the DataFrame </li>
#     <li>We may also format float values using options.display.float_format() in Pandas</li>
# </ul>

# In[85]:


#By accessing .str, we gain access to all the string methods we covered in Python 1!
#new data frame with split value columns 
print ("This is Python 2 - Pandas".split())
print ("This is Python 2 - Pandas".split('-'))


# In[86]:


features_df.head()


# In[87]:


new = features_df["Date"].str.split("-", expand=True)

new.head()


# In[88]:


#Declare new column named Year to be first column of new DataFrame
features_df['Year'] = new [0]

features_df['Month'] = new[1]


# In[89]:


features_df.head()


# In[90]:


#Format float 
features_df.round(2).head()


# 

# In[100]:


features_df.head()


# In[101]:


#Check data types of new columns
features_df.dtypes


# In[103]:


#Convert Year and Month to integers from string
features_df['Year'] = features_df['Year'].astype('int64')
features_df['Month'] = features_df['Year'].astype('int64')


# In[102]:


#Return rows with year value of 2011
year_filt = features_df["Year"] == 2011

feb_df = features_df[filt]
feb_df.head()


# In[43]:


#Return rows with CPI lower than 130
CPI_filt = features_df["CPI"] < 130
low_CPI = features_df[CPI_filt]
low_CPI.head()


# In[44]:


#Return rows with year equal to 2010 AND unemployment larger than 8


# In[45]:


#Return rows with temp larger than 40 OR Store number equal to 4


# In[46]:


##CLASS EXERCISE 
# find the rows with Fuel_Price larger than 3.00 AND IsHoliday is True
filt1 = features_df["IsHoliday"] == True
filt2 = features_df["Fuel_Price"] > 3.00

holiday_Fuel = features_df [filt1 & filt2]


# In[104]:


holiday_Fuel.head()


# In[47]:


# find the rows with CPI < 200  OR Unemployment < 5


# In[ ]:





# In[48]:


#Export the current version of our DataFrame to a .csv file
features_df.to_csv("features_final.csv", index=False, header=True)
#to_excel also an option to export to Excel Spreadsheet
features_df.to_excel("features_final.xlsx", index=False, header=True)


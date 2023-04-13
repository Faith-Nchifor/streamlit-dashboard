#!/usr/bin/env python
# coding: utf-8

# # EDA for LA crime datasets
# The datasets involved are:
# * Arrest data from 2010-2020
# * Crime data from 2010-2020
# ###### More ideas are welcome

# In[1]:




import numpy as np # linear algebra
import pandas as pd 
pd.option_context('display.max_columns', None, 'display.max_rows', None)
import matplotlib.pyplot as plt
import seaborn as sns

# In[2]:


arrest_data=pd.read_csv('arrest_cleaned.csv',parse_dates=['Arrest Date','Booking Date'])
crime_types=pd.read_csv('crime-cleaned.csv',parse_dates=['Date Rptd','DATE OCC'])





crime_years_df=crime_types.groupby('Date Rptd').size()
#sns.baplot(data=crime_years_df, x='Date Rptd',y='Vict Age')
plt.hist([2,3,5,5,3,1,2])
plt.show()


# In[ ]:





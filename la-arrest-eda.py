import streamlit as st


import numpy as np # linear algebra
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
#import folium
#pd.option_context('display.max_columns', None, 'display.max_rows', None)



# In[2]:

#arrest_data=pd.read_csv('arrest_cleaned.csv',parse_dates=['Arrest Date','Booking Date'])
#crime_types=pd.read_csv('crime-cleaned.csv',parse_dates=['Date Rptd','DATE OCC'])
df=pd.read_csv('sports-political-donations.csv')
print(df.head())
print(df['Team'].value_counts().reset_index())
parties=df['Party'].value_counts().reset_index()

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.bar_chart(parties, x='index',y='Party')


m = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])

st.map(m)


fig, ax = plt.subplots()
#plt.plot(df['Team'].value_counts())
sns.countplot(y='Team',data=df)
st.pyplot(fig)

st.line_chart(df['Team'].value_counts().reset_index(), x='Team')








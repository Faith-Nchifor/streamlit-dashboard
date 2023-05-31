import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

#helpful functiions
def sev(x):    
    if ((x>=4) & (x<8)):
        return 'moderate'
    elif(x<=3):
        return 'mild'
    else:
        return 'severe'
#print(df.columns)

df=pd.read_csv('./asthma_allergies.csv',index_col='SUBJECT_ID')
df=df[df.AGE_START_YEARS>0.0]
df.ASTHMA_END=df.ASTHMA_END.astype(int)
df.ASTHMA_START=df.ASTHMA_START.astype(int)
df.AGE_END_YEARS=df.AGE_END_YEARS.astype(int)
df.AGE_START_YEARS=df.AGE_START_YEARS.astype(int)
df['A_S_SEV']=df['ASTHMA_START'].apply(lambda x:sev(x))
df['A_E_SEV']=df['ASTHMA_END'].apply(lambda x:sev(x))
avg_td=df.ASTHMA_END- df.ASTHMA_END


df_by=df.groupby('BIRTH_YEAR')['AGE_START_YEARS'].mean()

#df_asthma=df[[['BIRTH_YEAR','ASTHMA_END','ASTHMA_START','GENDER_FACTOR']]]
st.header('Asthma allergy analysis in Children')
kp1,kp2 = st.columns(2)
kp1.metric(
label='Total Population',
value=df.shape[0]
)

kp2.metric(
    label='Average study duration',
    value=str(int(df_by.mean()))+' years'
)


c1,c2 = st.columns(2)

c3,c4= st.columns(2)

con=st.container()


with c1:
    st.text('The birth year with the most persons is 1994 ')
    yrs=df.groupby('BIRTH_YEAR').size().reset_index()
    ax=plt.figure()
    #sns.histplot(x=df['BIRTH_YEAR'])
    sns.lineplot(x='BIRTH_YEAR',y=0,data=yrs)
    plt.title('Birth year distribution for various patients')
    st.pyplot(ax)
with c2:
    st.text('This study shows that over 50% of persons belong to white race')
    data=df.groupby('RACE').size()
    values=data.values
    races=data.index
    colors = sns.color_palette('pastel')[0:5]

    ax=plt.figure()
    #plt.plot(df_by)
    plt.pie(data, labels = races, colors = colors, autopct='%.0f%%')
    plt.title('Population race distribution')
    st.pyplot(ax)
with c3:
    st.write('Majority of the population are within ages 0.0 - 0.9')
    
#df_age=pd.crosstab(df.AGE_START_YEARS,[df.RACE,df.ASTHMA_START])
with c4:
    ax=plt.figure()
    sns.distplot(x=df.AGE_START_YEARS)
    plt.ylabel('')
    plt.title('Age distribution')
    plt.xlabel('Age')
    #plt.legend()
    st.pyplot(ax)
    
with con:
    st.write('These following plots show that the asthma status of most patients is mild in their first years and later moves from moderate to severe in their later years')
    df_age_s=pd.crosstab(df['AGE_START_YEARS'],df['A_S_SEV'])
    df_age_e=pd.crosstab(df['AGE_END_YEARS'],df['A_E_SEV'])
    fig,ax=plt.subplots(2)    
    df_age_s.plot(kind='bar',stacked=True,legend=True,ax=ax[0],title='Number of cases with Asthma by severity')
    df_age_e.plot(kind='bar',stacked=True,legend=True,ax=ax[1])
    
    fig.tight_layout()
    st.pyplot(fig)
st.write('Also, the amonst the races, Asians have a higher asthma status for all the age groups ')
fig=plt.figure()
t=df.groupby(['AGE_START_YEARS','RACE'])['ASTHMA_START'].min()
t=t.reset_index()
sns.lineplot(x='AGE_START_YEARS',y='ASTHMA_START',hue='RACE',data=t[t.RACE !='Other'])
plt.ylabel('Asthma status')
plt.xlabel('Age')
st.pyplot(fig)

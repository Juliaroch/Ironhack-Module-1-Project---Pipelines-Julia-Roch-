#Wrangling.py
import pandas as pd
import numpy as np
import sqlalchemy

def wrangle(engine):
    business = pd.read_sql_table('business_info', engine)
    rank = pd.read_sql_table('rank_info', engine)
    personal = pd.read_sql_table('personal_info', engine)
    business.drop('realTimeWorth', axis=1, inplace=True)
    df_outer = pd.merge(personal, business, on='id', how='outer')
    df_merged = pd.merge(df_outer, rank, on='id', how='outer')
    df_merged.replace({'gender': 'Male'}, 'M', inplace=True)
    df_merged.replace({'gender': 'Female'}, 'F', inplace=True)
    df_merged['country']=df_merged['country'].str.replace('''People's Republic of China''', 'China')
    df_merged['country']=df_merged['country'].str.replace('USA', 'United States')
    df_merged['country']=df_merged['country'].str.replace('UK', 'United Kingdom')
    df_merged['country']=df_merged['country'].str.replace('UAE', 'United Arab Emirates')
    df_merged['country']=df_merged['country'].str.replace('Hong Kong', 'China')
    df_merged.rename(columns={'worth':'worth (in BUSD)','worthChange':'worthChange (in millions USD)'}, inplace=True)
    df_merged['worth (in BUSD)']=df_merged['worth (in BUSD)'].str.replace(r'\s+BUSD', '')
    df_merged['worthChange (in millions USD)']=df_merged['worthChange (in millions USD)'].str.replace(r'\s+millions USD', '')
    df_merged['worth (in BUSD)'] = df_merged['worth (in BUSD)'].astype(float)
    df_merged['worthChange (in millions USD)'] = df_merged['worthChange (in millions USD)'].astype(float)
    df_merged.drop('Unnamed: 0_y', axis=1, inplace=True)
    df_merged.rename(columns={'age':'age (years old)'}, inplace=True)
    df_merged['age (years old)']=df_merged['age (years old)'].str.replace(r'\s+years old', '')
    df_merged['age (years old)'] = df_merged['age (years old)'].astype(float)
    df_merged.drop_duplicates()
    df_merged = df_merged.groupby(['country']).agg({'name': ['count']}).reset_index()
    df_merged = df_merged.drop(df_merged.index[31])
    df_merged = df_merged.reset_index(drop=True)
    processed_data = df_merged.to_csv('/Users/Julia/labs/Ironhack-Module-1-Project---Pipelines-Julia-Roch-/data/processed/processed_data.csv', index=False)
    return processed_data

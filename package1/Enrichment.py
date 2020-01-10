#Enrichment.py
import pandas as pd
import numpy as np

def enrich(url):
    url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
    df_ws = pd.read_html(url)
    df_world_population = df_ws[0]
    df_world_population.rename(columns={'Country(or dependent territory)':'Country'}, inplace=True)
    df_world_population['Country']=df_world_population['Country'].str.replace(r'\[.*?\]', '')
    df_world_population['Country']=df_world_population['Country'].str.replace(r'\([^()]*\)', '')
    df_world_population['Country']=df_world_population['Country'].str.replace('''People's Republic of China''', 'China')
    df_world_population['Country']=df_world_population['Country'].str.replace('USA', 'United States')
    df_world_population['Country']=df_world_population['Country'].str.replace('UK', 'United Kingdom')
    df_world_population['Country']=df_world_population['Country'].str.replace('UAE', 'United Arab Emirates')
    df_world_population['Country']=df_world_population['Country'].str.replace('Hong Kong', 'China')
    df_world_population['new_column'] = df_world_population.apply(lambda row: (row.Population)/(7760127000), axis=1)
    decimals = 6  
    df_world_population['new_column'] = df_world_population['new_column'].apply(lambda x: round(x, decimals))
    df_world_population.drop('% of World Population', axis=1, inplace=True)
    df_world_population.rename(columns={'new_column':'% of World Population'}, inplace=True)
    df_world_population.rename(columns={'Country':'country'}, inplace=True)
    processed_data_ws = df_world_population.to_csv('/Users/Julia/labs/Ironhack-Module-1-Project---Pipelines-Julia-Roch-/data/processed/processed_data_ws.csv', index=False)
    df_forbes = pd.read_csv('/Users/Julia/labs/Ironhack-Module-1-Project---Pipelines-Julia-Roch-/data/processed/processed_data.csv')
    df_wikipedia = pd.read_csv('/Users/Julia/labs/Ironhack-Module-1-Project---Pipelines-Julia-Roch-/data/processed/processed_data_ws.csv')
    df_complete = pd.merge(df_forbes, df_wikipedia, on='country', how='outer')
    df_complete.rename(columns={'name':'number of billionaires'}, inplace=True)
    df_complete = df_complete.drop(df_complete.index[0])
    df_complete = df_complete.reset_index(drop=True)
    df_complete['number of billionaires'] = df_complete['number of billionaires'].astype(float)
    df_complete=df_complete[df_complete['number of billionaires'].notnull()]
    df_complete['% of World Population'].fillna(0, inplace=True)
    return df_complete
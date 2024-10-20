import streamlit as st
import pandas as pd
import preprocessor, helper

df = pd.read_csv('athlete_events1.csv')
region_df = pd.read_csv('noc_regions1.csv')

df = preprocessor.preprocess(region_df, df)

user_manu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-Wise Analysis', 'Athlete Wise Analysis')
)

st.dataframe(df)

if user_manu == 'Medal Tally':
    medal_telly = helper.medal_telly(df)
    st.dataframe(medal_telly)
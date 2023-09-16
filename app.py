import pickle
import streamlit as st
import requests
import csv
import pandas as pd

import openai

page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://getwallpapers.com/wallpaper/full/7/7/4/1520334-cool-medical-wallpaper-backgrounds-1994x1100-desktop.jpg");
  background-size: cover;
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)


# st.title('Drug Prescription System')
st.title('💉 Drug Prescription System 💊')

# read csv
df = pd.read_csv('drug_final.csv')
condition_list = df['condition']
unique_conditions =list(set(condition_list.tolist()))

condition = st.text_area("Enter the illness condition").lower()
if st.button('Predict'):

    # 1. preprocess
    if condition in unique_conditions:
        condition1 = df[['drugName', 'avg_score']].loc[df['condition'] == condition]
        top_scores = condition1.sort_values(['avg_score'], ascending=[False])
        final = top_scores['drugName'].head(5)
        st.subheader('Top 5 drugs for given condition are:', divider='rainbow')
        st.header(final.values.tolist())
    else:
        st.header("Please enter a valid illness condition")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Button with hyperlink


url = 'https://github.com/nihar-max/drug_prescription_using_reviews'

st.markdown(f'''
<a href={url}><button style="background-color:whiteblack;">Github link</button></a>
''',
unsafe_allow_html=True)


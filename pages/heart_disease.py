import pandas as pd
import requests
import plotly.express as px
import streamlit as st
from streamlit_card import card

from st_pages import Page, Section, show_pages, add_page_title

st.set_page_config(page_title="Welcome", layout="wide")

with open("./pages/welcome.css") as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

head1,head2 = st.columns([.3,.7])
with head1:
    st.image("./img/head_pic.jpg")

with head2:
    st.header("Allan Khariton - Data Science & Analytics Portfolio")
    st.write("I'm a Data Analyst II, and advancing in my career as a data professional. My portfolio focuses on interesting projects I've recently undertaken, with a strong emphasis on business impact and learning new tools & languages. You can view my projects in the posts below, and visit my Github & LinkedIn pages (or download my Resume) by using the links below.")
# Specify what pages should be shown in the sidebar, and what their titles and icons

st.write("##")
space1,link1,link2,link3,link4 = st.columns([.3,.17,.17,.17,.17])
with link1:
    st.write("Rockville, MD")
with link2:
    # st.image("./img/github.svg")
    url2 = "https://github.com/akstl1"
    st.write("[Github](%s)" % url2)

with link3:
    url3 = "https://www.linkedin.com/in/allan-khariton/"
    
    # st.write("[![Title](<https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg>)](<https://www.linkedin.com/in/allan-khariton/>)" "[LinkedIn](%s)" % url3)
    # st.write("[![Title](<./img/github.svg>)](<https://www.linkedin.com/in/allan-khariton/>)" "[LinkedIn](%s)" % url3)
    st.write("[LinkedIn](%s)" % url3)

with link4:
    url4 = "https://akstl1.github.io/docs/A_Khariton_Resume_2022.08.22.pdf"
    
    st.write( "[Resume](%s)" % url4)
    
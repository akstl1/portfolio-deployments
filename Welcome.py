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
    st.write("I'm a Data Analyst II at Edward Jones and specialize in leveraging SQL and Power Platform products to transform existing processes, create efficient new solutions, and shape our analytics strategy. Additionally I am a firm Power BI Champion and spend time mentoring associates, hosting office hours, and shaping our firm standards and BI Community of Practice.")
    st.write("My portfolio focuses on interesting projects I've recently undertaken, with a strong emphasis on business impact and learning new tools & languages. You can view my projects in the posts below, and visit my Github & LinkedIn pages (or download my Resume) by using the links below.")
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
    
    # st.markdown("[![Title](<https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg>)](<https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg>)")
# st.image("./img/github.svg")
# st.markdown('<i class="material-icons">face</i>', unsafe_allow_html=True)
# st.markdown('<img src="./img/head_pic.jpg" alt="Girl in a jacket" width="500" height="600">', unsafe_allow_html=True)


tab1, tab2, tab3, tab4 = st.tabs(["Python - Data Science", "Python - Data Analytics","Power BI", "Tableau"])
with tab1:
   tab11,tab12 = st.columns([.3,.3])
   with tab11:
    st.image("./img/head_pic.jpg")
    st.subheader("Heart Disease Classification")

    
    with tab12:
       st.image("./img/head_pic.jpg")
       st.subheader("Parkinson's Verification")
    #  hasClicked = card(
    #     title="Project Coming Soon!",
    #     text="Some description",
    #     image="http://placekitten.com/200/300",
    #     url="https://github.com/gamcoh/st-card"
    #     )
    
    # with tab13:
    #  st.image("./img/head_pic.jpg")
    #  hasClicked = card(
    #     title="Another Project!",
    #     text="Some description",
    #     image="http://placekitten.com/200/300",
    #     url="https://github.com/gamcoh/st-card"
    #     )

#    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("Test")
   
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("Test")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

show_pages(
    [
        Page("Welcome.py", "Home", "🏠"),
        Section("Additional Projects", icon="🎈️"),
        Page("pages/analyducks.py", "Analyducks"),
        Page("pages/pokedex.py", "Pokedex"),
        Page("pages/power_bi_aggregation.py", "BI Aggregation")
        # # Pages after a section will be indented
        # Page("Another page", icon="💪"),
        # # Unless you explicitly say in_section=False
        # Page("Not in a section", in_section=False)
    ]
  )


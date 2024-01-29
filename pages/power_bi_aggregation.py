# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt
from datetime import date
import numpy as np

st.set_page_config(page_title="BI Aggregation", layout="wide")


with open("./pages/bi_agg.css") as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title("Power BI Data Aggregation Query Builder")
st.header("Purpose of this project:")
st.write("For some of my BI queries, I have to create a custom grouping measure to combine data by one field while taking in the first or last input in each column with that matching grouping field. To make this custom grouping call easier I created this site, where I can upload all the column names and information in the applicable dataset and the custom function is generated thereafter. I can then copy paste this output into Power Query quickly to get my desired result.")
st.header("Instructions for BI Query Fields")
st.write("In the below please enter:")
st.write("1. the name of the previous step in Power Query Applied Steps")
st.write("2. Enter whether you would like to record the first or last recorded input for each column")
st.write("3. Enter whether you would like each newly created column name to include an index")
st.header("BI Query Input Fields")
# adding user input fields to input table name, grouping fields, first and last preferene, and index preference

col1,col2 = st.columns([.4,.6])
with col1:
    prev_table = st.text_input("Enter Previous Step Name:","Pivoted Table")

    group_by_table = st.text_input("Enter Variable To Group By:","ProjectID")
    first_last = st.selectbox(
        'Enter whether to keep First or Last value inputs:',
        ('First','Last'))


    name_index = st.selectbox(
        'Enter whether to add an Index to re-named field:',
        ('Yes','No'))

# initiating string var needed to compile the final result
column_list_string_query = ''

# inserting instructions and headers, 
st.header("Instructions for file upload")
st.write("To use this aggregation tool please: upload a csv/xlsx file, with the input fields in one column, and a header as the top cell of the column.")

# inserting uploaded file component to insert a file
uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False,type=['xlsx','xls','csv'])

# adding in logic to parse data, and compile into final string format
if uploaded_file is not None:
    file_type = uploaded_file.name
    if "xlsx" in file_type or "xls" in file_type:
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)
    
    # make a df in dict format to access data, and find the relevant col name to search through
    df2=df.to_dict()
    # column_name = list(df.columns.values)[0]
    column_name = list(df2.keys())[0]
    #for loop to go through each row of the data, transform it to be in the right format for the query, and append to the query string
    for row in range(len(df)):
        if row>=0:
            if name_index=='Yes':
                datum = df2[column_name][row]
                column_list_string_query+='{"'+str(row+1)+'_'+datum+'", each List.'+first_last+'(List.RemoveNulls(['+datum+']))},'
            else:
                datum = df2[column_name][row]
                column_list_string_query+='{"'+datum+'", each List.'+first_last+'(List.RemoveNulls(['+datum+']))},'



# initiate first part of query string var
first_part_of_query = '=Table.Group(#\"'+prev_table+'", {"'+group_by_table+'"},{'

# insert final query header and final query text
st.header("Final Query Output")

st.write(first_part_of_query+column_list_string_query[:-1]+'})')
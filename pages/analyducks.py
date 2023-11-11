# Improt libraries
import streamlit as st
import pandas as pd
import plotly.express as px

import datetime as dt
from datetime import date

import numpy as np
# import dash_bootstrap_components as dbc


# from streamlit_card import card

## read in excel dataset
df = pd.read_excel("./data/duck_data.xlsx", sheet_name="Ducks")

## convert date bought col to date, and extract year into a column
df['Date_Bought'] = pd.to_datetime(df['Date_Bought'],format='%m/%d/%Y').dt.date
# df['Year'] = pd.to_datetime(df['Date_Bought'],format='%Y')
df['Year'] = pd.DatetimeIndex(df['Date_Bought']).year
df = df.sort_values(by=['Date_Bought'], ascending=True)

## find avg weight measure, needed for rows where more than 1 duck is included in the total weight
df['Avg_Weight'] = np.round(df.Total_Weight/df.Quantity,2)
df["About Me"].fillna("Nothing yet")
## transform and create new dfs to find ducks bought by state, country, purchase method, buyer, year, weight, and cumulative weight
state_df = df.groupby(["Purchase_State"]).agg({"Quantity":"sum"}).reset_index()
state_df = state_df[state_df["Purchase_State"]!=""]

county_df = df.groupby(["ISO_Code","Purchase_Country"]).agg({"Quantity":"sum"}).reset_index()

purchase_method_df = df.groupby(["Purchase_Method"]).agg({"Quantity":"sum"}).reset_index()

buyer_df = df.groupby(["Buyer"]).agg({"Quantity":"sum"}).reset_index()
buyer_df = buyer_df.sort_values(by=['Quantity'],ascending=True)
yearly_df = df.groupby(["Year"]).agg({"Quantity":"sum"}).reset_index()

weight_df = df.groupby(["Year"]).agg({"Total_Weight":"sum"}).reset_index()

weight_cum_df = df.groupby(['Year']).sum().cumsum().reset_index()

## insert a title for the app and instructions
st.set_page_config(page_title="Analyducks", layout="wide")
st.markdown("<h1 style='text-align: center;'>Analyducks</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>A visual analysis of Allan K's rubber duck collection</h1>", unsafe_allow_html=True)
st.markdown(
    """<a style='display: block; text-align: center;' href="https://akstl1.github.io/">Click here to view my portfolio</a>
    """,
    unsafe_allow_html=True,
)

# st.markdown(
#     """
#     <style>
    
#     .st-emotion-cache-ocqkz7 {
#         background-color: #000000;
#         }
#     </style>
#     """, 
#     unsafe_allow_html=True
    
#     )
# <div data-testid="column" class="st-emotion-cache-j5r0tf e1f1d6gn2"><div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="157.7624969482422" data-testid="stVerticalBlock" class="st-emotion-cache-9xwmxx e1f1d6gn1"><div data-stale="false" width="157.7624969482422" class="element-container st-emotion-cache-az4wv8 e1f1d6gn3" data-testid="element-container"><div data-testid="stMetric"><label data-testid="stMetricLabel" visibility="0" class="st-emotion-cache-1tenn4l e1i5pmia2"><div class="st-emotion-cache-1wivap2 e1i5pmia3"><div data-testid="stMarkdownContainer" class="st-emotion-cache-xujc5b e1nzilvr5"><p>Total Ducks Owned</p></div></div></label><div data-testid="stMetricValue" class="st-emotion-cache-1xarl3l e1i5pmia1"><div class="st-emotion-cache-1wivap2 e1i5pmia3"> 133 </div></div></div></div></div></div></div>
# <div data-testid="stHorizontalBlock" class="st-emotion-cache-ocqkz7 e1f1d6gn4"><div data-testid="column" class="st-emotion-cache-j5r0tf e1f1d6gn2"><div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="157.7624969482422" data-testid="stVerticalBlock" class="st-emotion-cache-9xwmxx e1f1d6gn1"><div data-stale="false" width="157.7624969482422" class="element-container st-emotion-cache-az4wv8 e1f1d6gn3" data-testid="element-container"><div data-testid="stMetric"><label data-testid="stMetricLabel" visibility="0" class="st-emotion-cache-1tenn4l e1i5pmia2"><div class="st-emotion-cache-1wivap2 e1i5pmia3"><div data-testid="stMarkdownContainer" class="st-emotion-cache-xujc5b e1nzilvr5"><p>Total Ducks Owned</p></div></div></label><div data-testid="stMetricValue" class="st-emotion-cache-1xarl3l e1i5pmia1"><div class="st-emotion-cache-1wivap2 e1i5pmia3"> 133 </div></div></div></div></div></div></div><div data-testid="column" class="st-emotion-cache-j5r0tf e1f1d6gn2"><div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="157.7624969482422" data-testid="stVerticalBlock" class="st-emotion-cache-9xwmxx e1f1d6gn1"><div data-stale="false" width="157.7624969482422" class="element-container st-emotion-cache-az4wv8 e1f1d6gn3" data-testid="element-container"><div data-testid="stMetric"><label data-testid="stMetricLabel" visibility="0" class="st-emotion-cache-1tenn4l e1i5pmia2"><div class="st-emotion-cache-1wivap2 e1i5pmia3"><div data-testid="stMarkdownContainer" class="st-emotion-cache-xujc5b e1nzilvr5"><p>Ducks Bought Within Last Year</p></div></div></label><div data-testid="stMetricValue" class="st-emotion-cache-1xarl3l e1i5pmia1"><div class="st-emotion-cache-1wivap2 e1i5pmia3"> 78 </div></div></div></div></div></div></div><div data-testid="column" class="st-emotion-cache-j5r0tf e1f1d6gn2"><div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="157.7624969482422" data-testid="stVerticalBlock" class="st-emotion-cache-9xwmxx e1f1d6gn1"><div data-stale="false" width="157.7624969482422" class="element-container st-emotion-cache-az4wv8 e1f1d6gn3" data-testid="element-container"><div data-testid="stMetric"><label data-testid="stMetricLabel" visibility="0" class="st-emotion-cache-1tenn4l e1i5pmia2"><div class="st-emotion-cache-1wivap2 e1i5pmia3"><div data-testid="stMarkdownContainer" class="st-emotion-cache-xujc5b e1nzilvr5"><p>Duck Collection Weight (g)</p></div></div></label><div data-testid="stMetricValue" class="st-emotion-cache-1xarl3l e1i5pmia1"><div class="st-emotion-cache-1wivap2 e1i5pmia3"> 5209.2 </div></div></div></div></div></div></div><div data-testid="column" class="st-emotion-cache-j5r0tf e1f1d6gn2"><div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="157.7624969482422" data-testid="stVerticalBlock" class="st-emotion-cache-9xwmxx e1f1d6gn1"><div data-stale="false" width="157.7624969482422" class="element-container st-emotion-cache-az4wv8 e1f1d6gn3" data-testid="element-container"><div data-testid="stMetric"><label data-testid="stMetricLabel" visibility="0" class="st-emotion-cache-1tenn4l e1i5pmia2"><div class="st-emotion-cache-1wivap2 e1i5pmia3"><div data-testid="stMarkdownContainer" class="st-emotion-cache-xujc5b e1nzilvr5"><p>Unique Countries of Purchase</p></div></div></label><div data-testid="stMetricValue" class="st-emotion-cache-1xarl3l e1i5pmia1"><div class="st-emotion-cache-1wivap2 e1i5pmia3"> 8 </div></div></div></div></div></div></div><div data-testid="column" class="st-emotion-cache-j5r0tf e1f1d6gn2"><div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="157.7624969482422" data-testid="stVerticalBlock" class="st-emotion-cache-9xwmxx e1f1d6gn1"><div data-stale="false" width="157.7624969482422" class="element-container st-emotion-cache-az4wv8 e1f1d6gn3" data-testid="element-container"><div data-testid="stMetric"><label data-testid="stMetricLabel" visibility="0" class="st-emotion-cache-1tenn4l e1i5pmia2"><div class="st-emotion-cache-1wivap2 e1i5pmia3"><div data-testid="stMarkdownContainer" class="st-emotion-cache-xujc5b e1nzilvr5"><p>Unique Cities of Purchase</p></div></div></label><div data-testid="stMetricValue" class="st-emotion-cache-1xarl3l e1i5pmia1"><div class="st-emotion-cache-1wivap2 e1i5pmia3"> 40 </div></div></div></div></div></div></div></div>
# <div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="852.7999877929688" data-testid="stVerticalBlock" class="st-emotion-cache-pplk8x e1f1d6gn1"><div data-testid="stHorizontalBlock" class="st-emotion-cache-ocqkz7 e1f1d6gn4"><div data-testid="column" class="st-emotion-cache-j5r0tf e1f1d6gn2"><div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="157.7624969482422" data-testid="stVerticalBlock" class="st-emotion-cache-9xwmxx e1f1d6gn1"><div data-stale="false" width="157.7624969482422" class="element-container st-emotion-cache-az4wv8 e1f1d6gn3" data-testid="element-container"><div data-testid="stMetric"><label data-testid="stMetricLabel" visibility="0" class="st-emotion-cache-1tenn4l e1i5pmia2"><div class="st-emotion-cache-1wivap2 e1i5pmia3"><div data-testid="stMarkdownContainer" class="st-emotion-cache-xujc5b e1nzilvr5"><p>Total Ducks Owned</p></div></div></label><div data-testid="stMetricValue" class="st-emotion-cache-1xarl3l e1i5pmia1"><div class="st-emotion-cache-1wivap2 e1i5pmia3"> 133 </div></div></div></div></div></div></div><div data-testid="column" class="st-emotion-cache-j5r0tf e1f1d6gn2"><div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="157.7624969482422" data-testid="stVerticalBlock" class="st-emotion-cache-9xwmxx e1f1d6gn1"><div data-stale="false" width="157.7624969482422" class="element-container st-emotion-cache-az4wv8 e1f1d6gn3" data-testid="element-container"><div data-testid="stMetric"><label data-testid="stMetricLabel" visibility="0" class="st-emotion-cache-1tenn4l e1i5pmia2"><div class="st-emotion-cache-1wivap2 e1i5pmia3"><div data-testid="stMarkdownContainer" class="st-emotion-cache-xujc5b e1nzilvr5"><p>Ducks Bought Within Last Year</p></div></div></label><div data-testid="stMetricValue" class="st-emotion-cache-1xarl3l e1i5pmia1"><div class="st-emotion-cache-1wivap2 e1i5pmia3"> 78 </div></div></div></div></div></div></div><div data-testid="column" class="st-emotion-cache-j5r0tf e1f1d6gn2"><div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="157.7624969482422" data-testid="stVerticalBlock" class="st-emotion-cache-9xwmxx e1f1d6gn1"><div data-stale="false" width="157.7624969482422" class="element-container st-emotion-cache-az4wv8 e1f1d6gn3" data-testid="element-container"><div data-testid="stMetric"><label data-testid="stMetricLabel" visibility="0" class="st-emotion-cache-1tenn4l e1i5pmia2"><div class="st-emotion-cache-1wivap2 e1i5pmia3"><div data-testid="stMarkdownContainer" class="st-emotion-cache-xujc5b e1nzilvr5"><p>Duck Collection Weight (g)</p></div></div></label><div data-testid="stMetricValue" class="st-emotion-cache-1xarl3l e1i5pmia1"><div class="st-emotion-cache-1wivap2 e1i5pmia3"> 5209.2 </div></div></div></div></div></div></div><div data-testid="column" class="st-emotion-cache-j5r0tf e1f1d6gn2"><div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="157.7624969482422" data-testid="stVerticalBlock" class="st-emotion-cache-9xwmxx e1f1d6gn1"><div data-stale="false" width="157.7624969482422" class="element-container st-emotion-cache-az4wv8 e1f1d6gn3" data-testid="element-container"><div data-testid="stMetric"><label data-testid="stMetricLabel" visibility="0" class="st-emotion-cache-1tenn4l e1i5pmia2"><div class="st-emotion-cache-1wivap2 e1i5pmia3"><div data-testid="stMarkdownContainer" class="st-emotion-cache-xujc5b e1nzilvr5"><p>Unique Countries of Purchase</p></div></div></label><div data-testid="stMetricValue" class="st-emotion-cache-1xarl3l e1i5pmia1"><div class="st-emotion-cache-1wivap2 e1i5pmia3"> 8 </div></div></div></div></div></div></div><div data-testid="column" class="st-emotion-cache-j5r0tf e1f1d6gn2"><div class="st-emotion-cache-1wmy9hl e1f1d6gn0"><div width="157.7624969482422" data-testid="stVerticalBlock" class="st-emotion-cache-9xwmxx e1f1d6gn1"><div data-stale="false" width="157.7624969482422" class="element-container st-emotion-cache-az4wv8 e1f1d6gn3" data-testid="element-container"><div data-testid="stMetric"><label data-testid="stMetricLabel" visibility="0" class="st-emotion-cache-1tenn4l e1i5pmia2"><div class="st-emotion-cache-1wivap2 e1i5pmia3"><div data-testid="stMarkdownContainer" class="st-emotion-cache-xujc5b e1nzilvr5"><p>Unique Cities of Purchase</p></div></div></label><div data-testid="stMetricValue" class="st-emotion-cache-1xarl3l e1i5pmia1"><div class="st-emotion-cache-1wivap2 e1i5pmia3"> 40 </div></div></div></div></div></div></div></div></div></div>
###################### KPI Calcs ##############################

# weight KPI
duck_weight = df["Total_Weight"].sum()

# total ducks bought KPI
total_ducks = df["Quantity"].sum()

# unique purchase countries KPI
unique_countries = df.Purchase_Country.nunique()

# unique purchase cities KPI
unique_cities = df.Purchase_City.nunique()

# ducks bought within last year KPI
today = date.today()
today_yr = today.year
today_day = today.day
today_month = today.month
ducks_bought_last_year = df[df["Date_Bought"]>=dt.date(today_yr-1,today_month,today_day)].Quantity.sum()

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Ducks Owned",total_ducks)
    col2.metric("Ducks Bought Within Last Year",ducks_bought_last_year)
    col3.metric("Duck Collection Weight (g)",duck_weight)
    col4.metric("Unique Countries of Purchase",unique_countries)
    col5.metric("Unique Cities of Purchase",unique_cities)

# css='''
# [data-testid="stMetric"] {
#     color: #212529;
#     background-color: #f8f9fa;
#     width: 75%;
#     margin: auto;
#     padding: 1rem 1rem;
#     border-radius: 0.25rem
# }

# [data-testid="stMetric"] > div {
#     color: #212529;
#     background-color: #f8f9fa;
#     width: fit-content;
#     margin: auto;
# }


# [data-testid="stMetric"] label {
#     color: #212529;
#     background-color: #f8f9fa;
#     width: fit-content;
#     margin: auto;
# }
# '''

# st.markdown(f'<style>{css}</style>',unsafe_allow_html=True)
# st.markdown('''
# <style>
# /*center metric label*/
# [data-testid="stMetricLabel"] > div:nth-child(1) {
#     justify-content: center;
# }

# /*center metric value*/
# [data-testid="stMetricValue"] > div:nth-child(1) {
#     justify-content: center;
# }
# </style>
# ''', unsafe_allow_html=True)

###################### General Data graphs ##############################




## pie chart showing purchase method of ducks

purchase_fig = px.pie(purchase_method_df, values='Quantity', names='Purchase_Method')
purchase_fig.update_layout(title_text="Purchase Method Distribution",
                           title_x=0.2,
                           paper_bgcolor="rgb(235,204,52)",
                           plot_bgcolor="rgb(206,212,218)",
                           font=dict(color="black")
                           )


owner_bar = px.bar(buyer_df,x="Buyer", y="Quantity")
owner_bar.update_layout(title_text="Rubber Duck Distribution by Purchaser", 
                        title_x=0.2,
                        xaxis_title="Purchaser", 
                        yaxis_title="Quantity",
                        paper_bgcolor="rgb(235,204,52)",
                        plot_bgcolor="rgb(206,212,218)",
                        font=dict(color="black")
                        )

## 3d scatter of length, height, width

three_d_fig = px.scatter_3d(df, x='Length', 
                            y='Width', 
                            z="Height",
                            size='Avg_Weight',
                            color='Avg_Weight',
                            labels={'Avg_Weight':'Avg. Weight'}
                            )

three_d_fig.update_layout(title_text="Rubber Duck Length vs Width vs Height (cm)",
                          title_x=0.2,
                          paper_bgcolor="rgb(235,204,52)",
                          plot_bgcolor="rgb(255,0,0)",
                          font=dict(color="black")
                          )
camera = dict(
    eye=dict(x=0, y=2, z=1),
    # up=dict(x=1, y=1, z=0),
)

three_d_fig.update_layout(scene_camera=camera)

gen1,gen2,gen3 = st.columns(3)
gen1.plotly_chart(purchase_fig, use_container_width=True,theme=None)
gen2.plotly_chart(owner_bar, use_container_width=True,theme=None)
gen3.plotly_chart(three_d_fig, use_container_width=True,theme=None)

###################### Purchase and weight graphs ##############################

## bar plot showing number of ducks bought per year 

year_bar = px.bar(yearly_df,x="Year", y="Quantity")
year_bar.update_layout(title_text="Rubber Ducks Bought Per Year", 
                       title_x=0.3,
                       xaxis_title="Purchase Year",
                       yaxis_title="Quantity",
                       paper_bgcolor="rgba(0,0,0,0)"
                       )


## bar plot showing number of ducks bought per year, cumulative

year_bar_cumulative = px.line(weight_cum_df,x="Year", y="Quantity")
year_bar_cumulative.update_layout(title_text="Total Rubber Ducks Owned",
                                  title_x=0.3,
                                  xaxis_title="Purchase Year", 
                                  yaxis_title="Quantity",
                                  paper_bgcolor="rgba(0,0,0,0)"
                                  )

## bar plot showing weight of ducks bought each year

weight_bar = px.bar(weight_df,x="Year", y="Total_Weight")
weight_bar.update_layout(title_text="Weight (g) of Annual Purchases",
                         title_x=0.3,
                         xaxis_title="Purchase Year",
                         yaxis_title="Weight (g)",
                         paper_bgcolor="rgba(0,0,0,0)"
                         )


## bar plot showing weight of ducks bought each year, cumulative

weight_bar_cumulative = px.line(weight_cum_df,x="Year", y="Total_Weight")
weight_bar_cumulative.update_layout(title_text="Cumulative Collection Weight (g)",
                                    title_x=0.3,
                                    xaxis_title="Purchase Year", 
                                    yaxis_title="Cumulative Weight (g)",
                                    paper_bgcolor="rgba(0,0,0,0)"
                                    )

purchase1,purchase2 = st.columns(2)
purchase1.plotly_chart(year_bar, use_container_width=True,theme=None)
purchase2.plotly_chart(year_bar_cumulative, use_container_width=True,theme=None)

weight1,weight2 = st.columns(2)
weight1.plotly_chart(weight_bar, use_container_width=True,theme=None)
weight2.plotly_chart(weight_bar_cumulative, use_container_width=True,theme=None)


###################### Mapping graphs ##############################

map_fig = px.scatter_geo(df,
        lon = 'Longitude',
        lat = 'Latitude',
        hover_name="Name"      
        )

map_fig.update_traces(marker=dict(color="Red"))

## choropleth showing duck purchase by country

country_fig = px.choropleth(county_df, locations="ISO_Code",
                    color="Quantity", 
                    hover_name="Purchase_Country"
                    # color_continuous_scale="YlGn"
                    )
country_fig.add_trace(map_fig.data[0])

country_fig.update_geos(
    visible=True, resolution=50, scope="world", showcountries=True, countrycolor="Black"
)
country_fig.update_geos(projection_type="natural earth")
country_fig.update_layout(title_text="Rubber Duck Purchase By Country",title_x=0.3,width=1000)

## choropleth showing duck purchase by US state

state_fig = px.choropleth(state_df,locations="Purchase_State", 
                          locationmode="USA-states", 
                          color="Quantity", 
                          scope="usa"
                        #   color_continuous_scale="YlGn"
                          )
state_fig.update_layout(title_text="Rubber Duck Purchase By State",title_x=0.3)
state_fig.add_trace(map_fig.data[0])


map1,map2 = st.columns(2)
map1.plotly_chart(country_fig, use_container_width=True,theme=None)
map2.plotly_chart(state_fig, use_container_width=True,theme=None)

###################### Duck info graphs ##############################


st.write(df[["Name","Purchase_City","Date_Bought","About Me"]])

duck = st.selectbox("Select Duck to get more info: ",df.Name)

index = df[df['Name'] == duck].index[0]

duck1,duck2 = st.columns(2)
with duck1:
    st.image("./img/DuckFamily.jpg")
    
with duck2:
    st.write("About Me: "+df.iloc[index][11])
    st.write("Purchase Method: "+df.iloc[index][2])
    st.write("Purchase Retailer: "+df.iloc[index][3])
    if df.iloc[index][6]=="USA":
        st.write("Purchase Details: Bought by "+df.iloc[index][12]+" on "+str(df.iloc[index][8])+" in "+df.iloc[index][4]+", "+df.iloc[index][5]+", "+df.iloc[index][6])
    else:
        st.write("Purchase Details: Bought by "+df.iloc[index][12]+" on "+str(df.iloc[index][8])+" in "+df.iloc[index][4]+", "+df.iloc[index][6])
    st.write("Quantity: "+str(df.iloc[index][13]))
    st.write("Weight: "+str(df.iloc[index][14]))
    st.write("Dimensions (L x W x H): "+str(df.iloc[index][17])+" cm x "+str(df.iloc[index][16])+" cm x "+str(df.iloc[index][15])+" cm")
    

# img_nm = "DuckFamily.jpg"    
# names = [i for i in df['Name']]   
# desc = [i for i in df['About Me']]     
# ducks = len(df['Quantity'])
# n_cols=5
# n_rows=int(1+ducks//n_cols)
# rows = [st.columns(n_cols,gap="small") for _ in range(n_rows)]
# cols = [column for row in rows for column in row]
# st.write(n_rows)
# for col,i,d in zip(cols,names,desc):
#     col.image("./img/DuckFamily.jpg")
#     col.subheader(i)
#     col.write(d)
    # with col:
    #     res=card(
    #         title=i,
    #         text=d,
    #         image="https://placekitten.com/500/500",
    #         on_click=lambda: print("Clicked!"),
    #         styles={
    #             "card": {
    #                 "width": "100%",
    #                 "height": "200px",
    #                 "border-radius": "2px",
    #                 "padding": "5px",
    #                 "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
    #             },
    #             "text": {
    #                 "font-family": "serif"
    #             },
    #             "title": {
    #                 "font-size":"10px"
    #                 }
    #         }
    #     )
    
css='''
[data-testid="stMetric"] {
    color: #212529;
    background-color: #f8f9fa;
    width: 75%;
    margin: auto;
    padding: 1rem 1rem;
    border-radius: 0.25rem
}

[data-testid="stDataFrameResizable"] {
    align-content: center;
    align-items: center;
    width: 75%;
    margin: auto;
    padding: 1rem 1rem;
    border-radius: 0.25rem
}

[data-testid="stMetric"] > div {
    color: #212529;
    background-color: #f8f9fa;
    width: fit-content;
    margin: auto;
}


[data-testid="stMetric"] label {
    color: #212529;
    background-color: #f8f9fa;
    width: fit-content;
    margin: auto;
}

[data-testid="stVerticalBlock"] > [".st-emotion-cache-pplk8x e1f1d6gn1"] {
    border: 20px groove red;
}


# [data-testid="block-container"] {
#     color: #000000;
#     background-color: #f8f9fa;
#     width: fit-content;
#     margin: auto;
# }

# [data-testid="stMarkdownContainer"] > div > h1 {
#     color: #000000;
#     # background-color: #f8f9fa;
#     width: fit-content;
#     margin: auto;
# }

# [data-testid="stHorizontalBlock"] > div {
#     color: #000000;
#     background-color: #f8f9fa;
#     width: fit-content;
#     margin: auto;
# }



# [data-testid="element-container"] > div  {
#     # color: #EBCC34;
#     background-color: #EBCC34;
#     # width: fit-content;
#     # margin: auto;
# }    

# [data-testid="stMetric"] {
#     color: #212529;
#     background-color: #f8f9fa;
#     width: 75%;
#     margin: auto;
#     padding: 1rem 1rem;
#     border-radius: 0.25rem
# }

# [data-testid="stMetric"] > div {
#     color: #212529;
#     background-color: #f8f9fa;
#     width: fit-content;
#     margin: auto;
# }


# [data-testid="stMetric"] label {
#     color: #212529;
#     background-color: #f8f9fa;
#     width: fit-content;
#     margin: auto;
# }
}
'''
st.markdown(f'<style>{css}</style>',unsafe_allow_html=True)




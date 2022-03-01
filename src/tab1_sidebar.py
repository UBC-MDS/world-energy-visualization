from dash import Input, Output, callback, html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

df_all = pd.read_csv("data/Primary-energy-consumption-from-fossilfuels-nuclear-renewables.csv")

df_notna = df_all[df_all['Code'].notna()]
df_countries = df_notna[df_notna['Code']!='OWID_WRL']
df_world = df_notna[df_notna['Code']=='OWID_WRL']
df_continents = df_all[df_all['Code'].isna()]

list_of_continents = df_continents['Entity'].unique()
list_of_countries = df_countries['Entity'].unique()

#==============================================================================
#                            SideBar1
#==============================================================================  

SIDEBAR1_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    #"width": "18rem",
    "padding": "2rem 1rem",
    "background-image": "url(/assets/wind-energy.jpg)"
    # "background-color": "#98FB98",
}


sidebar1 = dbc.Col([
        html.H3("World Energy Visualisation"),
        html.Br(),
        html.H5(
            "Energy type",
            #style={"width": "50%", "display": "inline-block"},
        ),
        
        dbc.Row(
            dcc.Dropdown(
                id="tab1-energy-type-dropdown",
                options=[{"label": energy_type, "value": energy_type} for energy_type in ["Fossil", "Nuclear", "Renewables"]],
                value="Fossil",
            ),
            #width=12,
            style={
                "padding": "10px 10px 10px 0px",
            },
        ),
        html.Br(),
        
        html.H5(
            "Region",
            style={"width": "50%", "display": "inline-block"},
        ),
        
        dbc.Row(
            dcc.Dropdown(
                id="tab1-region-dropdown",
                options=[{"label": region, "value": region} for region in list_of_continents],
                multi=True,
                value=["North America", "Europe"],
            ),
            #width=12,
            style={
                "padding": "10px 10px 10px 0px",
            },
        ),
        html.Br(),
        
        html.H5(
            "Data sources",
            style={"width": "50%", "display": "inline-block"},
        ),
        dbc.Row(
            dcc.Markdown('''
                Datasets for visualization of energy trends were downloaded from [here](https://www.kaggle.com/donjoeml/energy-consumption-and-generation-in-the-globe)
            '''),
        ),
    ],
    md=2,
    style=SIDEBAR1_STYLE,
)

import dash
from dash import Input, Output, callback, html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)



df_all = pd.read_csv("../data/Primary-energy-consumption-from-fossilfuels-nuclear-renewables.csv")
df_notna = df_all[df_all['Code'].notna()]
df_countries = df_notna[df_notna['Code']!='OWID_WRL']
df_world = df_notna[df_notna['Code']=='OWID_WRL']
df_continents = df_all[df_all['Code'].isna()]

list_of_continents = df_continents['Entity'].unique()
list_of_countries = df_countries['Entity'].unique()

#==============================================================================
#                            Layout for map and barchart 
#==============================================================================       
    
tab1_plots = html.Div([
    dcc.Graph(id="tab1-map"),
    dcc.Slider(1950, 
               2022, 
               5,
               value=1980,
               id="tab1-year-slider"
    ),
    html.H4("Top N countries"),
    html.Br(),
    dcc.Graph(id="tab1-barchart"),
    dbc.Row([
        dbc.Col([
            html.H5("Number of countries"),
            html.Br(),
            dbc.Input(id="tab1-input-topN", placeholder="10", type="number"),     
        ]),
        
        dbc.Col([
            html.H5("Ranking type"),
            html.Br(),
            dcc.RadioItems(["Top", "Bottom"], "Top", inline=True)   
        ]),  
    ])
])


#==============================================================================
#                            World Map
#==============================================================================

@callback(
    Output("map", "figure"), 
    Input("tab1-energy-type-dropdown", "energy_type"),
    Input("tab1-year-slider", "year"))
def display_map(energy_type, year):
    """
    Docs
    """
    fig = "Figure of World map"
    
    return fig
    
    
#==============================================================================
#                            Top N countries barchart
#==============================================================================    

@callback(
    Output("tab1-barchart", "figure"), 
    Input("tab1-energy-type-dropdown", "energy_type"),
    Input("tab1-year-slider", "year"))
def display_barchart(energy_type, year):
    """
    Docs
    """
    fig = "Barchart with top 10 countries"
    
    return fig



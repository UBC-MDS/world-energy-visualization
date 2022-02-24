import dash
from dash import Input, Output, callback, html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go


df_all = pd.read_csv("../data/Primary-energy-consumption-from-fossilfuels-nuclear-renewables.csv")

df_notna = df_all[df_all['Code'].notna()]
df_countries = df_notna[df_notna['Code']!='OWID_WRL']
df_world = df_notna[df_notna['Code']=='OWID_WRL']
df_continents = df_all[df_all['Code'].isna()]

list_of_continents = df_continents['Entity'].unique()
list_of_countries = df_countries['Entity'].unique()

#==============================================================================
#                            Lineplots
#==============================================================================

tab2_lineplots = dbc.Col([
        html.H4("Fossil"),
        dcc.Graph(id="tab2-lineplot-fossil"),
        html.Br(),
        
        html.H4("Nuclear"),
        dcc.Graph(id="tab2-lineplot-nuclear"),
        html.Br(),
        
        html.H4("Renewable"),
        dcc.Graph(id="tab2-lineplot-renewable"),
        html.Br(),
        
        dcc.RangeSlider(1950, 2022, 5,
                   value=1980,
                   id="tab2-years-rangeslider"),
        
    ])


@callback(
    Output("tab2-lineplot-fossil", "figure"), 
    Input("tab2-country-dropdown", "countries"), 
    Input("tab2-region-dropdown", "regions"), 
    Input("tab2-world-toggle", "world"), 
    Input("tab2-years-rangeslider", "years"))
def lineplot_fossil(years):
    """
    Docs
    """
    fig = "Lineplot for fossil"

    return fig
    
    
@callback(
    Output("tab2-lineplot-nuclear", "figure"), 
    Input("tab2-country-dropdown", "countries"), 
    Input("tab2-region-dropdown", "regions"), 
    Input("tab2-world-toggle", "world"), 
    Input("tab2-years-rangeslider", "years"))
def lineplot_nuclear(years):
    """
    Docs
    """
    fig = "Lineplot for nuclear"

    return fig
    
    
@callback(
    Output("tab2-lineplot-renewable", "figure"), 
    Input("tab2-country-dropdown", "countries"), 
    Input("tab2-region-dropdown", "regions"), 
    Input("tab2-world-toggle", "world"), 
    Input("tab2-years-rangeslider", "years"))
def lineplot_renewable(years):
    """
    Docs
    """
    fig = "Lineplot for renewable"

    return fig
    
    

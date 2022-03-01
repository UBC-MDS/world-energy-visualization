from dash import Input, Output, callback, html, dcc
import dash_bootstrap_components as dbc

import numpy as np
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
#                 Placeholder for valid plots, remove afterwards
#==============================================================================  
list_yrs = df_all['Year'].unique()

#==============================================================================
#                            Layout for lineplots
#==============================================================================   

tab2_lineplots = dbc.Col([

        dcc.RangeSlider(
            min=list_yrs.min(), 
            max=list_yrs.max(), 
            step=1, 
            value=[list_yrs.min(), list_yrs.max()],
            marks={int(i): str(i) for i in np.append(list_yrs[::5], [list_yrs.max()])},
            tooltip={"placement": "top", "always_visible": False},
            id="tab2-years-rangeslider"),
        html.Br(),

        html.H4("Fossil"),
        dcc.Graph(id="tab2-lineplot-fossil"),
        html.Br(),
        
        html.H4("Nuclear"),
        dcc.Graph(id="tab2-lineplot-nuclear"),
        html.Br(),
        
        html.H4("Renewable"),
        dcc.Graph(id="tab2-lineplot-renewable")
        
    ])


#==============================================================================
#                            Lineplots
#==============================================================================

@callback(
    Output("tab2-lineplot-fossil", "figure"), 
    Input("tab2-country-dropdown", "value"), 
    Input("tab2-region-dropdown", "value"), 
    Input("tab2-world-toggle", "value"), 
    Input("tab2-years-rangeslider", "value"))
def lineplot_fossil(country, region, toggle, years):
    """
    Docs
    """
    df_use = df_all[df_all['Entity'].isin([country] + region + len(toggle) * ["World"])]
    df_use = df_use[(df_use['Year'] >= years[0]) & (df_use["Year"] <= years[1])]
    fig = px.line(df_use, x="Year", y="Fossil fuels (% sub energy)", color="Entity", 
        title=f'Fossil fuels usage from {years[0]} to {years[1]}')
    return fig
    
    
@callback(
    Output("tab2-lineplot-nuclear", "figure"), 
    Input("tab2-country-dropdown", "value"), 
    Input("tab2-region-dropdown", "value"), 
    Input("tab2-world-toggle", "value"), 
    Input("tab2-years-rangeslider", "value"))
def lineplot_nuclear(country, region, toggle, years):
    """
    Docs
    """
    df_use = df_all[df_all['Entity'].isin([country] + region + len(toggle) * ["World"])]
    df_use = df_use[(df_use['Year'] >= years[0]) & (df_use["Year"] <= years[1])]
    fig = px.line(df_use, x="Year", y="Nuclear (% sub energy)", color="Entity", 
        title=f'Nuclear fuel usage from {years[0]} to {years[1]}')

    return fig
    
    
@callback(
    Output("tab2-lineplot-renewable", "figure"), 
    Input("tab2-country-dropdown", "value"), 
    Input("tab2-region-dropdown", "value"), 
    Input("tab2-world-toggle", "value"), 
    Input("tab2-years-rangeslider", "value"))
def lineplot_renewable(country, region, toggle, years):
    """
    Docs
    """
    df_use = df_all[df_all['Entity'].isin([country] + region + len(toggle) * ["World"])]
    df_use = df_use[(df_use['Year'] >= years[0]) & (df_use["Year"] <= years[1])]
    fig = px.line(df_use, x="Year", y="Renewables (% sub energy)", color="Entity", 
        title=f'Renewables usage from {years[0]} to {years[1]}')
    
    return fig
    
    

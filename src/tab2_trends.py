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
#                 Placeholder for valid plots, remove afterwards
#==============================================================================  
df = px.data.gapminder().query("country=='Canada'")

#==============================================================================
#                            Layout for lineplots
#==============================================================================   

tab2_lineplots = dbc.Col([

        dcc.RangeSlider(min=0, 
                max=20, 
                step=1, 
                value=[5, 15],
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
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
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
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

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
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
    
    return fig
    
    

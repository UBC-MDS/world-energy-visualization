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
#                            Sidebar for Tab2
#==============================================================================
   
SIDEBAR2_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


sidebar2 = dbc.Col([
        html.H1("Historical Trends"),
        html.Hr(),
        
        html.H3(
            "Country",
            style={"width": "50%", "display": "inline-block"},
        ),
        html.Hr(),
        
        dbc.Col(
            dcc.Dropdown(
                id="tab2-country-dropdown",
                options=[{"label": country, "value": country} for country in list_of_countries],
                value=["Canada", "France"],
            ),
            width=12,
            style={
                "padding": "10px 10px 10px 0px",
            },
        ),
        html.Hr(),
        
        html.H3(
            "Region",
            style={"width": "50%", "display": "inline-block"},
        ),
        html.Hr(),
        dbc.Col(
            dcc.Dropdown(
                id="tab2-region-dropdown",
                options=[{"label": region, "value": region} for region in list_of_continents],
                multi=True,
                value=["North America", "Europe"],
            ),
            width=12,
            style={
                "padding": "10px 10px 10px 0px",
            },
        ),
        html.Hr(),
        
        html.H3(
            "World",
            style={"width": "50%", "display": "inline-block"},
        ),
        dbc.Checklist(
            options=[
                {"label": "Option 1", "value": 1},
            ],
            value=[1],
            id="tab2-world-toggle",
            switch=True,
        ),
    ],
    style=SIDEBAR2_STYLE,
)


#==============================================================================
#                            Lineplots
#==============================================================================

tab2_lineplots = dbc.Col([
        sidebar2, 
        html.H1("Fossil"),
        dcc.Graph(id="tab2-lineplot-fossil"),
        html.Hr(),
        
        html.H1("Nuclear"),
        dcc.Graph(id="tab2-lineplot-nuclear"),
        html.Hr(),
        
        html.H1("Renewable"),
        dcc.Graph(id="tab2-lineplot-renewable"),
        html.Hr(),
        
        dcc.RangeSlider(1950, 2022, 5,
                   value=1980,
                   id="tab2-years-rangeslider"
    ),
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
    
    
#==============================================================================
#                            Tab2 Layout
#==============================================================================    

tab2_layout = dbc.Container([
        dbc.Row([
            sidebar2,
            tab2_lineplots
        ]),   
    ],
    fluid=True,
    style={"width": "80%"},
)
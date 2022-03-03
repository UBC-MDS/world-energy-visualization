from dash import Input, Output, callback, html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

from tab2_trends import tab2_lineplots
#from app import SIDEBAR_STYLE

df_all = pd.read_csv("data/Primary-energy-consumption-from-fossilfuels-nuclear-renewables.csv")

df_notna = df_all[df_all['Code'].notna()]
df_countries = df_notna[df_notna['Code']!='OWID_WRL']
df_world = df_notna[df_notna['Code']=='OWID_WRL']
df_continents = df_all[df_all['Code'].isna()]

list_of_continents = df_continents['Entity'].unique()
list_of_countries = df_countries['Entity'].unique()


#==============================================================================
#                            Sidebar for Tab2
#==============================================================================

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    #"width": "16rem",
    "padding": "2rem 1rem",
    "background-image": "url(/assets/wind-energy.jpg)",
    "background-color": "rgba(255,255,255,0.6)",
    "background-blend-mode": "overlay",
}

sidebar2 = dbc.Col([
    
        html.H3("World Energy Visualisation"),
        html.H4("Historical Trends", style={"color":"#686868"}),
        html.Br(),
        
        html.H5(
            "Country",
            style={"width": "50%", "display": "inline-block"},
        ),
        html.P("Select a country to visualize its trend:", style={"color":"#686868", "margin": 0, "font-size": "14px"}),
        
        dbc.Col(
            dcc.Dropdown(
                id="tab2-country-dropdown",
                options=[{"label": country, "value": country} for country in list_of_countries],
                value="Canada",
            ),
            width=12,
            style={
                "padding": "10px 10px 10px 0px",
            },
        ),
        html.Br(),
        
        html.H5(
            "Region",
            style={"width": "50%", "display": "inline-block"},
        ),
        html.P("Select regions to compare with the country:", style={"color":"#686868", "margin": 0, "font-size": "14px"}),
        dbc.Col(
            dcc.Dropdown(
                id="tab2-region-dropdown",
                options=[{"label": region, "value": region} for region in list_of_continents],
                multi=True,
                value=["North America"],
            ),
            width=12,
            style={
                "padding": "10px 10px 10px 0px",
            },
        ),
        html.Br(),
        
        dbc.Row([
            html.H5(
                "Show World Trend",
                style={"width": "80%", "display": "inline-block"},
            ),
            dbc.Checklist(
                options=[
                    {"label": "", "value": 1},
                ],
                value=[1],
                id="tab2-world-toggle",
                switch=True,
            )
        ], style={
            "margin-left": "0px"
        })
    ],
    md=2,
    style=SIDEBAR_STYLE,
)


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
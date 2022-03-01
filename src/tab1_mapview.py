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
df_notna = df_notna.rename(columns={"Fossil fuels (% sub energy)": "Fossil", 
                         "Renewables (% sub energy)": "Renewables", 
                         "Nuclear (% sub energy)": "Nuclear"}).melt(id_vars=['Entity', 'Code', 'Year'], 
                                                                    value_vars=['Fossil',  "Renewables", "Nuclear"],
                                                                    var_name="energy_type",
                                                                    value_name="percentage")
df_countries = df_notna[df_notna['Code']!='OWID_WRL']
df_world = df_notna[df_notna['Code']=='OWID_WRL']
df_continents = df_all[df_all['Code'].isna()]

list_of_continents = df_continents['Entity'].unique()
list_of_countries = df_countries['Entity'].unique()

#==============================================================================
#                            Layout for map and barchart 
#==============================================================================       
    
tab1_plots = dbc.Col([
    dcc.Graph(id="tab1-map"),
    dcc.Slider( id='tab1-year-slider', 
                min=1965, 
                max=2015, 
                step=5, 
                value=2015,
                marks={i: str(i) for i in range(1965, 2015 + 1, 5)}),
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
    Output("tab1-map", "figure"), 
    Input("tab1-energy-type-dropdown", "value"),
    Input("tab1-year-slider", "value"))

def display_map(energy_type, year):
    """
    Docs
    """
    df = df_notna.query("Year==@year & energy_type==@energy_type")
    fig = px.choropleth(df, locations="Code",
                    color="percentage", 
                    hover_name="energy_type",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    )

    fig.update_layout(
            title={
            'text' : "Global " + str(energy_type) + " Energy Consumption in " + str(year),
            'x':0.5,
            'xanchor': 'center'
        })

    return fig
    
    
#==============================================================================
#                            Top N countries barchart
#==============================================================================    

@callback(
    Output("tab1-barchart", "figure"), 
    Input("tab1-energy-type-dropdown", "value"),
    Input("tab1-year-slider", "value"))
def display_barchart(energy_type, year):
    """
    Docs
    """
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
    
    return fig



from dash import Input, Output, callback, html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

df_all = pd.read_csv(
    "data/Primary-energy-consumption-from-fossilfuels-nuclear-renewables.csv"
)

df_notna = df_all[df_all["Code"].notna()]
df_countries = df_notna[df_notna["Code"] != "OWID_WRL"]
df_world = df_notna[df_notna["Code"] == "OWID_WRL"]
df_continents = df_all[df_all["Code"].isna()]

list_of_continents = df_continents["Entity"].unique()
list_of_countries = df_countries["Entity"].unique()

proj_param = {
    "World": [0, 0, 1],
    "North America": [40, -120, 2],
    "Europe": [50, 20, 4],
    "Africa": [0, 20, 2]
}

# ==============================================================================
#                            SideBar1
# ==============================================================================

SIDEBAR1_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "padding": "2rem 1rem",
    "background-image": "url(/assets/wind-energy.jpg)",
    "background-color": "rgba(255,255,255,0.6)",
    "background-blend-mode": "overlay",
}


sidebar1 = dbc.Col(
    [
        html.H3("World Energy Visualisation"),
        html.H4("Global Distribution", style={"color": "#686868"}),
        html.Br(),
        html.H5("Energy type"),
        html.P(
            "Select a energy type for visualization:",
            style={"color": "#686868", "margin": 0, "font-size": "14px"},
        ),
        dbc.Row(
            dcc.Dropdown(
                id="tab1-energy-type-dropdown",
                options=[
                    {"label": energy_type, "value": energy_type}
                    for energy_type in ["Fossil", "Nuclear", "Renewables"]
                ],
                value="Fossil",
            ),
            # width=12,
            style={
                "padding": "10px 10px 10px 0px",
            },
        ),
        html.Br(),
        html.H5("Map View"),
        html.P(
            "Select a region for map zoom in",
            style={"color": "#686868", "margin": 0, "font-size": "14px"},
        ),
        dbc.Row(
            dcc.Dropdown(
                id="tab1-map-focus",
                options=[
                        {"label": region, "value": region}
                        for region in proj_param
                    ],
                    value="World",
                    clearable=False
            ),
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
            dcc.Markdown(
                """
                Datasets for visualization of energy trends were downloaded from [here](https://www.kaggle.com/donjoeml/energy-consumption-and-generation-in-the-globe)
            """
            ),
        ),
    ],
    md=2,
    style=SIDEBAR1_STYLE,
)

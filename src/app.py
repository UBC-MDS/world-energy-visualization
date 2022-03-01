import dash
from dash import Input, Output, callback, html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

from tab1_sidebar import sidebar1
from tab1_mapview import tab1_plots
from tab2_sidebar import tab2_layout

app = dash.Dash(__name__, 
                title = "World Energy Visualization",
                external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

TABS_STYLE = {
    "position": "fixed",
    "top": 0,
    "right": 20,
    "bottom": 0,
    "width": "80%",
    "padding": "2rem 1rem",
    "overflow-y": "scroll"
}

app.layout = dbc.Container([
                    dbc.Row([
                        sidebar1,
                            dbc.Col([
                                dbc.Tabs([
                                    dbc.Tab(
                                        tab1_plots,
                                        label="Map view",
                                        tab_id="tab1_mapview",
                                    ),
                                    dbc.Tab(
                                        tab2_layout,
                                        label="Trends",
                                        tab_id="tab2_trends",
                                    ),
                                ],
                                id="tabs",
                                active_tab="tab1_mapview",
                                )
                            ],
                            md=10,
                            style=TABS_STYLE,
                    ),
])],
fluid=True,
style={"width": "80%",},
)



if __name__ == '__main__':
    app.run_server(debug=True)
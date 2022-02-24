import dash
from dash import Input, Output, callback, html, dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

from tab1_sidebar import *
from tab1_mapview import *
from tab2_trends import *


app = dash.Dash(__name__, 
                title = "World Energy Visualization",
                external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


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
                    # dbc.Tab(
                        # tab2_layout,
                        # label="Trends",
                        # tab_id="tab2_trends",
                    # ),
                ],
                id="tabs",
                active_tab="tab1_mapview",
                )
            ]),
        ]),
        
    ],
    fluid=True,
    style={"width": "80%",},
)


if __name__ == '__main__':
    app.run_server(debug=True)
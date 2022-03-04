from dash import Input, Output, callback, html, dcc
import dash_bootstrap_components as dbc

import numpy as np
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
list_yrs = df_all["Year"].unique()

# ==============================================================================
#                            Layout for lineplots
# ==============================================================================

tab2_lineplots = dbc.Col(
    [
        html.Div(
            [
                html.P(
                    "Select the year range for the below plots:",
                    style={"color": "#888888"},
                ),
                dcc.RangeSlider(
                    min=list_yrs.min(),
                    max=list_yrs.max(),
                    step=1,
                    value=[list_yrs.min(), list_yrs.max()],
                    marks={
                        int(i): str(i)
                        for i in np.append(list_yrs[::5], [list_yrs.max()])
                    },
                    tooltip={"placement": "top", "always_visible": False},
                    id="tab2-years-rangeslider",
                ),
            ],
            style={"padding-top": "30px"},
        ),
        html.Br(),
        dcc.Graph(id="tab2-lineplot-fossil"),
        dcc.Graph(id="tab2-lineplot-nuclear"),
        dcc.Graph(id="tab2-lineplot-renewable"),
    ]
)


# ==============================================================================
#                            Lineplots
# ==============================================================================


@callback(
    Output("tab2-lineplot-fossil", "figure"),
    Input("tab2-country-dropdown", "value"),
    Input("tab2-region-dropdown", "value"),
    Input("tab2-world-toggle", "value"),
    Input("tab2-years-rangeslider", "value"),
)
def lineplot_fossil(country, region, toggle, years):
    """
    Docs
    """
    df_use = df_all[df_all["Entity"].isin([country] + region + len(toggle) * ["World"])]
    df_use = df_use[(df_use["Year"] >= years[0]) & (df_use["Year"] <= years[1])]
    fig = px.line(
        df_use,
        x="Year",
        y="Fossil",
        color="Entity",
        title=f"Fossil fuels usage from {years[0]} to {years[1]}",
    )
    fig.update_layout(
        title={"x": 0.5, "y": 0.8, "xanchor": "center", "yanchor": "bottom"}
    )
    return fig


@callback(
    Output("tab2-lineplot-nuclear", "figure"),
    Input("tab2-country-dropdown", "value"),
    Input("tab2-region-dropdown", "value"),
    Input("tab2-world-toggle", "value"),
    Input("tab2-years-rangeslider", "value"),
)
def lineplot_nuclear(country, region, toggle, years):
    """
    Docs
    """
    df_use = df_all[df_all["Entity"].isin([country] + region + len(toggle) * ["World"])]
    df_use = df_use[(df_use["Year"] >= years[0]) & (df_use["Year"] <= years[1])]
    fig = px.line(
        df_use,
        x="Year",
        y="Nuclear",
        color="Entity",
        title=f"Nuclear fuel usage from {years[0]} to {years[1]}",
    )
    fig.update_layout(
        title={"x": 0.5, "y": 0.8, "xanchor": "center", "yanchor": "bottom"}
    )

    return fig


@callback(
    Output("tab2-lineplot-renewable", "figure"),
    Input("tab2-country-dropdown", "value"),
    Input("tab2-region-dropdown", "value"),
    Input("tab2-world-toggle", "value"),
    Input("tab2-years-rangeslider", "value"),
)
def lineplot_renewable(country, region, toggle, years):
    """
    Docs
    """
    df_use = df_all[df_all["Entity"].isin([country] + region + len(toggle) * ["World"])]
    df_use = df_use[(df_use["Year"] >= years[0]) & (df_use["Year"] <= years[1])]
    fig = px.line(
        df_use,
        x="Year",
        y="Renewables",
        color="Entity",
        title=f"Renewables usage from {years[0]} to {years[1]}",
    )
    fig.update_layout(
        title={"x": 0.5, "y": 0.8, "xanchor": "center", "yanchor": "bottom"}
    )

    return fig

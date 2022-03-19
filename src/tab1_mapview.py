from dash import Input, Output, callback, html, dcc, State
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

from urllib.request import urlopen
import json

df_all = pd.read_csv(
    "data/Primary-energy-consumption-from-fossilfuels-nuclear-renewables.csv"
)
df_notna_wide = df_all[df_all["Code"].notna()]
df_notna = df_notna_wide.melt(
    id_vars=["Entity", "Code", "Year"],
    value_vars=["Fossil", "Renewables", "Nuclear"],
    var_name="energy_type",
    value_name="percentage",
).merge(df_notna_wide, on=["Year", "Code", "Entity"])

df_countries = df_notna[df_notna["Code"] != "OWID_WRL"]
df_world = df_notna[df_notna["Code"] == "OWID_WRL"]
df_continents = df_all[df_all["Code"].isna()]

list_of_continents = df_continents["Entity"].unique()
list_of_countries = df_countries["Entity"].unique()
list_yrs = df_all["Year"].unique()

proj_param = {
    "World": [0, 0, 1],
    "North America": [40, -120, 2],
    "Europe": [50, 20, 4],
    "Africa": [0, 20, 2],
}

# ==============================================================================
#                            Layout for map and barchart
# ==============================================================================

tab1_plots = dbc.Col(
    [
        dbc.Row(
            [
                html.H4("World Consumption by Country", style={"width": "fit-content"}),
                dbc.Col(
                    [
                        dbc.Button(
                            id="map_tooltip",
                            color="secondary",
                            children="?",
                            size="sm",
                            outline=True,
                        ),
                        dbc.Tooltip(
                            "Drag and select the number of year to view the change of engergy consumption distribution using the slide bar. You can hover or zoom to get the details of a specific region.",
                            target="map_tooltip",
                            placement="bottom",
                        ),
                    ]
                ),
            ],
            style={"padding": "3vh 0"},
        ),
        dcc.Graph(id="tab1-map"),
        html.Div(
            dcc.Slider(
                id="tab1-year-slider",
                min=list_yrs.min(),
                max=list_yrs.max(),
                step=1,
                value=list_yrs.max(),
                marks={
                    int(i): str(i) for i in np.append(list_yrs[::5], [list_yrs.max()])
                },
                tooltip={"placement": "top", "always_visible": True},
                updatemode="drag",
            ),
            style={"padding": "0vh 10vw"},
        ),
        html.Br(),
        dbc.Row(
            [
                html.H4(
                    "Top/Bottom energy consumer nations", style={"width": "fit-content"}
                ),
                dbc.Col(
                    [
                        dbc.Button(
                            id="bar_tooltip",
                            color="secondary",
                            children="?",
                            size="sm",
                            outline=True,
                        ),
                        dbc.Tooltip(
                            "Select the number of countries to view in the bar plot using the input tab,"
                            "then select whether to view to the top or bottom consumers."
                            "Hover the bar for details.",
                            target="bar_tooltip",
                            placement="bottom",
                        ),
                    ],
                    style={"padding": "0 0"},
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                html.H4(
                                    "Number of countries",
                                    style={"font-size": "20px", "width": "fit-content"},
                                ),
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            id="topN_tooltip",
                                            color="secondary",
                                            children="?",
                                            size="sm",
                                            outline=True,
                                        ),
                                        dbc.Tooltip(
                                            "Controls the number of countries to view in the barchart. Select upto 15 countries",
                                            target="topN_tooltip",
                                            placement="bottom",
                                        ),
                                    ],
                                    style={"padding": "0 0"},
                                ),
                            ]
                        ),
                        html.Br(),
                        dbc.Input(
                            id="tab1-input-topN",
                            value=10,
                            type="number",
                            debounce=True,
                            required=True,
                            minlength=1,
                            max=15,
                            min=0,
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                html.H4(
                                    "Ranking type",
                                    style={"font-size": "20px", "width": "fit-content"},
                                ),
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            id="top_bot_tooltip",
                                            color="secondary",
                                            children="?",
                                            size="sm",
                                            outline=True,
                                        ),
                                        dbc.Tooltip(
                                            "Select whether you want to view the top or bottom consumers",
                                            target="top_bot_tooltip",
                                            placement="bottom",
                                        ),
                                    ],
                                    style={"padding": "0 0"},
                                ),
                            ]
                        ),
                        html.Br(),
                        dcc.RadioItems(
                            ["Top", "Bottom"],
                            value="Top",
                            id="tab1_top_bot",
                            inline=True,
                            labelStyle={
                                "margin-right": "10px",
                                "margin-top": "1px",
                                "display": "inline-block",
                                "horizontal-align": "",
                            },
                        ),
                    ],
                    style={
                        "padding": "0 0",
                    },
                ),
            ]
        ),
        html.Br(),
        dcc.Graph(id="tab1-barchart"),
    ]
)


# ==============================================================================
#                            World Map
# ==============================================================================


@callback(
    Output("tab1-map", "figure"),
    Input("tab1-energy-type-dropdown", "value"),
    Input("tab1-year-slider", "value"),
    Input("tab1-map-focus", "value"),
)
def display_map(energy_type, year, scope):
    """
    Docs
    """
    # scope = "Africa"
    df = df_notna.query("Year==@year & energy_type==@energy_type")

    fig = px.choropleth(
        df,
        locations="Code",
        color="percentage",
        hover_name="Entity",
        hover_data={
            "Year": True,
            "Fossil": True,
            "Nuclear": True,
            "Renewables": True,
            "percentage": False,
            "Code": False,
        },
        color_continuous_scale=px.colors.sequential.YlGn,
        range_color=[0, 100],
    )

    fig.update_layout(
        dragmode="zoom",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        title={
            "text": "Global "
            + str(energy_type)
            + " Energy Consumption in "
            + str(year),
            "x": 0.5,
            "xanchor": "center",
        },
    )

    fig.update_geos(
        showcountries=True,
        center={"lat": proj_param[scope][0], "lon": proj_param[scope][1]},
        projection={"scale": proj_param[scope][2]},
    )

    return fig


# ==============================================================================
#                            Top N countries barchart
# ==============================================================================


@callback(
    Output("tab1-barchart", "figure"),
    Input("tab1-energy-type-dropdown", "value"),
    Input("tab1-year-slider", "value"),
    Input("tab1-input-topN", "value"),
    Input("tab1_top_bot", "value"),
)
def display_barchart(energy_type, year, topN, top_bot):
    """
    Docs
    """

    if top_bot == "Top":
        df_sorted = df_countries.query(
            "Year==@year & energy_type==@energy_type"
        ).sort_values(["percentage"], ascending=False)[:topN]

    elif top_bot == "Bottom":
        df_sorted = df_countries.query(
            "Year==@year & energy_type==@energy_type"
        ).sort_values(["percentage"], ascending=False)[-topN:]

    fig_bar = px.bar(
        df_sorted,
        x="percentage",
        y="Entity",
        color="percentage",
        # title="Bar Graph",
        hover_name="Entity",
        hover_data={
            "Year": True,
            "Fossil": True,
            "Nuclear": True,
            "Renewables": True,
            "percentage": False,
            "Entity": False,
        },
        range_color=[0, 100],
        color_continuous_scale=px.colors.sequential.YlGn,
        range_x=[0, 105],
        text_auto=True,
    )

    fig_bar.update_layout(
        xaxis_title="Percentage %",
        yaxis_title="Country",
        legend_title="%",
    )
    fig_bar.update_coloraxes(showscale=False)
    fig_bar.update_traces(textposition="outside")

    if top_bot == "Top":
        fig_bar.update_layout(
            yaxis={"categoryorder": "total ascending"},
            title={
                "text": "Top "
                + str(topN)
                + " "
                + str(energy_type)
                + " Energy Consumers in "
                + str(year),
                "x": 0.5,
                "xanchor": "center",
            },
        )

    elif top_bot == "Bottom":
        fig_bar.update_layout(
            # yaxis={"categoryorder": "total descending"},
            title={
                "text": "Bottom "
                + str(topN)
                + " "
                + str(energy_type)
                + " Energy Consumers in "
                + str(year),
                "x": 0.5,
                "xanchor": "center",
            },
        )

    return fig_bar

from dash import Input, Output, callback, html, dcc, State
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

from urllib.request import urlopen
import json


with urlopen(
    "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
) as response:
    counties = json.load(response)


df_all = pd.read_csv(
    "data/Primary-energy-consumption-from-fossilfuels-nuclear-renewables.csv"
)
df_notna = df_all[df_all["Code"].notna()]
df_notna = df_notna.rename(
    columns={
        "Fossil fuels (% sub energy)": "Fossil",
        "Renewables (% sub energy)": "Renewables",
        "Nuclear (% sub energy)": "Nuclear",
    }
).melt(
    id_vars=["Entity", "Code", "Year"],
    value_vars=["Fossil", "Renewables", "Nuclear"],
    var_name="energy_type",
    value_name="percentage",
)
df_countries = df_notna[df_notna["Code"] != "OWID_WRL"]
df_world = df_notna[df_notna["Code"] == "OWID_WRL"]
df_continents = df_all[df_all["Code"].isna()]

list_of_continents = df_continents["Entity"].unique()
list_of_countries = df_countries["Entity"].unique()

# ==============================================================================
#                            Layout for map and barchart
# ==============================================================================

tab1_plots = dbc.Col(
    [
        dcc.Graph(id="tab1-map"),
        dcc.Slider(
            id="tab1-year-slider",
            min=1965,
            max=2015,
            step=1,
            value=2015,
            marks={i: str(i) for i in range(1965, 2015 + 1, 5)},
            tooltip={"placement": "top", "always_visible": True},
            updatemode="drag",
        ),
        html.Br(),
        html.H4("Top/Bottom energy consumer nations"),
        html.H6(
            "Select the number of countries to view in the bar plot using the input tab, then select whether to view to the top or bottom consumers. The plot has an hover option to view the percentage if the text is too small.",
            style={"font-size": "15px"},
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4(
                            "Number of countries",
                            style={"font-size": "20px"},
                        ),
                        html.Br(),
                        dbc.Input(
                            id="tab1-input-topN",
                            value=10,
                            type="number",
                            debounce=True,
                            required=True,
                            minlength=1,
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.H4(
                            "Ranking type",
                            style={"font-size": "20px"},
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
                        "padding": "0px 0px 0px 50px",
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
)
def display_map(energy_type, year):
    """
    Docs
    """
    df = df_notna.query("Year==@year & energy_type==@energy_type")
    fig = px.choropleth(
        df,
        locations="Code",
        color="percentage",
        hover_name="energy_type",
        color_continuous_scale=px.colors.sequential.YlGn,
        range_color=[0, 100],
    )

    fig.update_layout(
        title={
            "text": "Global "
            + str(energy_type)
            + " Energy Consumption in "
            + str(year),
            "x": 0.5,
            "xanchor": "center",
        }
    )

    return fig


# ==============================================================================
#                            Top N countries barchart
# ==============================================================================


@callback(
    Output("tab1-barchart", "figure"),
    Input("tab1-energy-type-dropdown", "value"),
    Input("tab1-region-dropdown", "value"),
    Input("tab1-year-slider", "value"),
    Input("tab1-input-topN", "value"),
    Input("tab1_top_bot", "value"),
)
def display_barchart(energy_type, region, year, topN, top_bot):
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
        range_color=[0, 100],
        color_continuous_scale=px.colors.sequential.YlGn,
        range_x=[0, 100],
        text_auto=True,
    )

    fig_bar.update_layout(
        xaxis_title="Percentage %",
        yaxis_title="Country",
        legend_title="%",
    )
    fig_bar.update_coloraxes(showscale=False)

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
            yaxis={"categoryorder": "total descending"},
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

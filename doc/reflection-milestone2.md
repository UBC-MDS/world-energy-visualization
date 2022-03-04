# Reflection of milestone 2

## Implementation of the Dashboard

### Data Wranggling

The kaggle dataset [Renewable vs Nuclear Energy generation](https://www.kaggle.com/donjoeml/energy-consumption-and-generation-in-the-globe) is used for this project.
The dataset contains 4 csv files, which illustrated the proportion of energy source of eletricity production and consumption for each country from
1965 to 2019. We mainly used `Primary-energy-consumption-from-fossilfuels-nuclear-renewables.csv`. Sine the kaggle data is well process,
there is not special data wranggling required, except renaming three columns, from `Fossil fuels (% sub energy)`, `Renewables (% sub energy)`,
`Nuclear (% sub energy)` to `Fossil`, `Renewables`, and `Nuclear` respectively. Compare to script writing, this simple process is done maunelly.
The edited csv is stored in data folder.

### Dashboard design

World Energy Visualizatoin dashboard will consists of two tabs, where the first tab provides a high level overview, while the second tab gives a more granular
detailed information about trends for energy consuption over many years.  As can be seen from the sketch shown in Figure 1, in the main dashboard users will be
able gain a high level insight about countries with some dominant type of energy, such as "nuclear", "fossil fuel" or "renewable energy". Also with a simple switch,
 users of the dashboard will be able to identify countries at the bottom of the list, which are lagging behind in adoption of certain type of energy. Besides this
 tab of the dashboard will provide visualization of the world map colored by a fraction of energy type consumed in each country.

<p align="center">
  <img src="1_map_and_bar_chart.PNG" width=600>
  </br>
  Figure 1. Overview of the main tab
</p>

At the second tab of the app, users will be able to select one or a few countries for comparison between each other or with certain regions. All those trends
of energy consumption over time will be realized as line plots as schematically shown in Figure 2.

<p align="center">
  <img src="2_trends.PNG" width=600>  
  </br>
  Figure 2. Prototype for the dashboard with trends
</p>

## Roadmap

### World Map of Energy Consumption (tab1)

- Animation of map can be added to show the change of energy consumption throughout the years
- Regional filter can be incorporated, with auto zoom into the region based on the selection 

### Bar Chart of Top 'N'/Bottom 'N' Energy Consumers (tab1)

- This chart displays a specified number of top or bottom consumers by percentage for the selected energy source and year. 
- Currently, the ordering is only computed using the percentage of consumption. Hence very large and small countries are compared on the same scale. Though the data does not have the actual units of consuption, a proxy metric such as the units of power generated from different sources can also be incorporated to get a better sense of the scale. Another solution is to incorporate this data using an additional data source.
- One limitation with this plot is that there are certain years in which multiple countries have a 0% consuption for a type of energy source. This is particularly true for the nuclear energy consuption, as only a few countries in the world have access to it. Hence a useful feature to incorporate would be an option for the user to filter out zeros when looking at the bottom countries. This ensures that the information is filtered transparently, and that the user is not mislead by the results. 
- The regional filter can be incorporated to list the top/bottom countries by region. 

### Line plot of Energy Consumption by energy (tab2)

- Currently, the tab visualizes only the trend of energy consumption of major energy sources with line plots.
Since the dataset has a more comprehensive data, including percentage of production and consumption of individual
sources of energy, we would consider adding these plots along with corresponding filter and selection boxes.
- Moreover, the `Region` box now only has 3 options, `North America`, `Europe` and `Africa`, which is due to
the sparcity of the dataset. However, it is also considered to compute the data values of missing continents
and sub-regions by data from corresponding countries.

## Limitation of the Dashboard

- The dashboard is better to be used full screen on Chrome, not mobile compatable.
- A loading icon can be incorporated for all the plots as the render to let the user know that the plots are rendering. 

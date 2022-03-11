# Reflection of milestone 2

## Implementation of the Dashboard

### Data Wranggling - keep?

The kaggle dataset [Renewable vs Nuclear Energy generation](https://www.kaggle.com/donjoeml/energy-consumption-and-generation-in-the-globe) is used for this project.
The dataset contains 4 csv files, which illustrated the proportion of energy source of eletricity production and consumption for each country from
1965 to 2019. We mainly used `Primary-energy-consumption-from-fossilfuels-nuclear-renewables.csv`. Since the kaggle data is well process,
there is not special data wranggling required, except renaming three columns, from `Fossil fuels (% sub energy)`, `Renewables (% sub energy)`,
`Nuclear (% sub energy)` to `Fossil`, `Renewables`, and `Nuclear` respectively. Compared to script writing, this simple process is done manually.
The edited csv is stored in data folder. 

### Dashboard design - add screenshots instead of the diagrams?

![](demo.gif)

As can be seen on short demonstration above World Energy Visualizatoin dashboard onsists of two tabs, where the first tab provides a high level overview,
while the second tab gives a more granular detailed information about trends for energy consuption over many years.  

In the main dashboard users are able gain an insight about countries with some dominant type of energy, such as "nuclear", "fossil fuel" or "renewable energy". This is realized with visualization of the world map colored by a fraction of energy type consumed in each country. Also with a simple switch, users of the dashboard can identify countries at the bottom of the list, which are lagging behind in adoption of certain type of energy.

At the second tab of the dashboard, users can select one or a few countries for comparison between each
other or with certain regions.

## Roadmap

### Overall Dashboard Design 

The dashboard has been designed with 2 tabs - one to display the global trends in energy consumption and the second to focus on the time series data of specific nations and regions. There is a global filter on either tab on the left of the dashboard that allows the user to select the type of energy they would like to view the information of. In each tab, there are other sliders, input bars and buttons to control specific plots.

### World Map of Energy Consumption (tab1)

#### Current Implementation:

- This is a world chloropleth map that shows the percentage energy consuption for every country for the specified energy type. The year displayed on the plot is controlled by a slider below it.

#### Limitations and future direction:

- Animation of map can be added to show the change of energy consumption throughout the years instead of the user sliding across all the years manually.
- The map can zoom into a particular region when selected to make it easier to anlyze those particular countries. It is currently difficult to view some of the smaller nations and regions with many nations.

### Bar Chart of Top 'N'/Bottom 'N' Energy Consumers (tab1)

#### Current Implementation:

- This chart displays a specified number of top or bottom consumer nations by percentage for the selected energy source. The year is controlled by the same slider as the world map so that both plots are synced.

#### Limitations and future direction:

- The ordering is only computed using the percentage of consumption. Hence very large and small countries are compared on the same scale. Though the data does not have the actual units of consuption, a proxy metric such as the units of power generated from different sources can also be incorporated to get a better sense of the scale. Another solution is to incorporate this data using an additional data source.
- There are certain years in which multiple countries have a 0% consuption for a type of energy source. This is particularly true for the nuclear energy consuption, as only a few countries in the world have access to it. Hence a useful feature to incorporate would be an option for the user to filter out zeros when looking at the bottom countries. This ensures that the information is filtered transparently, and that the user is not mislead by the results. 
- The regional filter can be incorporated to list the top/bottom countries by region. 

### Line plot of Energy Consumption by energy (tab2)

#### Current Implementation:

- These charts display the percentage of energy sources consumed by country, region, as well as the world trend. The lines displayed are controlled by the selection boxes in the sidebar.
- Currently, the tab visualizes only the trend of energy consumption of major energy sources, i.e. Fossil fuels, Nuclear and Renewables, with line plots.

#### Limitations and future direction:

- Since the dataset has a more comprehensive data, including percentage of production and consumption of individual
sources of energy, we would consider adding these plots along with corresponding filter and selection boxes.

- Moreover, the `Region` box now only has 3 options, `North America`, `Europe` and `Africa`, which is due to
the sparcity of the dataset. However, it is also considered to compute the data values of missing continents
and sub-regions by data from corresponding countries.

### Limitation of the overall Dashboard

- The dashboard is better to be used full screen on Chrome, not mobile compatible.
- A loading icon can be incorporated for all the plots as the render to let the user know that the plots are rendering. 
- Additional work can done with making the app look more appealing. This can be implemented by tweaking style of the blocks inline or changing CSS settings. 

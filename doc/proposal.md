# World Energy Visualization

## Motivation and Purpose

Role: Data Scientists working for the World Bank
Target: Policy makers in the World Bank making decisions related to energy

Climate change is an imminent threat to humanity. Therefore, the switch to renewable and nuclear energy from fossil fuels is paramount in mitigating its effects. Though there are annual reports and other sources that detail the trends in global energy consumption, these are often static representations of the data. Therefore it can be difficult to visualize trends over time and compare the trends for the different sources of energy. This app aims to facilitate the analysis of the type of energy consumed over time and identify the countries leading the transition to alternative energy. The user will be able to filter for the type of energy and year and view the consumption patterns globally. The time series plots this app provides can be used to compare the performance of selected countries against the global and regional averages over time. Policy makers can use this information to identify countries that currently have effective policies or otherwise allocate a larger budget to countries lagging in the transition.
  
## Dataset Description

In this dashboard, we will be visualizing the [Renewable vs Nuclear Energy generation](https://www.kaggle.com/donjoeml/energy-consumption-and-generation-in-the-globe) dataset. The kaggle dataset contains 4 csv files,

1. **Primary-energy-consumption-from-fossilfuels-nuclear-renewables.csv**  
    - Global primary energy consumption in fossil fuels, renewables and nuclear per country
    - 6 columns with 4284 rows
2. **global_power_plant_database_last.csv**  
    - A global dataset of power plants built per country
    - 36 columns with 34.9k+ rows
3. **share-elec-produc-by-source.csv**  
    - Total electricity production percentage in oil, coal, solar, nuclear, hydro, wind and gas per country
    - 11 columns with 6190 rows
4. **share-elec-consum-by-source.csv**  
   - Total energy consumption percentage in oil, coal, solar, nuclear, hydro, wind and gas per country.
   - 11 columns with 4284 rows

The files record the proportion of energy source of eletricity production and consumption for each country from 1965 to 2019, as well highlight the type and capacity of energy production from every power plants in the world.  

For the csv files (1, 3, 4), they record the percentage of energy type for power consumption/production with shared columns.

| columns                              | explanation                                          |
|--------------------------------------|------------------------------------------------------|
| `Entity`, `Code`                     | The country or region, `Code` using ISO country code |
| `Year`                               | Year of record                                       |
| `(% sub energy)`, `(% electricity)`  | Percentage values                                    |

For the csv file (2), it contains power plant data. Apart from the country and year, it also provides the production capacity (`capacity_mw`) of power plant in each country and its type of energy source (`primary fuel`).

With the four files, we will visualize the percentage of energy consumption/production by broad types (`Fossil Fuels`, `Renewables`, `Nuclear`) and sub-types (`Coal`, `Gas`, `Hydro`, `Solar`, `Wind`, `Oil`, `Nuclear`) in each country. The number and total capacity of power plants in each country by their primary energy type would also be calculated and rendered as one of the numeric attributes available for users to select.

## Concepts being investigated

John is a policy maker in the Energy department of the World Bank.  He is well aware of the need for nations to reduce their consumption of fossil fuels and switch to alternate energy forms such as renewables and nuclear energy. He is in charge of crafting the World Bank’s annual energy policy that includes identifying nations to provide monetary or strategic support for energy initiatives. To do so, he needs to explore a dataset that contains the consumption of energy by type by nation and region, and understand the trends over a period of time. He uses the `Map View` on `World Energy Visualization` app to understand energy consumption on a global scale. This page contains a shaded world map by percentage consumption for a given year, and a bar chart lists either the top or bottom ten nations with the lowest percentage consumption. He uses the slider to visualize the change in percentage consumption by year on the map.  Additionally, he filters for the specific type of energy source, region of interest, and whether he wants to view the top or bottom consumers by percentage. He selects the number of countries to view on the bar graph. In doing so, he notices there are a few countries that particularly concern him ,and he switches to the `Trends` tab. Here, he views the time series plots over a selected range of years for the percentage consumption for each energy type. He filters for 2 countries of interest at a time, and compares them to the regional and global averages. With this, he identifies specific trends in consumption for the nation. Additionally, he takes special note of the nations that are lagging behind in their own regions. With these insights, not only he is aware of the global energy consumption landscape but countries that should be the primary focus of this year’s policy. He will conduct further research into these nations with respect to their current energy policies and economics. He will also contact the policy makers in the nations with the highest renewable energy adoptions to discuss strategies that could be implemented in other nations.

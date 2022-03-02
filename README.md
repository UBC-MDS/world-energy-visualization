# World Energy Visualization

Authors: Macy Chan, Philson Chan, Mukund Iyer, Pavel Levchenko

## Welcome

This app has a goal to provide an easy access to information related to types of energy consumed at every country and multiple regions over the last few decades. This information could be beneficial to policy makers, who are in charge of making decision related to climate change and forcing transition to cleaner energy sources. More details about potential usage of this dashboard can be found in the [proposal document](proposal.md).

## Table of Content

* [What are we doing? (And why?)](#what-are-we-doing)
* [Who are we?](#who-are-we)
* [What are we doing?](#what-are-we-doing)
* [Description of the Dashboard](#description-of-the-dashboard)
* [Contributing to this Dashboard](#contributing-to-this-dashboard)
* [License](#license)
* [Credits](#credits)

## Who are we

## What are we doing

### Our Motivation

Climate change is an imminent threat to humanity. Therefore, the switch to renewable and nuclear energy from fossil fuels is paramount in mitigating its effects. Though there are annual reports and other sources that detail the trends in global energy consumption, these are often static representations of the data. Therefore it can be difficult to visualize trends over time and compare the trends for the different sources of energy. This app aims to facilitate the analysis of the type of energy consumed over time and identify the countries leading the transition to alternative energy. The user will be able to filter for the type of energy and year and view the consumption patterns globally. The time series plots this app provides can be used to compare the performance of selected countries against the global and regional averages over time. Policy makers can use this information to identify countries that currently have effective policies or otherwise allocate a larger budget to countries lagging in the transition.
  
### Problems we are trying to solve and why is it important

## Description of the Dashboard

> Place holder for the Git

World Energy Visualizatoin dashboard will consists of two tabs, where the first tab provides a high level overview, while the second tab gives a more granular detailed information about trends for energy consuption over many years.  As can be seen from the sketch shown in Figure 1, in the main dashboard users will be able gain a high level insight about countries with some dominant type of energy, such as "nuclear", "fossil fuel" or "renewable energy". Also with a simple switch, users of the dashboard will be able to identify countries at the bottom of the list, which are lagging behind in adoption of certain type of energy. Besides this tab of the dashboard will provide visualization of the world map colored by a fraction of energy type consumed in each country.

At the second tab of the app, users will be able to select one or a few countries for comparison between each other or with certain regions. All those trends of energy consumption over time will be realized as line plots as schematically shown in Figure 2.

## Contributing to this Dashboard

If you have any ideas regarding to this project and wish to help, you are welcome to contribute.

### Calling for developer
The dashboard currently have implemented all the basic functionality, yet there are some potential enhancements and additional features. We welcome all contributors to help with implementation of the following features.  
### What do we need
Pontential features include:
- Add an chronological animation to the world map
- Visualization of locations & production of power plants
- Trends of energy consumption & producton by individual source of energy

You are also welcomed to raise new ideas and report any existing bugs. Please go through the [contributing guidelines](CONTRIBUTING.md) for the recommended ways to do so.
### How to install and run locally
To run the dashboard locally, it is recommeded to use a virtual environment like [venv](https://docs.python.org/3/library/venv.html) or [Anaconda](https://www.anaconda.com/). For simplicity, we could demonstrate the installiation process with venv.

#### Set up
Run the following command at the root directory of the project:
```
# Create the virtual environment
python -m venv energy-viz

# Activate the environment
source energy-viz/bin/activate

# Install the requirements
pip install -r requirements.txt
```

#### Run the dashboard
```
python src/app.py
```
The dashboard could then be accessed locally in <localhost:8050>, and you are good to go!

### Contributing Guidelines

You may also please review our [contributing guidelines](CONTRIBUTING.md) for more information.

## License

`world-energy-visualization` dashboard is licensed under the terms of the MIT license.

## Credits

Datasets for visualization of energy trends were downloaded from <https://www.kaggle.com/donjoeml/energy-consumption-and-generation-in-the-globe>

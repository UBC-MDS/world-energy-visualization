# Reflection of milestone 4

## Has it been easy to use your app?

- According to the peer feedback, the dashboard is easy to use in general. We tried to make our application as straightforward as possible with short descriptions of each plot.
- To have a better user experience, we added toggle buttons for descriptions to simplify the interface while information is still accessible if needed.
- We believe the two tabs by two categories - `Global Distribution` and `Historical Trends`- would conveniently help users locate the desired information and prevent being overwhelmed by charts and plots.

## What differences are there between the DashR and DashPy app?
- We were able to replicate fully functionality and visual aspects of DashR based on initial prototype of dashboard implementation in Python. All differences in implementations are only related to syntaxes differences between R and Python, however there were significant changes in code for making proper visualisation of sidebar which changes after clicking at tabs. For Python it was done very easily, but for R dashboard we needed to apply multiple additional logical functions in order to replicate visual aspect of DashPy.

- One more difference between R and Python implementations of our dashboard is in terms of overall architecture. Creating dashboard in Dash involves huge amount of brackets, so to make the code more readable, we splitted DashPy at four distinct blocks, which are much easier to read and maintain. However, for DashR we could not do this due to limitations of R versionof Dash, where is not clear how to use callbacks from separate files. 

## Are there reoccurring themes in your feedback on what is good and what can be improved?

Positives:

- Based on the peer review, one positive element of our app is the use of tabs to separate the plots displaying global information from the regional (more specific data). This has improved the user experience greatly as it reduces the number of plots they are presented with at once and allows them to focus on either a general global analysis or specific regional analysis. 
- Another reoccuring comment was that the app had an effective use of bootstrap components to organize the plots and filtering elements to make it easy for the users to use. In particular, the peer reviewer specified that our design and use of plots were appropriate for the persona we described who the app is intended to be used by.

Improvements: 

- One general trend in the feedback on the improvements was to do with the representation of the data in the world map and bar plot in the first tab. 
- In the context of the persona viewing the app, he/she needs to be explicitly made aware that a particular country is missing data. Additionally, analysis on smaller nations and regions like Europe where there are many nations will be compromised due to the lack of a zoom feature. 
- Furthermore, if the persona were to do an analysis of countries that are the smallest consumers, there is a lack of communication when the consumption percentage is zero. 

## Is there any feedback (or other insight) that you have found particularly valuable during your dashboard development?

- From the peer review, some valuable feedbacks are made towards our layouts and graph visualizations.
- One of the problems is that the zero-valued countries are unable to be properly shown in the Top/bottom country barplot, which caused users to misunderstand the graph. Hence we decided to add labels to show the actual values, which could help to indicate the value is zero.
- Another feedback we received from the review is that many countries are missing from the map, while all the missing countries are shown in the same color in a contiguous block, which might be hard for users to understand. Hence the map would be improved to show all the country boundaries, so that users would be able to check the availability of data of a specific country more easily.

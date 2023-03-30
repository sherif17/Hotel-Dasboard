### Milestone 2 Reflection

In this milestone, the group developed a working version of an interactive dashboard in Python and successfully deployed the app on Heroku. Early in this milestone, it became evident that the main plots and features included in the proposal were not as value-adding as we initially thought. As a group, we made the decision to adapt the strategy and implement new ideas in order to better serve our customer (i.e. end-user). 

#### Features Implemented

The initial proposal included a crossplot feature where the user could select any two variables to see if and how they related to each other. After prototyping this, however, the majority of plots were not useful to the end-user. Instead, the main plot of the dashboard now contains time-series data where the user can choose a y-axis variable from a dropdown selector. There are currently eight y-variables to choose from that have been selected due to their importance to the end-user.  

Two other interactive plotting features have been included in this release. Both allow the user to filter data in ways that could be useful to the hotel management business. This includes a button selection that allows the user to choose to see data from city, resort or both types of hotels. There is also a slider bar that allows the user to see data for particular seasons (e.g spring).

In addition to the main plot, two histogram plots containing useful information about guests have been included. The data in these plots update with the two interactive plotting features (i.e. filters) mentioned in the previous paragraph. 

#### Strengths and Limitations

The strengths of the dashboard at the time of this release are:

* Clean layout
* Easy to interact with
* Relevant information to the end-user

One of the challenges of the dashboard was in coding interactivity that performed modifications on the data. To overcome this, some data wrangling was required on the front end of the dashboard script. There are likely more elegant and flexible solutions that we can explore as we continue to improve the dashboard. As a result of these challenges, the current interactive features are fairly simplistic and rigid for the time being.

Another limitation of the dashboard is that the width of the display does not adapt to the width of the screen of the viewer. 

#### Future Improvements

Future improvements to the dashboard include adding more end-user flexibility and implementing several more widgets that will make the dash board more informative. This includes features such as:

* Tile showing number of data observations selected
* Tiles to show the top 5 variable counts in the bar charts
* Potential for more plotting interactivity and additional variables of interest
* Ability to view time-series data over full range of time (currently expressed as weekly summaries)
* Layout and aesthetic improvements


## Milestone 4 Reflection

The goal for this milestone was to finalize a dashboard that includes improvements to make visualization meaningful and incorporate the feedback from prior release. One of the main considerations was developing in R versus Python. The main advantage of working in the R version was better load speed while opening the app on the browser. However, the troubleshooting was much easier on the Python version. Also, the deployment time on Heroku was quicker on the Python version. This made the Python version the more feasible choice for the final deployment.

### Features Implemented

The dashboard is designed for upper management so that they can get the information easily and in a digestible manner. Hence, one of the most significant changes in this iteration was in the data wrangling process to make the dashboard more readable. The two new filters "year" and "month" reflect the leap year correctly on the dashboard now. Also, a user can compare the selected year with the previous year to see the seasonal or unexpected trend changes in the selected feature. To summarize data in the plots, averages, maximum and minimum metrics are included on a monthly and daily level. In addition, the lines and the legends in the trend charts are clickable to highlight one of the lines to improve clarity. All plots have a hover effect to display the value of the data.

This version of the app also included one additional plot to show daily trends on the selected feature. The purpose of this was to give users a more comprehensive and granular level of information - similar to what was provided in the original dataset.

The second most significant changes in this iteration is the design changes that were implemented. This new version has styling that helps users to interact with the dashboard to get the insights effortlessly. “Learn more” tab is added to provide additional information about the dashboard. “Help” tab provides instructions to the user on how to interact with the plots and filters. The layout of the dashboard is also changed to filter the informationon on the plots. The Global controls (two vertical filters) will work on every plot of the dashboard. However, “Select feature to plot” (the top horizontal filter) works only on the top two plots (trends) of the dashboard. The slider to select the weeks was removed as per TA's feedback.

There is also additional text and links at the bottom of the dashboard so users can find more information about who built the app, where they can find the original data and source code. Finally, the aesthetics of the plots have been improved to be more visually appealing.

### Strengths and Limitations

The strengths of the dashboard at the time of this release are:

* Clean layout
* Easy to interact with
* Relevant information to the end-user

The limitation of the dashboard is that the width of the display does not adapt to the width of the screen of the viewer. In addition, the limited data from the source make this dashboard only able to display data over a two-year time window. 

### Future Improvements

Future improvements to the dashboard include adding more end-user flexibility to make dashboard more informative. This includes features such as:

* Filtering data on the bar graph such as clicking on a bar of  "Countries of origin" plot and displaying the filtered information on "Lengths of stay" plot.

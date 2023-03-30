# Proposal
# 1. Motivation and Purpose

**Our role:** Data scientist consultancy firm

**Target audience:** Internal management of a hotel company

Better customer understanding and good customer service can improve internal efficiencies resulting in higher revenues. To help in this goal, we propose building a data visualization app that allows the top administration to visually explore their company's booking data to identify key characteristics of customers, missed opportunities (in terms of cancelled reservations) and services ordered by customers to help understand their needs. Our Super-Hotels-Happy-Manager-Info app will illustrate the key metrics and trends and further allow users to explore different aspects of this data by filtering and re-ordering of different variables in order to better understand customer's needs. 


# 2. Description of the data

The data set we used in building the dashboard comes from the *Hotel Booking demand datasets* from Antonio, Almeida and Nunes at Instituto Universitario de Lisboa (ISCTE-IUL), Lisbon, Portugal (Antonio, Almeida, and Nunes 2019). The data can be found from the GitHub Repository [here](https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-02-11). 

The data is compased of two smaller datasets each containing reservation data from Super-Hotels in Portugal. One set from hotel in a city and one from a resort hotel. Each row in the dataset is an individual hotel reservation that occured in  between July 1st, 2015 and August 31st, 2017. There are a total of 119,390 booking details with 31 features. 40,060 observations from the resort hotel and 79,330 observations from the city hotel are included in this dataset.

Each observation has numerical features such as number of adults, number of previous cancellations etc., and categorical features such as room type reserved, type of meal booked etc. We will select the best features to be displayed in our app in order to deliver an informative dashboard.


# 3. Research questions and usage scenarios

Mary is an Executive Director with the Super-Hotels company in Portugal. She wants to see the overall trends in the market and what relationships exist among the variables available in the reservation data to make better marketing and internal policies. When Mary logs on to the Super-Hotels-Happy-Manager-Info app, she will see the summary of all the key metrics such as reservations made by year/months to see the seasonality effect on the business. She can also better manage internal resources to account for seasonal fluctuations in business. This will help her in making strategies to attract customers in the off-season. She can also filter trends by locations, type of customers etc. so that she can focus on one segment and can design marketing promotions to attract them. She can see the main factors that are contributing the most in the success story such as the top 5 types of meal ordered. She can also see the effect of one variable on another variable, for example the impact of having kids on demanding extra services.
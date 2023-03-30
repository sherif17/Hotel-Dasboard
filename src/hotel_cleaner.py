# hotel_cleaner.py
# author: Trevor Kinsey
# date: 2021-01-19

'''This script cleans and wrangles the hotels.csv file to be used
   in a visualization dashboard app

Usage: python hotel_cleaner.py

'''
import numpy as np
import pandas as pd

# import the data
hotels = pd.read_csv("data/raw/hotels.csv")

# create new columns from other columns
months = ["January", "February", "March", "April",
          "May", "June", "July", "August", "September", 
          "October", "November", "December"]
hotels["arrival_date_month"] = hotels["arrival_date_month"].replace(months,[1,2,3,4,5,6,7,8,9,10,11,12])
hotels["Arrival date"] = pd.to_datetime(hotels.arrival_date_year*10000 + hotels.arrival_date_month*100 + hotels.arrival_date_day_of_month, 
                                        format = '%Y%m%d')
hotels["Arrival day of week"] = hotels["Arrival date"].dt.dayofweek
hotels["Arrival day of week"] = hotels["Arrival day of week"].replace([0,1,2,3,4,5,6],["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"])
hotels["Total nights"] = hotels["stays_in_weekend_nights"] + hotels["stays_in_week_nights"]
# drop unused columns
hotels = hotels.drop(columns=['agent', 'company', 'lead_time',
                              'market_segment', 'distribution_channel',
                              'is_repeated_guest', 'previous_cancellations',
                              'previous_bookings_not_canceled', 'reserved_room_type',
                              'assigned_room_type','deposit_type',
                              'days_in_waiting_list', 'customer_type', 'reservation_status', 
                              'reservation_status_date', 'meal'], )
# Change values to make more readable
hotels["hotel"] = hotels["hotel"].replace(["Resort Hotel", "City Hotel"], ["Resort", "City"])
# change column names to make more readable
hotels.columns = ['Hotel type', 'Cancelled', 'Arrival year',
                  'Arrival month', 'Arrival week', 'Arrival day', 'Weekend nights', 
                  'Week nights', 'Adults', 'Children', 'Babies', 'Country of origin', 
                  'Booking changes', 'Average daily rate', 'Required parking spaces', 
                  'Special requests', "Arrival date", "Arrival day of week", 'Total nights']
                 
# # create date index column for date slider
# hotels["arrival_date_index"] = pd.to_numeric(hotels["Arrival date"])/60/60/24/10**9
# start_date = hotels["arrival_date_index"][0]
# hotels["arrival_date_index"] -= start_date

#  save to file
hotels.to_csv("data/processed/clean_hotels.csv", index = False)
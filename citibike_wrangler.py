# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 14:48:00 2015

@author: MU03179
"""

import pandas as pd
bikedata = pd.read_csv('C:/Users/mu03179/Desktop/NYU/PUI_project/201509-citibike-tripdata.csv')
print bikedata.columns
print bikedata.shape
station_combos = bikedata.drop_duplicates(subset=['start station latitude','start station longitude','end station latitude','end station longitude'])[['start station latitude','start station longitude','end station latitude','end station longitude']]
station_coords = bikedata.drop_duplicates(subset=['start station latitude','start station longitude'])[['start station latitude','start station longitude']]

print station_coords.shape
station_coords.columns = ['station latitude','station longitude']
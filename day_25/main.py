#!/usr/bin/python3

import csv
import pandas

# basic file I/O method
# with open("227 - weather-data.csv") as wdat:
#     data = wdat.readlines()

# csv library method
# with open("227 - weather-data.csv") as dat_file:
#     data = csv.reader(dat_file)
#     temperatures = []
#     for row in data:
#         if not row[1] == 'temp':
#             temperatures.append(int(row[1]))
# print(temperatures)

# pandas method

data = pandas.read_csv("227 - weather-data.csv")
print(data['temp'])

data_dict = data.to_dict()
temp_list = data_dict['temp'].to_list()

# challenge 1 - calculate average temp of temp series {normal-method}
total = 0
for temperature in temp_list:
    total += temperature
average_temperature = total / len(temp_list)

# pandas method for calculating average
avg_temp = data['temp'].mean()

# challenge 2- find the maximum temperature reached using pandas lib
max_temp = data['temp'].max()

# get data in a Row
print(data[data.day == "Monday"])

# challenge 3 - get row with the highest temp
print(data[data.temp == max_temp])

# create a datafrome from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_from_dict = pandas.DataFrame(data_dict)

# convert a datafranme to a csv file
data_from_dict.to_csv("new_data.csv")


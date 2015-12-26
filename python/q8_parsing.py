#!/usr/bin/python
# -*- coding: utf-8 -*-

#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv
import pandas as pd
import os 

dirname = os.path.dirname(os.path.abspath(__file__))

def read_data(filename):
	fileRoute = dirname + '/' + filename
	data = pd.read_csv(fileRoute)
	return data

def get_min_score_difference(parsed_data):
	parsed_data['goalDiff'] = abs(parsed_data['Goals'] - parsed_data['Goals Allowed'])
	return parsed_data
    

def get_team(filename):
	data = read_data(filename)
	data = get_min_score_difference(data)
	sortedData=data.sort_values('goalDiff')
	team = sortedData[0:1]['Team'].values
	return 'The team with the smallest difference is: ' + team[0]
    # COMPLETE THIS FUNCTION

print get_team('football.csv')
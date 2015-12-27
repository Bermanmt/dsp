import pandas as pd
import os 
import re

dirname = os.path.dirname(os.path.abspath(__file__))

def read_data(filename):
	fileRoute = dirname + '/' + filename
	data = pd.read_csv(fileRoute)
	data.columns = ['name', 'degree', 'title', 'email']
	return data

#Question 6
def separate_name_and_lastname(data):
	splitted = data['name'].apply(lambda x: re.split(r'\s', x))
	first_names=[]
	last_names = []
	for name in splitted: 
		first_names.append(name[0])
		last_names.append(name[-1])
	data['first_name']=pd.Series(first_names, index=data.index)
	data['last_name']=pd.Series(last_names, index=data.index)
	return data

def clean_title(data):
	pass

def print_first_three(prof_dict):
	keys = prof_dict.keys()
	for i in range(3):
		print keys[i],': ', prof_dict[keys[i]]


def sort_last(tuples):
    lista = sorted(tuples, key= lambda tup: tup[-1])
    return lista
		

def create_dict_by_last_name(data):
	withLastNames = separate_name_and_lastname(data)
	uniqueLastNames=list(set(data['last_name'].values))
	professor_dict={}
	for name in uniqueLastNames:
		lists=map(list,data[data['last_name']==name][['degree','title','email']].values)
		professor_dict[name]=lists
	return professor_dict

#Question 7
def create_dict_with_name_tuple(data):
	dataValues = data.values
	prof_dict={}
	for professor in dataValues:
		prof_dict[(professor[-2],professor[-1])]=[professor[1],professor[2],professor[3]]
	return prof_dict

#Question 8
def order_dict_by_last_name(prof_dict):
	sortedKeys=sort_last(prof_dict.keys())
	orderedKeyValues= []
	for i in sortedKeys:
		orderedKeyValues.append([i,prof_dict[i]])
	return orderedKeyValues


#Results:

data = read_data('faculty.csv')
dataSeparatedNames = separate_name_and_lastname(data)
professor_dict= create_dict_by_last_name(data)
prof_dict = create_dict_with_name_tuple(data)
ordered_dict = order_dict_by_last_name(prof_dict)

print 'Question 6'
print '-'*30
print
print 'The first three key-value pairs of the array are:'
print_first_three(professor_dict)
print
print 'Question 7'
print '-'*30
print
print 'The first three key-value pairs of the array are:'
print_first_three(prof_dict)
print
print 'Question 8'
print '-'*30
print
print 'The first three key-value pairs of the array are:'
print
for i in range(3):
	print ordered_dict[i][0],': ', ordered_dict[i][1]








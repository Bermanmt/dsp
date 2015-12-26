import pandas as pd
import os 
import re

dirname = os.path.dirname(os.path.abspath(__file__))

def read_data(filename):
	fileRoute = dirname + '/' + filename
	data = pd.read_csv(fileRoute)
	data.columns = ['name', 'degree', 'title', 'email']
	return data

#Code Question 1
def removeDecimals(text):
	text = text.replace('.','')
	return text

def find_unique_degrees(data):
	data['degree']=data['degree'].apply(lambda x : removeDecimals(x))
	dataList = list(data['degree'].unique())
	joinedList = ' '.join(dataList)
	splitList = re.split(r'\s', joinedList)
	finalList = []
	for degree in splitList:
		if degree != '0' and degree!='' and degree not in finalList:
			finalList.append(degree)
	return finalList

def find_frequency_of_degrees(data):
	degreeList = data['degree'].values
	joinedList = ' '.join(degreeList)
	splitList = re.split(r'\s', joinedList)
	finalDegreeList = filter(lambda x: x!='' and x!='0', splitList)
	listOfUniqueDegrees=find_unique_degrees(data)
	degreeFrecuency = {}
	for degree in listOfUniqueDegrees:
		degreeFrecuency[degree] = finalDegreeList.count(degree)
	return degreeFrecuency

#Code Question 2
def clean_up_title_column(data):
	data['title']=data['title'].apply(lambda x: x.replace(' is', ' of'))
	return data

def get_unique_titles(data):
	pass

#Answers
data = read_data('faculty.csv')
listOfUniqueDegrees = find_unique_degrees(data)
countOfUniqueDegrees = len(listOfUniqueDegrees)
frecuencyOfUniqueDegrees = find_frequency_of_degrees(data)

print('Question 1:')
print '-'*30
print 'There are a total of ' + str(countOfUniqueDegrees) + ' different degrees.' 
print 'Each Degree Frecuency is: '
for key, value in enumerate(frecuencyOfUniqueDegrees):
	print value + ':' + str(frecuencyOfUniqueDegrees[value])
print 
print('Question 2:')
print '-'*30





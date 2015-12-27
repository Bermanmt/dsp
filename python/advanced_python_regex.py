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
	cleanData = clean_up_title_column(data)
	uniqueTitles = list(data['title'].unique())
	uniqueTitlesJoined = ' '.join(uniqueTitles)
	uniqueTitlesOnlyTitles = re.split(r' of Biostatistics',uniqueTitlesJoined)
	uniqueTitlesOnlyTitles.pop()
	finalTitleList = []
	for title in uniqueTitlesOnlyTitles:
		finalTitleList.append(title.lstrip())
	counts = cleanData['title'].value_counts()
	return {'counts': counts, 'titles':finalTitleList}

#Code Question 3
def get_emails(data):
	return list(data['email'])

#Code Question 4

def get_email_domain_count(data):
	emailList = list(data['email'].values)
	strippedDomains=[]
	for email in emailList: 
		locate= re.search(r'@',email)
		index= locate.end()
		strippedDomains.append(email[index:])
	strippedDomainsUnique = set(strippedDomains)
	return list(strippedDomainsUnique)


#Answers
data = read_data('faculty.csv')
listOfUniqueDegrees = find_unique_degrees(data)
countOfUniqueDegrees = len(listOfUniqueDegrees)
frecuencyOfUniqueDegrees = find_frequency_of_degrees(data)

uniqueTitles = get_unique_titles(data)
listOfEmails = get_emails(data)

emailDomains = get_email_domain_count(data)

print('Question 1:')
print '-'*30
print 'There are a total of %s different degrees.' %(countOfUniqueDegrees) 
print
print 'Each Degree Frecuency is: '
for key, value in enumerate(frecuencyOfUniqueDegrees):
	print value + ': ' + str(frecuencyOfUniqueDegrees[value])
print 
print('Question 2:')
print '-'*30
print 'There are a total of %s different titles on the list' %(len(uniqueTitles['titles']))
print
print 'The titles are: ' + ', '.join(uniqueTitles['titles'])
print 
print 'The frecuencies for each one of the titles are: '
print
print uniqueTitles['counts']
print
print('Question 3:')
print '-'*30
print
print 'This is the complete list of emails in the document: '
print
print listOfEmails
print
print('Question 4:')
print '-'*30
print
print 'There are a total of %s different email domains'%(len(emailDomains))
print
print 'The domain names are: ', emailDomains










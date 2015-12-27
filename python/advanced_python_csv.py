import pandas as pd
import os 
dirname = os.path.dirname(os.path.abspath(__file__))

def read_data(filename):
	fileRoute = dirname + '/' + filename
	data = pd.read_csv(fileRoute)
	data.columns = ['name', 'degree', 'title', 'email']
	return data

data = read_data('faculty.csv')
emailData = data['email']

emailData.to_csv(dirname+'/'+'emails.csv', index=False)
print 'File Successfully Exported'

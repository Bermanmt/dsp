# Hint:  use Google to find python function
from datetime import datetime

####a) 
date_format = '%m-%d-%Y'
date_start = '01-02-2013'  
date_stop = '07-28-2015'  

start = datetime.strptime(date_start, date_format)
stop =  datetime.strptime(date_stop, date_format)

numberOfDays = stop-start
print 'A)', numberOfDays.days

####b) 
date_format = '%d-%b-%Y'
date_start = '12312013'  
date_stop = '05282015'  

date_start = datetime.fromtimestamp(float(date_start)).strftime('%d-%b-%Y')
date_stop =  datetime.fromtimestamp(float(date_stop)).strftime('%d-%b-%Y')

start = datetime.strptime(date_start, date_format)
stop =  datetime.strptime(date_stop, date_format)

numberOfDays = start-stop
print 'B)',numberOfDays.days

####c)  
date_format = '%d-%b-%Y'
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

start = datetime.strptime(date_start, date_format)
stop =  datetime.strptime(date_stop, date_format)

numberOfDays = stop-start
print 'C)',numberOfDays.days




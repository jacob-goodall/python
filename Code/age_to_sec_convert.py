# Figure out your age
import datetime
currentDate = datetime.datetime.now()
#gets current date and time

deadline = input ('Please enter your date of birth (dd/mm/yyyy): ')
deadlineDate = datetime.datetime.strptime(deadline,'%d/%m/%Y')
#removes time from the input
print(deadlineDate)
daysLeft = deadlineDate - currentDate
daysLeft = abs(daysLeft)
#makes it to a postive number
print(daysLeft)

years = ((daysLeft.total_seconds())/(365.242*24*3600))
years = abs(years)
yearsInt = int(years)

months =(years-yearsInt)*12
months = abs(months)
monthsInt =int(months)

days =(months-monthsInt)*(365.242/12)
days = abs(days)
daysInt = int(days)

hours = (days-daysInt)*24
hours = abs(hours)
hoursInt = int(hours)

minutes = (hours-hoursInt)*60
minutes = abs(minutes)
minutesInt = int(minutes)

seconds = (minutes-minutesInt)*60
seconds = abs(seconds)
secondsInt = int(seconds)

print('You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} \
 minutes, {5:d} seconds old.'.format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt))

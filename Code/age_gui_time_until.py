import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot():
    global daysuntill
    x1 = entry1.get()
    import datetime
    currentDate = datetime.datetime.now()
    # gets current date and time

    deadline = x1
    deadlineDate = datetime.datetime.strptime(deadline, '%d/%m/%Y')
    # removes time from the input
    print(deadlineDate)
    daysLeft = deadlineDate - currentDate
    daysLeft = abs(daysLeft)
    # makes it to a postive number
    print(daysLeft)

    yearofborn = deadlineDate.strftime('%Y')
    yearnow = currentDate.strftime('%Y')
    yeardiff = int(yearnow) - int(yearofborn)
    print(yeardiff)
    if yeardiff < 18:
        print('under')
        timeuntillyears = 18 - yeardiff
        x2 = int(yearnow) + int(timeuntillyears)
        daysuntill = (datetime.datetime(x2,1,28) - datetime.datetime.now()).days
        daysuntill = abs(daysuntill)
        print(daysuntill)

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

    label1 = tk.Label(root, text='You are ' + str(yearsInt) + ' years, ' + str(monthsInt) + ' months, ' + str(daysInt) + ' days, ' + str(hoursInt) + ' hours, ' + str(minutesInt) + ' minutes, ' + str(secondsInt) + ' seconds old. \n Days until 18 years old: ' + str(daysuntill))
    canvas1.create_window(200, 230, window=label1)



button1 = tk.Button(text='Get Birthday in Seconds', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()

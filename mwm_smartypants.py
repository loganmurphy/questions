q1

dates = [
        'Oct 7, 2009', 'Nov 10, 2009', 'Jan 10, 2009',
        'Oct 22, 2009', 'Oct 3, 2004', 'Dec 10, 1984',
        'May 10, 1984', 'Jun 11, 1989', 'May 10, 2002'
    ]

months  = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12"
}

def date_sorter(dates, months):
    splitDates = []
    intDates = []
    sorted_dates = []
# Here I am splitting the dates into lists and removing the commas
    for date in dates:
        new_date = date.replace(',','')
        split_date = new_date.split(' ')
        splitDates.append(split_date)

    # Here I am replacing the months with their number equivalent
    # and I convert each date list into a single number string

    for date in splitDates:
        date[0] = months[date[0]]
        if len(date[1]) == 1:
            date[1] = "0{}".format(date[1])
        newDate = [date[2], date[0], date[1]]
        newDate = ''.join(newDate)
        newDate = newDate
        intDates.append(newDate)

    # Here I sort the number-string dates in descending order
    intDates = sorted(intDates, reverse=True)

    # Here I re-convert the sorted dates back to the original format.
    for date in intDates:
        newDate = [date[4:6], date[6:], date[:4]]
        newDate[0]
        for key, value in months.iteritems():
            if value == newDate[0]:
                newDate[0] = key
                sorted_dates.append(newDate)

    print(sorted_dates)

date_sorter(dates, months)

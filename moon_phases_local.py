#!/usr/bin/env python

# moon phases

moonPhase={}

import csv

def read_in_phases(fileName):
    with open(fileName, 'rb') as csvfile:
        moonphases=csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in moonphases:
            moonPhase[row[0]] = row[1]


def convertDateWithOffset(firstDate, Offset):
    YEAR=int(firstDate[2:4])
    MONTH=int(firstDate[4:6])
    DAY=int(firstDate[6:8])

    DAY = DAY + Offset

    if (DAY > 31):
        DAY=1
        MONTH = MONTH + 1

    if (MONTH > 12):
        MONTH=1
        YEAR = YEAR + 1

    return str(MONTH) + "/" + str(DAY) + "/" + str(YEAR)

def get_moon_phases(dateToRetrieve):
    # YYYYMMDD

    notFound=1
    counter=0
    while(notFound):
        date_to_check = convertDateWithOffset(dateToRetrieve, counter)
        if date_to_check in moonPhase:
            notFound
            return moonPhase[date_to_check]
        else:
            counter = counter + 1

read_in_phases('moon-phases.csv')
print get_moon_phases("20110110")

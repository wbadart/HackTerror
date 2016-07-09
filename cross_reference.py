import csv, json
from urllib2 import urlopen

base = 'http://api.wunderground.com/api/d0787b21158eb20b'

def load_gtb():
    fs = open('gtb2.csv', 'r')
    reader = csv.reader(fs)
    data = []
    for row in reader:
        data.append(row)
    fs.close()
    return data

db = load_gtb()

def two_dig(n):
    if int(n) < 10:
        return '0{}'.format(n)
    else:
        return str(n)

def get_history(lat=12.123, longt=14.123, date='20150328'):
    url = base + '/geolookup/q/{},{}.json'.format(lat, longt)

    loc = json.loads(urlopen(url).read())['location']
    city = str(loc['city'])
    country = str(loc['country_name'])

    if country == 'USA':
        country = str(loc['state'])

    url = base + '/history_{}/q/{}/{}.json'.format(date, country, city.replace(' ', '_'))
    data = json.loads(urlopen(url).read())

    return data

def get_attack_dict(eventID):
    for attack in db:
        if attack[0] == str(eventID):
            return attack
    return -1

def get_attack_weather(eventID):
    obj = get_attack_dict(eventID)
    lat   = obj[13]
    longt = obj[14]
    date  = obj[1] + two_dig(obj[2]) + two_dig(obj[3])

    data = get_history(lat, longt, date)
    return data



if __name__ == '__main__':
    fs = open('gtb.csv', 'r')
    reader = csv.reader(fs)
    
    data = []
    for row in reader:
        data.append(row)

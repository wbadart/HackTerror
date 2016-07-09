#!/usr/bin/env python

import json
import requests

limit_of_queries=1000
client_auth="&client_id=Uh3GM2dCNM1N4HA3dLdCZ&client_secret=ZN9Qe5pO1RbQIZLxxF0tTpnh7SCNW5WvL4us6EVA"
base_url="http://api.aerisapi.com/sunmoon/moonphases/"
query_string="LOCATION?from=FROM_DATE&to=TO_DATE&limit=LIMIT"

def query_moon_phases_from_provider(from_date, to_date, location):
    new_from_date=from_date[:4]+"-"+from_date[4:6]+"-"+from_date[6:]
    new_to_date=to_date[:4]+"-"+to_date[4:6]+"-"+to_date[6:]
    query=query_string.replace('LOCATION', location).replace('FROM_DATE', new_from_date).replace('TO_DATE', new_to_date).replace(" ", "+").replace("LIMIT", str(limit_of_queries))
    print(base_url+query+client_auth)
    return requests.get(base_url+query+client_auth)

def get_moon_phase_for_date(date, location):

json_obj=query_moon_phases_from_provider("20100505", "20130506", "Washington, DC").json()

for i in json_obj:
    print json_obj[i]

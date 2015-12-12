import requests, json
import os, sys, time
import ephem
import time
import math
import numpy as np
import geocoder
import urllib2
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from datetime import datetime
#from ephem_mathematics import *
from geopy.geocoders import Nominatim
noradID = 25544#sys.argv[1]

#space-track
#req json data TLEs
#noradID not as input
st_url = "https://www.space-track.org/basicspacedata/query/class/tle_latest/NORAD_CAT_ID/25544/limit/1/format/3le/ORDINAL/1/"
auth = requests.post("https://www.space-track.org/ajaxauth/login",
                     data={'identity': 'timuzi2011@gmail.com', 'password': 'timuzi!19901025'})
res = requests.get(st_url, cookies=auth.cookies.get_dict())

#geo_url = "https://maps.googleapis.com/maps/api/geocode/output?parameters"

zip = 24060 #sys.argv[2]
g_locator = Nominatim()
location = g_locator.geocode(zip)

ob_longitude = location.longitude
ob_lattitude = location.latitude #observer's location


print res.text
print(ob_longitude, ob_lattitude)


######################
#parsing


# Check for HTTP codes other than 200
if res.status_code != 200:
    print('Status:', res.status_code, 'Problem with the request. Exiting.')
    exit()


#current date/time
current_time=datetime.utcnow()
print(current_time)


#parsing
j_lines = res.json() #decode Json  use the data
keyword = ['TLE_LINE0', 'TLE_LINE1', 'TLE_LINE2']
for k, v in json.res.iteritems():
    if k in keyword:
        name = v
        print(v)
        #break

#visibility
def seconds_between(d1, d2):
    return abs((d2 - d1).seconds)

def datetime_from_time(tr):
    year, month, day, hour, minute, second = tr.tuple()
    dt = datetime.datetime(year, month, day, hour, minute, int(second))
    return dt

def get_next_pass(lon, lat, alt, tle):

    sat = ephem.readtle(str(tle[0]), str(tle[1]), str(tle[2]))
    observer = ephem.Observer()
    observer.lat = str(lat)
    observer.long = str(lon)
    observer.elevation = alt
    observer.pressure = 0
    observer.horizon = '-0:34'

    now = datetime.datetime.utcnow()
    observer.date = now

    tr, azr, tt, altt, ts, azs = observer.next_pass(sat)

    duration = int((ts - tr) *60*60*24)
    rise_time = datetime_from_time(tr)
    max_time = datetime_from_time(tt)
    set_time = datetime_from_time(ts)

    observer.date = max_time

    sun = ephem.Sun()
    sun.compute(observer)
    sat.compute(observer)

    sun_alt = degrees(sun.alt)

    visible = False
    if sat.eclipsed is False and -18 < degrees(sun_alt) < -6 :
        visible = True

    return {
             "rise_time": timegm(rise_time.timetuple()),
             "rise_azimuth": degrees(azr),
             "max_time": timegm(max_time.timetuple()),
             "max_alt": degrees(altt),
             "set_time": timegm(set_time.timetuple()),
             "set_azimuth": degrees(azs),
             "elevation": sat.elevation,
             "sun_alt": sun_alt,
             "duration": duration,
             "visible": visible
           }

from skyfield.api import load, Topos
# from string import Template
from pytz import timezone
from datetime import datetime

class Celestial:
    def __init__(self, name):
        self.name = name
        self.caption = name.capitalize()
        self.set_object()

    def set_object(self):
        planets = load('de421.bsp')
        self.object = planets[self.name]

    # def observe(self, location, time):
    #     astrometric = location.position.at(time.astrometric_dt).observe(self.object).apparent()
    #     obj_name = self.caption
    #     loc_name = location.name
    #     alt, az, distance = astrometric.altaz()
    #     tm = time.local_dt
    #     observation = Template(
    #         'Obserwuję ${obj_name} w miejscowości ${loc_name} o czasie $tm: * Azymut: ${az} | * Wysokość: ${alt}').substitute(
    #         obj_name=obj_name, loc_name=loc_name, tm=tm, az=az, alt=alt)
    #     print(observation)

    def get_observation(self, location, time):
        astrometric = location.position.at(time.astrometric_dt).observe(self.object).apparent()
        obj_name = self.caption
        loc_name = location.name
        alt, az, distance = astrometric.altaz()
        tm = time.local_dt

        observation = {
            'objective': obj_name,
            'azimuth': az.degrees,
            'altitude': alt.degrees,
            'place': loc_name,
            'time': tm.strftime("%d.%m.%Y, %H:%M")
        }
        return observation

class Location:
    def __init__(self, name, longitude, latitude):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.set_position()

    def set_position(self):
        planets = load('de421.bsp')
        earth = planets['earth']
        self.position = earth + Topos(self.longitude, self.latitude)

class DateTime:
    def __init__(self, js_timestamp):
        self.timestamp = datetime.fromtimestamp(js_timestamp)
        self.set_time()

    def set_time(self):
        timescale = load.timescale()
        central = timezone('Europe/Warsaw')
        d = self.timestamp
        c = central.localize(d)
        self.astrometric_dt = timescale.utc(c)
        self.universal_dt = self.astrometric_dt.utc_datetime()
        self.local_dt = self.astrometric_dt.astimezone(central)

    def get_range(self):

        return month_range

class Observation:
    def __init(self, name, azimuth, altitude, place, time):
        self.name = name
        self.azimuth = azimuth
        self.altitude = altitude
        self.place = place
        self.time = time

def perform_observation(object, timestamp):
    # for observable in observables:
    celestial = Celestial(object)
    place = Location('Lodz', '51.0 N', '19.0 W')
    time = DateTime(int(timestamp))
    observation = celestial.get_observation(place, time)
    return observation
# perform_observation('venus')
# r = perform_observation('venus')
# print(r)
#-----INPUT----------------------------------
#1. Coords
# place = Location('Łódź', '51.0 N', '19.0 W')
#2. Time/Time range
# time = DateTime(1585254836)
#3. Celestial objects
# observables = ['sun', 'moon', 'mercury', 'venus', 'mars']
#-----MIDDLEWARE----------------------------------
# -cardinal world direction enum
# -from decimal coords to semi-decimal
# -get other planets
# -get sunset, sunrise and midnight times
# -get 1-day intervals from 1st till 1st
# -compute 3 lists for each night time for each day
# -eliminate objects below horizon
#-----OUTPUT----------------------------------
 # perform_observation('venus')
# print(datetime.time(time.timestamp))
#---------------------------------------------
from classes.celestial import Celestial
from classes.location import Location
from classes.date_time import DateTime

def debug(i):
    print('----------------------')
    print('\n\n\n\n\n\n\n\n\n\n\n')
    print(i)
    print('\n\n\n\n\n\n\n\n\n\n\n')
    print('----------------------')

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
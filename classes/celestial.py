from string import Template
from skyfield.api import load

class Celestial:
    def __init__(self, name):
        self.name = name
        self.caption = name.capitalize()
        self.set_object()

    def set_object(self):
        planets = load('de421.bsp')
        print(planets)
        self.object = planets[self.name]

    def observe(self, location, time):
        astrometric = location.position.at(time.astrometric_dt).observe(self.object).apparent()
        obj_name = self.caption
        loc_name = location.name
        alt, az, distance = astrometric.altaz()
        tm = time.local_dt
        observation = Template(
            'Obserwuję ${obj_name} w miejscowości ${loc_name} o czasie $tm: * Azymut: ${az} | * Wysokość: ${alt}').substitute(
            obj_name=obj_name, loc_name=loc_name, tm=tm, az=az, alt=alt)
        print(observation)

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
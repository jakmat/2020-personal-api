from skyfield.api import Topos, load

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
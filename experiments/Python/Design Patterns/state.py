class City(object):
    name = 'city'
    allowed = []

    def warp(self, city):
        if city.name in self.allowed:
            self.__class__ = city
            return 'From ' + str(self) + ' to ' + city.name + ' done'
        else:
            return 'From ' + str(self) + ' to ' + city.name + ' break'

    def __str__(self):
        return self.name


class MainCity(City):
    name = 'MainCity'
    allowed = ['MarineCity', 'SkyCity']


class MarineCity(City):
    name = 'MarineCity'
    allowed = ['MainCity']


class SkyCity(City):
    name = 'SkyCity'
    allowed = ['MainCity']


class CityPortal(object):
    def __init__(self):
        self.city = MainCity()

    def warp(self, city):
        return self.city.warp(city)

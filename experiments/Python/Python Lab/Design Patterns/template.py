class MakeMap:
    _tileset = None
    _events = None
    _enemies = None

    def load_tileset(self): pass
    def load_events(self): pass
    def load_enemies(self): pass

    def load(self):
        self.load_tileset()
        self.load_events()
        self.load_enemies()

    def describe(self):
        return 'It is a region of ' + str(self._tileset) + ' with some ' + str(self._events) + ' and a lot of ' + (','.join(self._enemies))


class MakeIceMap(MakeMap):
    def load_tileset(self):
        self._tileset = 'ice'

    def load_events(self):
        self._events = 'ice storm'

    def load_enemies(self):
        self._enemies = ['ice poring']


class MakeLavaMap(MakeMap):
    def load_tileset(self):
        self._tileset = 'lava'

    def load_events(self):
        self._events = 'erruption'

    def load_enemies(self):
        self._enemies = ['lava poring']

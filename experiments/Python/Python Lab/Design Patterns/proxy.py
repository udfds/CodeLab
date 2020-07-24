class Dungeon:
    def __init__(self, name):
        self._name = name

    def load_dungeon(self):
        return 'Building: ' + self._name

    def show_dungeon(self):
        return 'Dungeon: ' + self._name


class Proxy:
    def __init__(self, instance):
        self._instance = instance
        self._proxystate = None


class ProxyDungeon(Proxy):
    def show_dungeon(self):
        if self._proxystate == None:
            self._proxystate = 1
            return self._instance.load_dungeon()
        return self._instance.show_dungeon()

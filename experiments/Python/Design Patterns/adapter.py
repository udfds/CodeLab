class AdapterInterface:
    def attack(self): pass
    def live(self): pass


class SkeletonAdapter(AdapterInterface):
    def attack(self):
        return 2

    def live(self):
        return 10


class BeastAdapter(AdapterInterface):
    def attack(self):
        return 10

    def live(self):
        return 25


class AdapterClass(AdapterInterface):
    _instance = None

    def __init__(self, instance):
        self._instance = instance

    def attack(self):
        return self._instance.attack()

    def live(self):
        return self._instance.live()


class MiniBossAdapter:
    _adapter = None

    def set_adapter(self, adapter):
        self._adapter = AdapterClass(adapter)

    def attack(self):
        return self._adapter.attack() * 10

    def live(self):
        return self._adapter.live() * 100


class BossAdapter:
    _adapter = None

    def set_adapter(self, adapter):
        self._adapter = AdapterClass(adapter)

    def attack(self):
        return self._adapter.attack() * 25

    def live(self):
        return self._adapter.live() * 1000

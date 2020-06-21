class SpellFacade:
    def __init__(self):
        self.sorceries_service = SorceriesService()
        self.pyromancies_service = PyromanciesService()
        self.miracles_service = MiraclesService()

    def soul_arrow(self):
        return self.sorceries_service.soul_arrow()

    def fireball(self):
        return self.pyromancies_service.fireball()

    def heal(self):
        return self.miracles_service.heal()


class SorceriesService:
    def soul_arrow(self):
        return 'Soul arrows inflict magic damage, making them effective against iron armor, tough scales, and other physically resilient materials'


class PyromanciesService:
    def fireball(self):
        return 'The fire damage caused by fireballs makes them effective against corporeal beasts and Undead, who by nature fear flame.'


class MiraclesService:
    def heal(self):
        return 'To cast a miracle, the caster learns a tale of the Gods, and says a prayer to be blessed by its revelations. Heal is the shortest of such miraculous tales.'

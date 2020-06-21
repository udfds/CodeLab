class AbstractMonster:
    _name = None
    _family = None

    def __init__(self, name, family):
        self._name = name
        self._family = family

    def get_name(self):
        return self._name

    def get_family(self):
        return self._family


class FireElemental(AbstractMonster):
    def __init__(self):
        AbstractMonster.__init__(self, 'Fire elemental', 'elemental')


class FirePoring(AbstractMonster):
    def __init__(self):
        AbstractMonster.__init__(self, 'Fire poring', 'poring')


class IceElemental(AbstractMonster):
    def __init__(self):
        AbstractMonster.__init__(self, 'Ice elemental', 'elemental')


class IcePoring(AbstractMonster):
    def __init__(self):
        AbstractMonster.__init__(self, 'Ice poring', 'poring')


class MonsterFactory:
    def get_elemental(self): pass
    def get_poring(self): pass


class FireMonsterFactory(MonsterFactory):
    def get_elemental(self):
        return FireElemental()

    def get_poring(self):
        return FirePoring()


class IceMonsterFactory(MonsterFactory):
    def get_elemental(self):
        return IceElemental()

    def get_poring(self):
        return IcePoring()

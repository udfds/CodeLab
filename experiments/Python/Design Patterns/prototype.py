import copy


class MonsterPrototype:
    _head = None
    _body = None

    def clone(self):
        pass

    def get_head(self):
        return self._head

    def get_body(self):
        return self._body

    def describre(self):
        return 'Head is ' + str(self._head) + ' with a ' + str(self._body)


class ZombiePrototype(MonsterPrototype):
    def __init__(self):
        self._head = 'dirty and rotten'
        self._body = 'dirty, bloody and rotten'

    def clone(self):
        return copy.copy(self)


class SkeletonPrototype(MonsterPrototype):
    def __init__(self):
        self._head = 'skull'
        self._body = 'just bones'

    def clone(self):
        return copy.copy(self)


class MonsterPrototypeFactory():
    _zombie = None
    _skeleton = None

    @staticmethod
    def initialize():
        MonsterPrototypeFactory._zombie = ZombiePrototype()
        MonsterPrototypeFactory._skeleton = SkeletonPrototype()

    @staticmethod
    def get_zombie():
        return MonsterPrototypeFactory._zombie.clone()

    @staticmethod
    def get_skeleton():
        return MonsterPrototypeFactory._skeleton.clone()

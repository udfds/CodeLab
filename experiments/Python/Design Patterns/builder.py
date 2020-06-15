class MonsterBuilder:
    _builder = None

    def set_builder(self, builder):
        self._builder = builder

    def get_monster(self):
        monster = Monster()

        body = self._builder.get_body()
        head = self._builder.get_head()
        left = self._builder.get_left()
        right = self._builder.get_right()

        monster.set_body(body)
        monster.set_head(head)
        monster.set_left(left)
        monster.set_right(right)
        return monster


class Monster:
    def __init__(self):
        self._body = None
        self._head = None
        self._left = None
        self._right = None

    def set_body(self, body):
        self._body = body

    def set_head(self, head):
        self._head = head

    def set_left(self, left):
        self._left = left

    def set_right(self, right):
        self._right = right

    def describre(self):
        return 'Head is ' + str(self._head) + ' with a ' + str(self._body) + ' the left hand is ' + str(self._left) + ' and the right hand is ' + str(self._right)


class Builder:
    def get_body(self): pass
    def get_head(self): pass
    def get_left(self): pass
    def get_right(self): pass


class ZombieBuilder(Builder):
    def get_body(self):
        return 'dirty, bloody and rotten'

    def get_head(self):
        return 'dirty and rotten'

    def get_left(self):
        return 'rotten'

    def get_right(self):
        return 'broken and rotten'


class SkeletonBuilder(Builder):
    def get_body(self):
        return 'just bones'

    def get_head(self):
        return 'skull'

    def get_left(self):
        return 'missing'

    def get_right(self):
        return 'bones'

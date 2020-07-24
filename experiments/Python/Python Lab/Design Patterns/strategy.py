import types


class MoveSetStrategy:
    def __init__(self, function=None):
        self.name = 'MoveSet'
        if function is not None:
            self.execute = types.MethodType(function, self)

    def execute(self):
        return self.name


def moveset_a(self):
    return self.name + ' from execution A'


def moveset_b(self):
    return self.name + ' from execution B'

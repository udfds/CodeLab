class TwoHeadDragon():
    def __init__(self):
        self.left_head = IceDragon(self)
        self.right_head = FireDragon(self)

    def ice_breath(self):
        return self.left_head.ice_breath()

    def fire_breath(self):
        return self.right_head.fire_breath()

    def get_left_head(self):
        return self.left_head

    def get_right_head(self):
        return self.right_head


class IceDragon():
    def __init__(self, mediator):
        self._mediator = mediator

    def ice_breath(self):
        return 'Ice'

    def fire_breath(self):
        return self._mediator.fire_breath()


class FireDragon():
    def __init__(self, mediator):
        self._mediator = mediator

    def ice_breath(self):
        return self._mediator.ice_breath()

    def fire_breath(self):
        return 'Fire'

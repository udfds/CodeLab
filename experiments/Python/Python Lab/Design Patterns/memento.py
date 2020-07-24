import pickle


class SavePoint:
    def __init__(self):
        self.state = None

    def load(self, save_point):
        backup = pickle.loads(save_point)
        vars(self).clear()
        vars(self).update(backup)

    def save(self):
        return pickle.dumps(vars(self))

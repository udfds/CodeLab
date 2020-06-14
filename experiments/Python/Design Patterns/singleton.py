class Singleton:

    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception('Singleton violation')
        else:
            Singleton._instance = self

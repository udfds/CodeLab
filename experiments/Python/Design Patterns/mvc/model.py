import json


class DesignPattern(object):
    def __init__(self, name=None, design_type=None):
        self.name = name
        self.design_type = design_type

    def name(self):
        return self.name + ' - ' + self.design_type

    def getAll(self):
        database = open('database.txt', 'r')
        designs = []
        json_list = json.loads(database.read())

        for item in json_list:
            item = json.loads(item)
            design_pattern = DesignPattern(item['name'], item['design_type'])
            designs.append(design_pattern)
        return designs

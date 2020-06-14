class Entity(object):
    description = ''

    def get_description(self):
        return self.description


class Hero(Entity):
    description = 'Current caracter'


class Monster(Entity):
    description = 'Regular enemy'


class Boss(Entity):
    description = 'Epic enemy'


class EntityFactory():
    def create_entity(self, entity_type):
        target_type = entity_type.capitalize()
        return globals()[target_type]()

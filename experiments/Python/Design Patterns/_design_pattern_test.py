import unittest
from singleton import Singleton
from factory import EntityFactory


class DesignPatternTest(unittest.TestCase):

    # TestCase Singleton
    def test_singleton(self):
        instance_a = Singleton.get_instance()
        instance_b = Singleton.get_instance()

        self.assertEqual(instance_a, instance_b)

    # TestCase Factory
    def test_factory(self):
        factory = EntityFactory()
        hero = factory.create_entity('hero')
        monster = factory.create_entity('monster')
        boss = factory.create_entity('boss')

        self.assertEqual(hero.get_description(), 'Current caracter')
        self.assertEqual(monster.get_description(), 'Regular enemy')
        self.assertEqual(boss.get_description(), 'Epic enemy')


if __name__ == '__main__':
    unittest.main()

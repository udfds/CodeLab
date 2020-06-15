import unittest

from singleton import Singleton
from factory import EntityFactory
from builder import ZombieBuilder
from builder import SkeletonBuilder
from builder import MonsterBuilder
from prototype import MonsterPrototypeFactory


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

    # TestCase Builder
    def test_builder(self):
        monster_builder = MonsterBuilder()

        monster_builder.set_builder(ZombieBuilder())
        instance_a = monster_builder.get_monster()

        monster_builder.set_builder(SkeletonBuilder())
        instance_b = monster_builder.get_monster()

        self.assertTrue('dirty and rotten' in instance_a.describre())
        self.assertTrue('skull' in instance_b.describre())

    # TestCase Prototype
    def test_prototype(self):
        MonsterPrototypeFactory.initialize()

        instance_a = MonsterPrototypeFactory.get_zombie()
        instance_b = MonsterPrototypeFactory.get_skeleton()

        self.assertTrue('dirty and rotten' in instance_a.describre())
        self.assertTrue('skull' in instance_b.describre())


if __name__ == '__main__':
    unittest.main()

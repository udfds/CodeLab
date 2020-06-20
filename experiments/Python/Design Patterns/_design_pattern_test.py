import unittest

from singleton import Singleton
from factory import EntityFactory
from builder import ZombieBuilder
from builder import SkeletonBuilder
from builder import MonsterBuilder
from prototype import MonsterPrototypeFactory
from adapter import SkeletonAdapter
from adapter import BeastAdapter
from adapter import MiniBossAdapter
from adapter import BossAdapter
from proxy import Dungeon
from proxy import ProxyDungeon
from state import CityPortal
from state import MainCity
from state import MarineCity
from state import SkyCity


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

    # TestCase Adapter
    def test_adapter(self):
        skeleton = SkeletonAdapter()
        beast = BeastAdapter()

        mini_boss = MiniBossAdapter()
        boss = BossAdapter()

        mini_boss.set_adapter(skeleton)
        self.assertTrue(mini_boss.attack() == 20)
        self.assertTrue(mini_boss.live() == 1000)

        mini_boss.set_adapter(beast)
        self.assertTrue(mini_boss.attack() == 100)
        self.assertTrue(mini_boss.live() == 2500)

        boss.set_adapter(skeleton)
        self.assertTrue(boss.attack() == 50)
        self.assertTrue(boss.live() == 10000)

        boss.set_adapter(beast)
        self.assertTrue(boss.attack() == 250)
        self.assertTrue(boss.live() == 25000)

    # TestCase Proxy
    def test_proxy(self):
        instance_a = ProxyDungeon(Dungeon('Instance 1'))
        instance_b = ProxyDungeon(Dungeon('Instance 2'))

        self.assertTrue('Building' in instance_a.show_dungeon())
        self.assertTrue('Dungeon' in instance_a.show_dungeon())
        self.assertTrue('Building' in instance_b.show_dungeon())
        self.assertTrue('Dungeon' in instance_b.show_dungeon())

    # TestCase State
    def test_state(self):
        instance = CityPortal()

        #self.assertTrue('to AnyCity break' in instance.warp('AnyCity'))
        self.assertTrue('to MarineCity done' in instance.warp(MarineCity))
        self.assertTrue('to MarineCity break' in instance.warp(MarineCity))
        self.assertTrue('to MainCity done' in instance.warp(MainCity))
        self.assertTrue('to SkyCity done' in instance.warp(SkyCity))


if __name__ == '__main__':
    unittest.main()

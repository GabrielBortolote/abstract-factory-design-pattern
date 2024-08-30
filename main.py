import random
from typing import List
from factories import (
  FireCreaturesFactory,
  WaterCreaturesFactory,
  EarthCreaturesFactory,
  AirCreaturesFactory,
)
from magical_creatures import MagicalCreature

NUMBER_OF_MONSTER_PER_REGION = 10

class Map:
    def __init__(self):
        self.creatures: List[MagicalCreature] = []

    def populate(self):
        self.populate_fire_regions()
        self.populate_water_regions()
        self.populate_earth_regions()
        self.populate_air_regions()

    def populate_fire_regions(self):
        factory = FireCreaturesFactory()
        creatures = factory.create_magical_creatures(NUMBER_OF_MONSTER_PER_REGION)
        self.creatures += creatures

    def populate_water_regions(self):
        factory = WaterCreaturesFactory()
        creatures = factory.create_magical_creatures(NUMBER_OF_MONSTER_PER_REGION)
        self.creatures += creatures
        pass

    def populate_earth_regions(self):
        factory = EarthCreaturesFactory()
        creatures = factory.create_magical_creatures(NUMBER_OF_MONSTER_PER_REGION)
        self.creatures += creatures

    def populate_air_regions(self):
        factory = AirCreaturesFactory()
        creatures = factory.create_magical_creatures(NUMBER_OF_MONSTER_PER_REGION)
        self.creatures += creatures

    def get_random_creature(self) -> MagicalCreature:
        return random.choice(self.creatures)


if __name__ == '__main__':
    # create and populate with monsters
    map = Map()
    map.populate()

    # get a creature to use as example
    creature = map.get_random_creature()
    creature.attack()
    creature.get_damage()
    creature.runaway()
    

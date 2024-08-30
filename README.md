# Abstract Factory

This project implements a use case for a Design Pattern, the Abstract Factory. To know more about this pattern you can access [this website](https://refactoring.guru/design-patterns/abstract-factory).

## What it is?

The **Abstract Factory**  is a creational design pattern that allows producing families of related or dependent objects without specifying their concrete classes. If you have families and variants of the products, you probably should use Abstract Factory, see the example bellow:

![schema](/example.png)

This is the schema of a Abstract Factory pattern:

![schema](/abstract-factory-schema.png)

Note that there'are two inheritances happening. The **Product** inheritance and the **Factory** inheritance, one of them represents the family and another one the variant.

- Abstract Products declare interfaces for a set of distinct but related products which make up a product **family**.
- Concrete Factories implement creation methods of the abstract factory. Each concrete factory corresponds to a specific **variant** of products and creates only those product variants.

## Project

Let's build a register of magical creatures, they can be:

1. Dragon
2. Monster
3. Elf

All the monster can belong to 4 different variants:

1. Fire;
2. Water;
3. Earth;
4. Air.

Yes, I love fantasy and I'm a ruge fan of Avatar the Last Airbender. Let's build the table:

|       | Dragon      | Monster       | Elf           |
|-------|-------------|---------------|---------------|
| Fire  | Blaze Wurm  | Pyro Beast    | Ember Sprite  |
| Water | Aquazor     | Tidal Tantrum | Mist Mage     |
| Earth | Golem Wyrm  | Terrakin      | GroveGuardian |
| Air   | Gale Wyvern | Wind Wraith   | Sky Sylph     |

Now, let's suppose that we are creating a map with regions that are full of volcanoes, perfect to Fire magical creatures, there are aquatic regions, like rivers, lakes and sea, perfect to Water magical creatures, regions like deserts and woods, where Earth creatures can live in piece and montains, abisms and another king of very high environments, where Air creatures can adapt better. The **Map** can be a class, and this class is responsible for populating each region with the right type of creatures. So the Map is the client that is going to call the factories, and the products are the creatures.

Let's start implementing some client code:

```python
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
```

Now we need to implement the missing Factories, all of them need a method *create_magical_creatures* returning the creatures were created:

```python
from abc import ABC, abstractmethod

class MagicalCreatureFactory(ABC):
    @abstractmethod
    def create_magical_creatures(n: int) -> list:
        pass

class FireCreaturesFactory(MagicalCreatureFactory):
    def create_magical_creatures(n: int) -> list:
        created_magical_creatures = []
        for _ in range(0, n):
            blazeWurm = BlazeWurm()
            pyroBeast = PyroBeast()
            emberSpreite = EmberSprite()
            created_magical_creatures += [blazeWurm, pyroBeast, emberSpreite]
        return created_magical_creatures
    
class WaterCreaturesFactory(MagicalCreatureFactory):
    def create_magical_creatures(n: int) -> list:
        created_magical_creatures = []
        for _ in range(0, n):
            aquazor = Aquazor()
            tidalTantrum = TidalTantrum()
            groveGuardian = GroveGuardian()
            created_magical_creatures += [aquazor, tidalTantrum, groveGuardian]
        return created_magical_creatures
    
class EarthCreaturesFactory(MagicalCreatureFactory):
    def create_magical_creatures(n: int) -> list:
        created_magical_creatures = []
        for _ in range(0, n):
            golemWyrm = golemWyrm()
            terrakin = terrakin()
            groveGuardian = groveGuardian()
            created_magical_creatures += [golemWyrm, terrakin, groveGuardian]
        return created_magical_creatures
    
class AirCreaturesFactory(MagicalCreatureFactory):
    def create_magical_creatures(n: int) -> list:
        created_magical_creatures = []
        for _ in range(0, n):
            galeWyvern = GaleWyvern()
            windWraith = WindWraith()
            skySylph = SkySylph()
            created_magical_creatures += [galeWyvern, windWraith, skySylph]
        return created_magical_creatures

```

As you can see, each factory creates only creatures to a specific type of region. Now we need to create the magical creatures classes:

```python
class MagicalCreature():
  def __init__(self):
    self.name = 'Default Creature'

  def attack(self):
    print(f'{self.name} attacking')

  def runaway(self):
    print(f'{self.name} running away')

  def get_damage(self):
    print(f'{self.name} got damage')

class BlazeWurm(MagicalCreature):
  def __init__(self):
    self.name = 'Blaze Wurm'

class PyroBeast(MagicalCreature):
  def __init__(self):
    self.name = 'Pyto Beast'

class EmberSprite(MagicalCreature):
  def __init__(self):
    self.name = 'Ember Sprite'

class Aquazor(MagicalCreature):
  def __init__(self):
    self.name = 'Aquazor'

class TidalTantrum(MagicalCreature):
  def __init__(self):
    self.name = 'Tidal Tantrum'

class GolemWyrm(MagicalCreature):
  def __init__(self):
    self.name = 'Golem Wyrm'

class Terrakin(MagicalCreature):
  def __init__(self):
    self.name = 'Terrakin'

class GroveGuardian(MagicalCreature):
  def __init__(self):
    self.name = 'Grove Guardian'

class GaleWyvern(MagicalCreature):
  def __init__(self):
    self.name = 'Gale Wyvern'

class WindWraith(MagicalCreature):
  def __init__(self):
    self.name = 'Wind Wraith'

class SkySylph(MagicalCreature):
  def __init__(self):
    self.name = 'Sky Sylph'
```

As you can see, all the magical creatures has the same methods, they can attack, runaway or get damage, all of them have a common attribute, the *name* attribute, and we can easily customize the method inside each creatures. If we want *Gale Wyvern* to attack in a different way, we can overwrite the method attack inside the class *GaleWyvern*. The same way we can create specific methods to specific creatures.

Now we can execute the *main.py* module to see what happens:

```bash
python main.py 
Gale Wyvern attacking
Gale Wyvern got damage
Gale Wyvern running away
```

In every execution the Map is going to be populated, a random creature is going to be selected and their execution methods are going to be called. We successfully implemented factories to populate specific regions in the map with the right variant of creatures and we easily created 12 different creatures reusing the same code.

This is the power of an Abstract Factory.

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

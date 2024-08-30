from abc import ABC, abstractmethod
from magical_creatures import (
    BlazeWurm,
    PyroBeast,
    EmberSprite,
    Aquazor,
    TidalTantrum,
    GolemWyrm,
    Terrakin,
    GroveGuardian,
    GaleWyvern,
    WindWraith,
    SkySylph,
)

class MagicalCreatureFactory(ABC):
    @abstractmethod
    def create_magical_creatures(self, n: int) -> list:
        pass

class FireCreaturesFactory(MagicalCreatureFactory):
    def create_magical_creatures(self, n: int) -> list:
        created_magical_creatures = []
        for _ in range(0, n):
            blazeWurm = BlazeWurm()
            pyroBeast = PyroBeast()
            emberSpreite = EmberSprite()
            created_magical_creatures += [blazeWurm, pyroBeast, emberSpreite]
        return created_magical_creatures
    
class WaterCreaturesFactory(MagicalCreatureFactory):
    def create_magical_creatures(self, n: int) -> list:
        created_magical_creatures = []
        for _ in range(0, n):
            aquazor = Aquazor()
            tidalTantrum = TidalTantrum()
            groveGuardian = GroveGuardian()
            created_magical_creatures += [aquazor, tidalTantrum, groveGuardian]
        return created_magical_creatures
    
class EarthCreaturesFactory(MagicalCreatureFactory):
    def create_magical_creatures(self, n: int) -> list:
        created_magical_creatures = []
        for _ in range(0, n):
            golemWyrm = GolemWyrm()
            terrakin = Terrakin()
            groveGuardian = GroveGuardian()
            created_magical_creatures += [golemWyrm, terrakin, groveGuardian]
        return created_magical_creatures
    
class AirCreaturesFactory(MagicalCreatureFactory):
    def create_magical_creatures(self, n: int) -> list:
        created_magical_creatures = []
        for _ in range(0, n):
            galeWyvern = GaleWyvern()
            windWraith = WindWraith()
            skySylph = SkySylph()
            created_magical_creatures += [galeWyvern, windWraith, skySylph]
        return created_magical_creatures

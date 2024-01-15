from .Daily import *
from .Explore import *
from .Other import *
from .Story import *
from .Town import *
from .Yard import *

from hiworker import Coordinate, InitImage


class Detect(DetectInvite, DetectBattle, DetectBossAttack, DetectBossDefense, DetectDaily, DetectDraftDuel, DetectDuel, DetectEncounter,
             DetectGuildFeast,
             DetectGymnasium, DetectNetherworldGate, DetectRoyalBattle, DetectAreaBoss, DetectBonus, DetectChapter, DetectDelegate,
             DetectEvoMaterials, DetectExplore, DetectHeianStories, DetectHeianTales, DetectRealmRaid, DetectSecretZone, DetectSouls,
             DetectTotem, DetectDemonParade, DetectTown, DetectCollection, DetectEarthly, DetectFriend, DetectGuild, DetectMall,
             DetectOnmyoji, DetectPet, DetectShikigami, DetectSummon, DetectFlowerFight, DetectYard, DetectGameOnStart,
             DetectBountySeals, DetectIllustratedHandbook, DetectStory, DetectTeam):
    def __init__(self):
        super(Detect, self).__init__()

from .Daily import *
from .Explore import *
from .Other import *
from .Story import *
from .Town import *
from .Yard import *
from hiworker import Coordinate


class Operate(OperateInvite, OperateBattle, OperateBossAttack, OperateBossDefense, OperateDaily, OperateDraftDuel, OperateDuel,
              OperateEncounter,
              OperateGuildFeast,
              OperateGymnasium, OperateNetherworldGate, OperateRoyalBattle, OperateAreaBoss, OperateBonus, OperateChapter, OperateDelegate,
              OperateEvoMaterials, OperateExplore, OperateHeianStories, OperateHeianTales, OperateRealmRaid, OperateSecretZone,
              OperateSouls,
              OperateTotem, OperateDemonParade, OperateTown, OperateCollection, OperateEarthly, OperateFriend, OperateGuild, OperateMall,
              OperateOnmyoji, OperatePet, OperateShikigami, OperateSummon, OperateFlowerFight, OperateYard, OperateTeam,
              OperateGameOnStart,
              OperateBountySeals, OperateIllustratedHandbook, OperateStory):
    def __init__(self):
        super(Operate, self).__init__()

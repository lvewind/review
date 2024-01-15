from . import *


class Play:
    def __init__(self, play_input: PlayInput):
        self.boss_attack = PlayBossAttack(play_input)
        self.boss_defense = PlayBossDefense(play_input)
        self.draft_duel = PlayDraftDuel(play_input)
        self.duel = PlayDuel(play_input)
        self.encounter = PlayEncounter(play_input)
        self.guild_feast = PlayGuildFeast(play_input)
        self.gymnasium = PlayGymnasium(play_input)
        self.netherworld_gate = PlayNetherworldGate(play_input)
        self.royal_battle = PlayRoyalBattle(play_input)

        self.area_boss = PlayAreaBoss(play_input)

        self.delegate = PlayDelegate(play_input)

        self.heian_stories = PlayHeianStories(play_input)
        self.heian_tales = PlayHeianTales(play_input)
        self.realm_raid = PlayRealmRaid(play_input)
        self.secret_zone = PlaySecretZone(play_input)
        self.totem = PlayTotem(play_input)

        self.chapter = PlayChapter(play_input)
        self.evo_materials = PlayEvoMaterials(play_input)
        self.souls = PlaySouls(play_input)

        self.demon_parade = PlayDemonParade(play_input)

        self.earthly = PlayEarthly(play_input)
        self.mall = PlayMall(play_input)
        self.onmyoji = PlayOnmyoji(play_input)
        self.pet = PlayPet(play_input)
        self.shikigami = PlayShikigami(play_input)
        self.summon = PlaySummon(play_input)
        self.yard = PlayYard(play_input)
        self.flower_fight = PlayFlowerFight(play_input)
        self.friend = PlayFriends(play_input)
        self.share = PlayShare(play_input)
        self.bounty_seals = PlayBountySeals(play_input)

        self.story = PlayStory(play_input)
        self.task_on_start = PlayGameOnStart(play_input)

from typing import Optional, List
from sqlalchemy import ForeignKey, String, Column, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(default="")
    platform: Mapped[str] = mapped_column(default="")
    remember_password: Mapped[int] = mapped_column(default=0)
    change_role: Mapped[int] = mapped_column(default=0)
    teamup_img: Mapped[str] = mapped_column(default="")
    login_img: Mapped[str] = mapped_column(default="")
    record_id: Mapped[str] = mapped_column(default="")


class AppSetting(Base):
    __tablename__ = "app_setting"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(default="")
    onmyoji_pc_path: Mapped[str] = mapped_column(default="")
    emulator_path: Mapped[str] = mapped_column(default="")
    sandbox_path: Mapped[str] = mapped_column(default="")
    scroll_count: Mapped[int] = mapped_column(default=0)
    scroll_time: Mapped[int] = mapped_column(default=0)
    cpu_sleep_time: Mapped[int] = mapped_column(default=0)
    offset_x: Mapped[int] = mapped_column(default=0)
    offset_y: Mapped[int] = mapped_column(default=0)
    record_id: Mapped[str] = mapped_column(default="")


class CounterRecord(Base):
    __tablename__ = "counter_record"

    id: Mapped[int] = mapped_column(primary_key=True)

    record_id: Mapped[int] = mapped_column(default=0)
    orochi_12: Mapped[int] = mapped_column(default=0)
    orochi_11: Mapped[int] = mapped_column(default=0)
    orochi_10: Mapped[int] = mapped_column(default=0)
    sougenbi: Mapped[int] = mapped_column(default=0)
    himiko: Mapped[int] = mapped_column(default=0)
    chapter: Mapped[int] = mapped_column(default=0)
    totem: Mapped[int] = mapped_column(default=0)
    evo_materials: Mapped[int] = mapped_column(default=0)
    realm_raid_person: Mapped[int] = mapped_column(default=0)
    realm_raid_guild: Mapped[int] = mapped_column(default=0)
    real_orochi: Mapped[int] = mapped_column(default=0)
    demon_seal: Mapped[int] = mapped_column(default=0)
    exp_spirit: Mapped[int] = mapped_column(default=0)
    coin_spirit: Mapped[int] = mapped_column(default=0)
    nen: Mapped[int] = mapped_column(default=0)
    kraken: Mapped[int] = mapped_column(default=0)
    lot: Mapped[int] = mapped_column(default=0)
    get_jade: Mapped[int] = mapped_column(default=0)
    get_ap: Mapped[int] = mapped_column(default=0)
    get_mail: Mapped[int] = mapped_column(default=0)
    get_guild_pack: Mapped[int] = mapped_column(default=0)
    get_bonus: Mapped[int] = mapped_column(default=0)
    talisman_pass: Mapped[int] = mapped_column(default=0)
    free_summon: Mapped[int] = mapped_column(default=0)
    pet: Mapped[int] = mapped_column(default=0)
    friendship_point: Mapped[int] = mapped_column(default=0)
    guild_task: Mapped[int] = mapped_column(default=0)
    guild_coin: Mapped[int] = mapped_column(default=0)
    guild_mall: Mapped[int] = mapped_column(default=0)
    guild_contribute: Mapped[int] = mapped_column(default=0)
    guild_realm: Mapped[int] = mapped_column(default=0)
    guild_foster: Mapped[int] = mapped_column(default=0)
    encounter: Mapped[int] = mapped_column(default=0)
    gymnasium: Mapped[int] = mapped_column(default=0)
    boss_attack: Mapped[int] = mapped_column(default=0)
    duel: Mapped[int] = mapped_column(default=0)
    draft_duel: Mapped[int] = mapped_column(default=0)
    royal_battle: Mapped[int] = mapped_column(default=0)
    boss_defense: Mapped[int] = mapped_column(default=0)
    netherworld_gate: Mapped[int] = mapped_column(default=0)
    guild_feast: Mapped[int] = mapped_column(default=0)
    area_boss: Mapped[int] = mapped_column(default=0)
    demon_parade: Mapped[int] = mapped_column(default=0)
    upgrade_star: Mapped[int] = mapped_column(default=0)
    upgrade_level: Mapped[int] = mapped_column(default=0)
    illustrated_share: Mapped[int] = mapped_column(default=0)
    normal_scale: Mapped[int] = mapped_column(default=0)
    gift_lot: Mapped[int] = mapped_column(default=0)
    honor_mall: Mapped[int] = mapped_column(default=0)
    medal_mall: Mapped[int] = mapped_column(default=0)
    side_bet: Mapped[int] = mapped_column(default=0)


class DemonParade(Base):
    __tablename__ = "demon_parade"

    id: Mapped[int] = mapped_column(primary_key=True)

    shikigami: Mapped[str] = mapped_column(default="")


class PlanProductAssociation(Base):
    __tablename__ = "plan_product_association"

    id: Mapped[int] = mapped_column(primary_key=True)
    plan_id: Mapped[int] = mapped_column(ForeignKey("plan.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))

    sort_order: Mapped[int] = mapped_column(default="0")

    product: Mapped[List["Product"]] = relationship(back_populates="plan_association")
    plan: Mapped["Plan"] = relationship(back_populates="product_association")


class Plan(Base):
    __tablename__ = "plan"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(default="")
    close_env: Mapped[int] = mapped_column(default=0)
    timing_start: Mapped[int] = mapped_column(default=0)

    product_association: Mapped[List["PlanProductAssociation"]] = relationship(back_populates="plan")


class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(default="")
    play_name: Mapped[str] = mapped_column(default="")
    play_name_second: Mapped[str] = mapped_column(default="")
    chapter_stage: Mapped[int] = mapped_column(default=0)
    preset_count: Mapped[int] = mapped_column(default=0)
    approximate_count: Mapped[int] = mapped_column(default=0)

    bonus_soul: Mapped[int] = mapped_column(default=0)
    bonus_evo: Mapped[int] = mapped_column(default=0)
    bonus_coin_50: Mapped[int] = mapped_column(default=0)
    bonus_coin_100: Mapped[int] = mapped_column(default=0)
    bonus_exp_50: Mapped[int] = mapped_column(default=0)
    bonus_exp_100: Mapped[int] = mapped_column(default=0)

    chapter_spirit_exp: Mapped[int] = mapped_column(default=0)
    chapter_spirit_coin: Mapped[int] = mapped_column(default=0)
    chapter_spirit_gift: Mapped[int] = mapped_column(default=0)
    chapter_map_seal: Mapped[int] = mapped_column(default=0)
    chapter_map_gift: Mapped[int] = mapped_column(default=0)

    dog_food_n: Mapped[int] = mapped_column(default=0)
    dog_food_m: Mapped[int] = mapped_column(default=0)
    use_yingbing: Mapped[int] = mapped_column(default=0)
    lock_cast: Mapped[int] = mapped_column(default=0)
    encounter_boss: Mapped[int] = mapped_column(default=0)
    gymnasium_only_watch: Mapped[int] = mapped_column(default=0)
    gymnasium_mass: Mapped[int] = mapped_column(default=0)

    chapter_dog_food_n: Mapped[int] = mapped_column(default=0)
    chapter_dog_food_m: Mapped[int] = mapped_column(default=0)
    chapter_2v2: Mapped[int] = mapped_column(default=0)
    chapter_1v3: Mapped[int] = mapped_column(default=0)
    chapter_0v3: Mapped[int] = mapped_column(default=0)
    chapter_1v2: Mapped[int] = mapped_column(default=0)
    chapter_0v0: Mapped[int] = mapped_column(default=0)
    chapter_dog_food_2: Mapped[int] = mapped_column(default=0)
    chapter_dog_food_3: Mapped[int] = mapped_column(default=0)
    chapter_dog_food_4: Mapped[int] = mapped_column(default=0)

    guild_mall_grade_daruma: Mapped[int] = mapped_column(default=0)
    guild_mall_souls: Mapped[int] = mapped_column(default=0)
    guild_mall_amulet: Mapped[int] = mapped_column(default=0)
    guild_mall_skill_daruma: Mapped[int] = mapped_column(default=0)
    guild_mall_skin_ticket: Mapped[int] = mapped_column(default=0)
    guild_mall_yingbing: Mapped[int] = mapped_column(default=0)

    story_buy_ap: Mapped[int] = mapped_column(default=0)
    story_realm_raid: Mapped[int] = mapped_column(default=0)
    battle_failed_stop: Mapped[int] = mapped_column(default=0)
    ap_use_up_close_game: Mapped[int] = mapped_column(default=0)
    ap_use_up_restart: Mapped[int] = mapped_column(default=0)

    guild_coin: Mapped[int] = mapped_column(default=0)
    guild_contribute: Mapped[int] = mapped_column(default=0)
    guild_invocation: Mapped[int] = mapped_column(default=0)
    guild_task: Mapped[int] = mapped_column(default=0)
    guild_task_contribute: Mapped[int] = mapped_column(default=0)
    realm_ap: Mapped[int] = mapped_column(default=0)
    guild_foster_m: Mapped[int] = mapped_column(default=0)
    guild_foster_n: Mapped[int] = mapped_column(default=0)
    cultivate_m: Mapped[int] = mapped_column(default=0)
    cultivate_n: Mapped[int] = mapped_column(default=0)
    record_id: Mapped[str] = mapped_column(default="")
    counter_item: Mapped[str] = mapped_column(default="")

    plan_association: Mapped[List["PlanProductAssociation"]] = relationship(back_populates="product")


class PlanRecord(Base):
    __tablename__ = "plan_record"

    id: Mapped[int] = mapped_column(primary_key=True)
    record_id: Mapped[str] = mapped_column(default="")
    finish_status: Mapped[int] = mapped_column(default=0)


class RunEnv(Base):
    __tablename__ = "run_env"

    id: Mapped[int] = mapped_column(primary_key=True)
    em_id: Mapped[int] = mapped_column(default=0)
    name: Mapped[str] = mapped_column(default="")
    env_type: Mapped[int] = mapped_column(default=1)
    status: Mapped[int] = mapped_column(default=0)
    record_id: Mapped[str] = mapped_column(default="")


class RunList(Base):
    __tablename__ = "run_list"

    id: Mapped[int] = mapped_column(primary_key=True)
    run_mode: Mapped[int] = mapped_column(default=1)
    teamup_mode: Mapped[str] = mapped_column(default="single_solo")
    teammate_type: Mapped[int] = mapped_column(default=1)

    run_env_id: Mapped[int] = mapped_column(default=0)

    account_id: Mapped[int] = mapped_column(default=0)

    teammate_id: Mapped[int] = mapped_column(default=0)

    plan_id: Mapped[int] = mapped_column(default=0)

    run_status: Mapped[int] = mapped_column(default=0)
    run_time: Mapped[int] = mapped_column(default=0)
    record_id: Mapped[str] = mapped_column(default="")
    timing_start: Mapped[int] = mapped_column(default=0)


class RunStatus(Base):
    __tablename__ = "run_status"
    id: Mapped[int] = mapped_column(primary_key=True)
    record_id: Mapped[str] = mapped_column(default="")


class TaskRecord(Base):
    __tablename__ = "task_record"

    id: Mapped[int] = mapped_column(primary_key=True)
    record_id: Mapped[str] = mapped_column(default="")
    finish_status: Mapped[int] = mapped_column(default=0)
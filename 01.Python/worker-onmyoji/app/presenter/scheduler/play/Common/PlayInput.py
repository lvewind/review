from typing import Union


class PlayInput:
    def __init__(self, executor_data):
        self.run_list = RunList(executor_data)
        self.run_env = RunEnv(executor_data.get("run_env"))
        self.account = Account(executor_data.get("account"))
        self.app_setting = AppSetting(executor_data.get("app_setting"))
        self.teammate = RunList(executor_data.get("teammate"))
        self.teammate_account = Account(executor_data.get("teammate_account"))
        self.plan = Plan(executor_data.get("plan"))
        self.products = []
        for product in executor_data.get("products"):
            self.products.append(Product(product))

        self.task_record_id = ""
        self.teammate_task_record_id = ""

        self.current_product: Union[Product, None] = None


class RunList:
    def __init__(self, data: dict):
        self.id = 0
        self.run_mode = 0
        self.teamup_mode = ""
        self.teammate_type = 0
        self.run_env_id = 0
        self.account_id = 0
        self.teammate_id = 0
        self.plan_id = 0
        self.run_status = 0
        self.run_time = 0
        self.record_id = 0
        self.timing_start = 0
        for key, value in data.items():
            setattr(self, key, value)


class RunEnv:
    def __init__(self, data: dict):
        self.id = 0
        self.em_id = 0
        self.name = ""
        self.env_type = ""
        self.status = 0
        self.record_id = ""
        for key, value in data.items():
            setattr(self, key, value)


class Plan:
    def __init__(self, data: dict):
        self.id = 0
        self.name = ""
        self.close_env = 0
        for key, value in data.items():
            setattr(self, key, value)


class Product:
    def __init__(self, data: dict):
        self.id = 0
        self.play_name = ""
        self.play_name_second = ""
        self.counter_item = ""
        self.chapter_stage = 0
        self.preset_count = 0
        self.approximate_count = False

        self.lock_cast = False
        self.use_yingbing = False

        self.bonus_soul = False
        self.bonus_evo = False
        self.bonus_exp_100 = False
        self.bonus_exp_50 = False
        self.bonus_coin_100 = False
        self.bonus_coin_50 = False

        self.chapter_spirit_exp = False
        self.chapter_spirit_coin = False
        self.chapter_spirit_gift = False
        self.chapter_map_seal = False
        self.chapter_map_gift = False

        self.chapter_2v2 = False
        self.chapter_1v3 = False
        self.chapter_0v3 = False
        self.chapter_1v2 = False
        self.chapter_0v0 = False

        self.chapter_dog_food_n = False
        self.chapter_dog_food_m = False
        self.chapter_dog_food_2 = False
        self.chapter_dog_food_3 = False
        self.chapter_dog_food_4 = False

        self.encounter_boss = False

        self.guild_mall_grade_daruma = False
        self.guild_mall_souls = False
        self.guild_mall_amulet = False
        self.guild_mall_skill_daruma = False
        self.guild_mall_skin_ticket = False
        self.guild_mall_yingbing = False

        self.gymnasium_only_watch = False
        self.gymnasium_mass = False

        self.story_buy_ap = False
        self.story_realm_raid = False
        self.battle_failed_stop = False
        self.ap_use_up_close_game = False
        self.ap_use_up_restart = False

        self.guild_coin = False
        self.guild_contribute = False
        self.guild_invocation = False
        self.guild_task = False
        self.guild_task_contribute = False
        self.realm_ap = False

        self.guild_foster_m = False
        self.guild_foster_n = False
        self.cultivate_m = False
        self.cultivate_n = False

        for key, value in data.items():
            setattr(self, key, value)


class Account:
    def __init__(self, data: dict):
        self.id = 0
        self.name = ""
        self.platform = ""
        self.remember_password = ""
        self.change_role = ""
        self.teamup_img = ""
        self.login_img = ""
        self.record_id = ""

        for key, value in data.items():
            setattr(self, key, value)


class AppSetting:
    def __init__(self, data: dict):
        self.id = 0
        self.name = ""
        self.onmyoji_pc_path = ""
        self.emulator_path = ""
        self.sandbox_path = ""
        self.scroll_count = 0
        self.scroll_time = 0
        self.cpu_sleep_time = 0
        self.record_id = ""
        self.offset_x = 0
        self.offset_y = 0

        for key, value in data.items():
            setattr(self, key, value)

class TableSetting:
    def __init__(self):
        self.run_list = {
            "id": {"col": 0, "header_name": "ID", "width": 40, "extend": None},
            "env_name": {"col": 1, "header_name": "机器", "width": 70},
            "account": {"col": 2, "header_name": "客户", "width": 70},
            "run_mode": {"col": 3, "header_name": "模式", "width": 40, "extend": None},
            "teamup_mode": {"col": 4, "header_name": "队伍", "width": 70, "extend": None},
            "teammate": {"col": 5, "header_name": "队员", "width": 80},
            "plan": {"col": 6, "header_name": "计划", "width": 140},
            "current_product": {"col": 7, "header_name": "当前任务", "width": 140, "extend": None},
            "current_scene": {"col": 8, "header_name": "当前场景", "width": 60, "extend": None},
            "current_operation": {"col": 9, "header_name": "当前操作", "width": 110, "extend": None},
            "run_time": {"col": 10, "header_name": "时间", "width": 60, "is_time": True, "extend": None}
        }

        self.run_list_set_plan = {
            "id": {"col": 0, "header_name": "ID", "width": 40},
            "name": {"col": 1, "header_name": "计划名称", "width": 180},
            "timing_start": {"col": 2, "header_name": "定时", "width": 60, "is_time": True}
        }

        self.run_count = {
            "name": {"col": 0, "header_name": "产品名", "width": 40},
            "counter": {"col": 1, "header_name": "产量", "width": 40}
        }

        self.run_count_row = {
            "orochi_12": {"row": 0, "row_name": "天罚"},
            "orochi_11": {"row": 1, "row_name": "悲鸣"},
            "orochi_10": {"row": 2, "row_name": "魂十"},
            "sougenbi": {"row": 3, "row_name": "业原火"},
            "himiko": {"row": 4, "row_name": "卑弥呼"},
            "chapter": {"row": 5, "row_name": "狗粮"},
            "totem": {"row": 6, "row_name": "御灵"},
            "evo_materials": {"row": 7, "row_name": "觉醒"},
            "realm_raid_person": {"row": 8, "row_name": "突破"},
            "realm_raid_guild": {"row": 9, "row_name": "寮突"},
            "real_orochi": {"row": 10, "row_name": "真蛇"},

            "demon_seal": {"row": 11, "row_name": "妖气"},
            "exp_spirit": {"row": 12, "row_name": "经验妖"},
            "coin_spirit": {"row": 13, "row_name": "金币妖"},
            "nen": {"row": 14, "row_name": "年兽"},
            "kraken": {"row": 15, "row_name": "石距"},

            "lot": {"row": 16, "row_name": "签到"},
            "get_jade": {"row": 17, "row_name": "领勾玉"},
            "get_ap": {"row": 18, "row_name": "领体力"},
            "get_mail": {"row": 19, "row_name": "邮件"},
            "get_guild_pack": {"row": 20, "row_name": "领寮包"},
            "get_bonus": {"row": 21, "row_name": "领加成"},
            "talisman_pass": {"row": 22, "row_name": "花合战"},

            "free_summon": {"row": 23, "row_name": "每日抽"},
            "pet": {"row": 24, "row_name": "宠物"},
            "friendship_point": {"row": 25, "row_name": "友情点"},

            "guild_task": {"row": 26, "row_name": "寮任务"},
            "guild_coin": {"row": 27, "row_name": "寮金币"},
            "guild_mall": {"row": 28, "row_name": "寮商店"},
            "guild_contribute": {"row": 29, "row_name": "寮捐赠"},
            "guild_realm": {"row": 30, "row_name": "寮结界"},
            "guild_foster": {"row": 31, "row_name": "寮寄养"},

            "encounter": {"row": 32, "row_name": "逢魔"},
            "gymnasium": {"row": 33, "row_name": "道馆"},
            "boss_attack": {"row": 34, "row_name": "麒麟"},
            "duel": {"row": 35, "row_name": "斗技"},
            "draft_duel": {"row": 36, "row_name": "协同"},
            "royal_battle": {"row": 37, "row_name": "百鬼奕"},
            "boss_defense": {"row": 38, "row_name": "退治"},
            "netherworld_gate": {"row": 39, "row_name": "阴门"},
            "guild_feast": {"row": 40, "row_name": "宴会"},

            "area_boss": {"row": 41, "row_name": "地鬼"},
            "demon_parade": {"row": 42, "row_name": "夜行"},
            "upgrade_star": {"row": 43, "row_name": "升星"},
            "upgrade_level": {"row": 44, "row_name": "升级"},
            "illustrated_share": {"row": 45, "row_name": "图鉴"},
            "normal_scale": {"row": 46, "row_name": "紫蛇皮"},
            "gift_lot": {"row": 47, "row_name": "礼包签"},
            "honor_mall": {"row": 48, "row_name": "荣誉点"},
            "medal_mall": {"row": 49, "row_name": "勋章"},
            "side_bet": {"row": 50, "row_name": "竞猜"}
        }

        self.table_quick = {
            "id": {"col": 0, "header_name": "ID", "width": 40},
            "name": {"col": 1, "header_name": "名称", "width": 180}
        }

        self.products = {
            "id": {"col": 0, "header_name": "ID", "width": 40},
            "name": {"col": 1, "header_name": "名称", "width": 190},
            "play_name": {"col": 2, "header_name": "内容", "width": 70},
            "play_name_second": {"col": 3, "header_name": "子项", "width": 70},
            "chapter_stage": {"col": 4, "header_name": "难度", "width": 60},
            "preset_count": {"col": 5, "header_name": "任务量", "width": 0},
            "lock_cast": {"col": 6, "header_name": "锁阵容", "width": 0, "is_bool": True},
            "bonus_soul": {"col": 7, "header_name": "御魂", "width": 0, "is_bool": True},
            "bonus_evo": {"col": 8, "header_name": "觉醒", "width": 0, "is_bool": True},
            "bonus_coin_50": {"col": 9, "header_name": "五十金", "width": 0, "is_bool": True},
            "bonus_coin_100": {"col": 10, "header_name": "一百金", "width": 0, "is_bool": True},
            "bonus_exp_50": {"col": 11, "header_name": "五十经", "width": 0, "is_bool": True},
            "bonus_exp_100": {"col": 12, "header_name": "一百经", "width": 0, "is_bool": True}
        }

        self.plan = {
            "id": {"col": 0, "header_name": "ID", "width": 40},
            "name": {"col": 1, "header_name": "计划名称", "width": 200},
            "close_env": {"col": 2, "header_name": "下班清场", "width": 80, "is_bool": True},
            "timing_start": {"col": 3, "header_name": "定时启动", "width": 80, "is_time": True}
        }

        self.plan_sub = {
            "sort_order": {"col": 0, "header_name": "排序", "width": 40},
            "assoc_id": {"col": 1, "header_name": "ID", "width": 40},
            "name": {"col": 2, "header_name": "产品名称", "width": 320}
        }

        self.plan_sub_add = {
            "id": {"col": 0, "header_name": "ID", "width": 40},
            "name": {"col": 1, "header_name": "产品名称", "width": 360}
        }

        self.account = {
            "id": {"col": 0, "header_name": "ID", "width": 40},
            "name": {"col": 1, "header_name": "账号名称", "width": 190},
            "platform": {"col": 2, "header_name": "账号平台", "width": 60},
            "remember_password": {"col": 3, "header_name": "免密登录", "width": 60, "is_bool": True},
            "change_role": {"col": 4, "header_name": "登录重选角色", "width": 90, "is_bool": True},
            "teamup_img": {"col": 5, "header_name": "组队图片", "width": 190},
            "login_img": {"col": 6, "header_name": "登陆图片", "width": 190}
        }

        self.account_ = {
            "id": {"col": 0, "header_name": "ID", "width": 40},
            "name": {"col": 1, "header_name": "账号名称", "width": 240}
        }

        self.emulator_list = {
            "id": {"col": 0, "header_name": "ID", "width": 40},
            "name": {"col": 1, "header_name": "模拟器名称", "width": 190}
        }

        self.sandbox_list = {
            "id": {"col": 0, "header_name": "ID", "width": 40},
            "name": {"col": 1, "header_name": "sandbox名称", "width": 190}
        }

        self.set_env = {
            "id": {"col": 0, "header_name": "ID", "width": 40},
            "env_type": {"col": 1, "header_name": "类型", "width": 60},
            "name": {"col": 2, "header_name": "名称", "width": 180}
        }

        self.teammate_list = {
            "run_id": {"col": 0, "header_name": "运行ID", "width": 80},
            "account_id": {"col": 1, "header_name": "账号ID", "width": 80},
            "account_name": {"col": 2, "header_name": "好友名称", "width": 120}
        }


table_setting = TableSetting()

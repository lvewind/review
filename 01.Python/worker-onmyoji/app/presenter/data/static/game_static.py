class DataStatic:
    def __init__(self):
        self.env_type = {
            "1": "sandbox",
            "2": "emulator"
        }

        self.month_data = {"1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七",
                           "8": "八", "9": "九", "10": "十", "11": "十一", "12": "十二", "13": "十三",
                           "14": "十四", "15": "十五", "16": "十六", "17": "十七", "18": "十八", "19": "十九",
                           "20": "二十", "21": "二十一", "22": "二十二", "23": "二十三", "24": "二十四", "25": "二十五",
                           "26": "二十六", "27": "二十七", "28": "二十八", "29": "二十九", "30": "三十", "31": "三十一"
                           }

        self.week_data = {"1": "周一", "2": "周二", "3": "周三", "4": "周四", "5": "周五", "6": "周六", "7": "周日"
                          }

        self.teammate_type = {
            "0": "default",
            "1": "friend",
            "3": "guild",
            "4": "recent",
            "5": "cross"
        }

        self.products = {
            "souls": {
                "name": "御魂",
                "zone": {
                    "orochi": {
                        "name": "八岐大蛇",
                        "stage": {
                            "12": "神罚",
                            "11": "悲鸣",
                            "10": "十层",
                            "9": "九层",
                            "8": "八层",
                            "7": "七层",
                            "6": "六层",
                            "5": "五层",
                            "4": "四层",
                            "3": "三层",
                            "2": "二层",
                            "1": "一层",
                        }
                    },
                    "sougenbi": {
                        "name": "业原火",
                        "stage": {"3": "痴之卷",
                                  "2": "嗔之卷",
                                  "1": "贪之卷"
                                  },
                    },
                    "himiko": {
                        "name": "卑弥呼",
                        "stage": {"3": "三层",
                                  "2": "二层",
                                  "1": "一层"}
                    },
                }
            },
            "chapter": {"name": "狗粮",
                        "zone": {
                            "hard": {
                                "name": "困难",
                                "stage": {
                                    "28": "二十八层",
                                    "27": "二十七层",
                                    "26": "二十六层",
                                    "25": "二十五层",
                                    "24": "二十四层",
                                    "23": "二十三层",
                                    "22": "二十二层",
                                    "21": "二十一层",
                                    "20": "二十层",
                                    "19": "十九层",
                                    "18": "十八层",
                                    "17": "十七层",
                                    "16": "十六层",
                                    "15": "十五层",
                                    "14": "十四层",
                                    "13": "十三层",
                                    "12": "十二层",
                                    "11": "十一层",
                                    "10": "十层",
                                    "9": "九层",
                                    "8": "八层",
                                    "7": "七层",
                                    "6": "六层",
                                    "5": "五层",
                                    "4": "四层",
                                    "3": "三层",
                                    "2": "二层",
                                    "1": "一层",
                                    "999": "剧情自动"
                                }},
                            "simple": {
                                "name": "简单",
                                "stage": {
                                    "28": "二十八层",
                                    "27": "二十七层",
                                    "26": "二十六层",
                                    "25": "二十五层",
                                    "24": "二十四层",
                                    "23": "二十三层",
                                    "22": "二十二层",
                                    "21": "二十一层",
                                    "20": "二十层",
                                    "19": "十九层",
                                    "18": "十八层",
                                    "17": "十七层",
                                    "16": "十六层",
                                    "15": "十五层",
                                    "14": "十四层",
                                    "13": "十三层",
                                    "12": "十二层",
                                    "11": "十一层",
                                    "10": "十层",
                                    "9": "九层",
                                    "8": "八层",
                                    "7": "七层",
                                    "6": "六层",
                                    "5": "五层",
                                    "4": "四层",
                                    "3": "三层",
                                    "2": "二层",
                                    "1": "一层",
                                    "999": "剧情自动"
                                }}
                        },
                        },
            "totem": {
                "name": "御灵",
                "zone": {
                    "an_shen_long": {
                        "name": "暗神龙",
                        "stage": {
                            "3": "三层",
                            "2": "二层",
                            "1": "一层"
                        }},
                    "an_bai_zang_zhu": {
                        "name": "暗白藏主",
                        "stage": {
                            "3": "三层",
                            "2": "二层",
                            "1": "一层"
                        }},
                    "an_hei_bao": {
                        "name": "暗神龙",
                        "stage": {
                            "3": "三层",
                            "2": "二层",
                            "1": "一层"
                        }},
                    "an_kong_que": {
                        "name": "暗孔雀",
                        "stage": {
                            "3": "三层",
                            "2": "二层",
                            "1": "一层"
                        }}
                }},
            "evo_materials": {
                "name": "觉醒",
                "zone": {
                    "fire": {
                        "name": "业火轮",
                        "stage": {
                            "10": "十层",
                            "9": "九层",
                            "8": "八层",
                            "7": "七层",
                            "6": "六层",
                            "5": "五层",
                            "4": "四层",
                            "3": "三层",
                            "2": "二层",
                            "1": "一层",
                        }},
                    "wind": {
                        "name": "风转符",
                        "stage": {
                            "10": "十层",
                            "9": "九层",
                            "8": "八层",
                            "7": "七层",
                            "6": "六层",
                            "5": "五层",
                            "4": "四层",
                            "3": "三层",
                            "2": "二层",
                            "1": "一层",
                        }},
                    "water": {
                        "name": "水灵鲤",
                        "stage": {
                            "10": "十层",
                            "9": "九层",
                            "8": "八层",
                            "7": "七层",
                            "6": "六层",
                            "5": "五层",
                            "4": "四层",
                            "3": "三层",
                            "2": "二层",
                            "1": "一层",
                        }},
                    "thunder": {
                        "name": "天雷鼓",
                        "stage": {
                            "10": "十层",
                            "9": "九层",
                            "8": "八层",
                            "7": "七层",
                            "6": "六层",
                            "5": "五层",
                            "4": "四层",
                            "3": "三层",
                            "2": "二层",
                            "1": "一层",
                        }}
                }},
            "realm_raid": {
                "name": "突破",
                "zone": {
                    "realm_raid_person": {
                        "name": "个人",
                        "stage": {
                            "3": "三层",
                            "6": "六层",
                            "9": "九层",

                        }},
                    "realm_raid_guild": {
                        "name": "寮突",
                        "stage": {
                            "0": "零星",
                            "1": "一星",
                            "2": "二星",
                            "3": "三星",
                            "4": "四星",
                            "5": "五星"
                        }}}
            },
            "yard": {
                "name": "庭院",
                "zone": {
                    "get_lot": {"name": "签到"},
                    "get_mail": {"name": "收取邮件"},
                    "get_bonus": {"name": "获取加成"},
                    "get_jade": {"name": "庭院勾玉"},
                    "get_ap": {"name": "庭院体力"},
                    "talisman_pass": {"name": "花合战"},
                    "friendship_point": {"name": "友情点"},
                    "illustrated_share": {"name": "图鉴分享"}
                }},
            "summon": {
                "name": "召唤",
                "zone": {
                    "summon_free": {"name": "免费一抽"},
                    "summon_normal": {"name": "抽厕纸"},
                    "summon_ten": {"name": "十连抽"}
                }},
            "pet": {
                "name": "宠物小屋",
                "zone": {
                    "play": {"name": "撸猫"},
                    "feed": {"name": "喂狗"},
                    "all": {"name": "撸·喂"},
                }},
            "mall": {
                "name": "商店",
                "zone": {
                    "normal_scale": {"name": "购买紫蛇皮"},
                    "medal_mall": {"name": "勋章商店"},
                    "honor_mall": {"name": "荣誉商店"},
                    "gift_lot": {"name": "礼包屋签到"},
                }},
            "daily": {
                "name": "日常",
                "zone": {
                    "encounter": {"name": "逢魔之时"},
                    "gymnasium": {"name": "道馆"},
                    "duel": {"name": "斗技"},
                    "draft_duel": {"name": "协同对弈"},
                    "royal_battle": {"name": "百鬼奕"},
                    "boss_attack": {"name": "鬼王来袭"},
                    "boss_defense": {"name": "首领退治"},
                    "netherworld_gate": {"name": "阴界之门"},
                    "guild_feast": {"name": "宴会"},
                }},

            "guild": {
                "name": "阴阳寮",
                "zone": {
                    "guild_contribute": {
                        "name": "捐勾玉",
                        "stage": {
                            "100": "一百",
                            "80": "八十",
                            "60": "六十",
                            "40": "四十",
                            "20": "二十"}
                    },
                    "guild_daily": {
                        "name": "寮三十",
                        "stage": {
                            "task_30": "结伴同行",
                            "evo_materials": "提交觉醒材料",
                            "souls": "提交御魂"
                        }, },
                    "guild_mall": {
                        "name": "功勋商店",
                        "zone": {
                            "yingbing": "买樱饼",
                            "grade_daruma": "买白蛋",
                            "souls": "买御魂",
                            "amulet": "买蓝票",
                            "skill_daruma": "买黑蛋皮",
                            "skin_ticket": "买皮肤券"
                        }, },
                }},
            "guild_realm": {
                "name": "寮结界",
                "zone": {
                    "guild_realm_card_setting": {
                        "name": "结界卡配置",
                        "stage": {
                            "taigu": "太鼓",
                            "douyu": "斗鱼",
                            "sanshinei": "伞室内",
                            "taiyinfuzhou": "太阴符咒",
                            "teshubianyi": "特殊变异"}},
                    "guild_realm_card_synthesis": {
                        "name": "结界卡合成",
                        "stage": {
                            "taiyin_1": "太阴·一星",
                            "taiyin_2": "太阴·二星",
                            "taiyin_3": "太阴·三星",
                            "taiyin_4": "太阴·四星",
                            "douyu_1": "斗鱼·一星",
                            "douyu_2": "斗鱼·二星",
                            "douyu_3": "斗鱼·三星",
                            "douyu_4": "斗鱼·四星",
                            "sanshinei_1": "伞室内·一星",
                            "sanshinei_2": "伞室内·二星",
                            "sanshinei_3": "伞室内·三星",
                            "sanshinei_4": "伞室内·四星",
                            "taigu_1": "太鼓·一星",
                            "taigu_2": "太鼓·二星",
                            "taigu_3": "太鼓·三星",
                            "taigu_4": "太鼓·四星",
                            "bianyi_1": "变异·一星",
                            "bianyi_2": "变异·二星",
                            "bianyi_3": "变异·三星",
                            "bianyi_4": "变异·四星",
                        }},
                    "guild_realm_foster": {
                        "name": "寄养",
                        "stage": {
                            "foster_m": "寄养素材",
                            "foster_n": "寄养N卡"}

                    },
                    "guild_realm_cultivate": {
                        "name": "寄养",
                        "stage": {
                            "cultivate_m": "育成素材",
                            "cultivate_n": "育成N卡"}

                    },
                    "guild_realm_collection": {
                        "guild_realm_ap": "收集体力",
                        "guild_realm_exp": "收集经验"
                    },
                },
            },
            "shikigami": {
                "name": "式神",
                "zone": {
                    "upgrade_star": {"name": "升星"},
                    "upgrade_level": {"name": "升级"},
                }},
            "area_boss": {
                "name": "地域鬼王",
                "zone": {
                    "tiaotiaogege": {"name": "跳跳哥哥"},
                    "jiaotu": {"name": "椒图"},
                    "gunv": {"name": "骨女"},
                    "egui": {"name": "恶鬼"},
                    "erkounv": {"name": "二口女"},
                    "haifangzhu": {"name": "海坊主"},
                    "guishihei": {"name": "鬼使黑"},
                    "xiaosongwan": {"name": "小松丸"},
                    "rihefang": {"name": "日和坊"}
                }},
            "real_orochi": {"name": "真蛇"},
            "demon_parade": {"name": "百鬼夜行"},
            "side_bet": {
                "name": "对弈竞猜",
                "zone": {
                    "red": {
                        "name": "红方",
                        "stage": {
                            "30": "三十万",
                            "20": "二十万",
                            "10": "十万",
                            "5": "五万"
                        }},
                    "blue": {
                        "name": "蓝方",
                        "stage": {
                            "30": "三十万",
                            "20": "二十万",
                            "10": "十万",
                            "5": "五万"
                        }}

                }
            },
            "story": {
                "name": "练号",
                "zone": {
                    "story_step_1": {
                        "name": "第一阶段",
                        "stage": {
                            "new": "新手教学",
                        }}

                }},
        }


data_static = DataStatic()

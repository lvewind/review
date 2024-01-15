import random

from PySide6 import QtWidgets

import hiworker
from .ui import *


class ProductsView(QtWidgets.QMainWindow, Ui_MainWindowProduct):
    def __init__(self):
        super(ProductsView, self).__init__()
        self.setupUi(self)
        self.data = {}
        self.products_dict = {}
        self.bind_func_product()

    def init_products_table_header(self, table_setting: dict):
        hiworker.TableLoad.init_table_header(self.tableWidget_products, table_setting)

    def load_table_products(self, data: list, table_setting: dict, select_last_row=False):
        hiworker.TableLoad.load_table(self.tableWidget_products, data, table_setting, select_last_row=select_last_row)

    def get_selected_ids(self):
        return hiworker.TableRead.get_selected_data_ids(self.tableWidget_products)

    def get_selected_id(self):
        return hiworker.TableRead.get_current_data_id(self.tableWidget_products)

    # 绑定函数
    def bind_func_product(self):
        self.checkBox_job_option_chapter_all_spirit.clicked.connect(self.setup_ui_products_chapter_by_all)
        self.checkBox_job_option_chapter_exp_spirit.clicked.connect(self.setup_ui_products_option_by_single)
        self.checkBox_job_option_chapter_gift_spirit.clicked.connect(self.setup_ui_products_option_by_single)
        self.checkBox_job_option_chapter_coin_spirit.clicked.connect(self.setup_ui_products_option_by_single)

        self.radioButton_job_option_chapter_0v0.toggled.connect(self.setup_ui_products_checkbox_chapter_dog_food_change)

    # 加载下拉列表默认数据
    def load_combo_box_product_default(self):
        for key, value in self.products_dict.items():
            self.comboBox_job_option_play.addItem(value.get("name"), key)

    def load_combo_box_product_sub_default(self):
        self.comboBox_job_option_play_sub.clear()
        play_name = self.comboBox_job_option_play.currentData()
        self.setup_ui_products_line_edit_count(True)
        self.setup_ui_products_play_name_second(True)
        if play_name:
            product = self.products_dict.get(play_name)
            if product:
                zone = product.get("zone")
                if zone:
                    for k, zone in zone.items():
                        name = zone.get("name")
                        self.comboBox_job_option_play_sub.addItem(name, k)

                    self.load_combo_box_play_stage_default()
                    self.setup_ui_products_option_enabled()

    def load_combo_box_play_stage_default(self):
        self.comboBox_job_option_stage.clear()
        play_name = self.comboBox_job_option_play.currentData()
        play_name_second = self.comboBox_job_option_play_sub.currentData()
        if play_name:
            product = self.products_dict.get(play_name)
            if product:
                zones = product.get("zone")
                if zones:
                    zone = zones.get(play_name_second)
                    if zone:
                        stage = zone.get("stage")
                        if stage:
                            for k, t in stage.items():
                                self.comboBox_job_option_stage.addItem(t, k)

        self.lineEdit_count.setText(str(random.randint(30, 80)))
        self.setup_ui_products_option_enabled()

    # 加载产品默认设置
    def set_option_default(self):
        self.comboBox_job_option_play.clear()
        self.lineEdit_count.clear()
        self.checkBox_job_option_bonus_soul.setChecked(False)
        self.checkBox_job_option_bonus_evolution.setChecked(False)
        self.checkBox_job_option_bonus_coin_50.setChecked(False)
        self.checkBox_job_option_bonus_exp_50.setChecked(False)
        self.checkBox_job_option_bonus_coin_100.setChecked(False)
        self.checkBox_job_option_bonus_exp_100.setChecked(False)

        self.checkBox_job_option_chapter_exp_spirit.setChecked(False)
        self.checkBox_job_option_chapter_gift_spirit.setChecked(False)
        self.checkBox_job_option_chapter_coin_spirit.setChecked(False)
        self.radioButton_job_option_dog_food_n.setChecked(False)
        self.radioButton_job_option_dog_food_m.setChecked(False)
        self.checkBox_job_option_chapter_map_seal.setChecked(False)
        self.checkBox_job_option_chapter_map_gift.setChecked(False)

        self.checkBox_job_option_encounter_boss.setChecked(False)
        self.checkBox_job_option_gymnasium_only_watch.setChecked(False)
        self.checkBox_job_option_gymnasium_mass.setChecked(False)
        self.checkBox_job_option_use_yingbing.setChecked(False)
        self.checkBox_job_option_lock_cast.setChecked(False)
        self.lineEdit_count.setText(str(random.randint(30, 80)))

    def load_option_product(self, product_data: dict):
        self.data = product_data

        play_name = product_data.get("play_name")
        if play_name:
            count = self.comboBox_job_option_play.count()
            for i in range(count):
                if self.comboBox_job_option_play.itemData(i) == play_name:
                    self.comboBox_job_option_play.setCurrentIndex(i)
                    break

        self.load_combo_box_product_sub_default()
        play_name_second = product_data.get("play_name_second")
        if play_name_second:
            count = self.comboBox_job_option_play_sub.count()
            for i in range(count):
                if self.comboBox_job_option_play_sub.itemData(i) == play_name_second:
                    self.comboBox_job_option_play_sub.setCurrentIndex(i)
                    break
                    
        play_stage = str(product_data.get("chapter_stage"))
        if play_stage:
            count = self.comboBox_job_option_stage.count()
            for i in range(count):
                if self.comboBox_job_option_stage.itemData(i) == play_stage:
                    self.comboBox_job_option_stage.setCurrentIndex(i)
                    break

        count = product_data.get("preset_count")
        self.lineEdit_count.setText(str(count)) if count else self.lineEdit_count.setText(str(random.randint(30, 80)))

        self.setup_ui_products_option_enabled()

        self.checkBox_job_option_approximate_count.setChecked(True if product_data.get("approximate_count") else False)

        self.checkBox_job_option_bonus_soul.setChecked(True if product_data.get("bonus_soul") else False)
        self.checkBox_job_option_bonus_evolution.setChecked(True if product_data.get("bonus_evo") else False)
        self.checkBox_job_option_bonus_coin_50.setChecked(True if product_data.get("bonus_coin_50") else False)
        self.checkBox_job_option_bonus_coin_100.setChecked(True if product_data.get("bonus_coin_100") else False)
        self.checkBox_job_option_bonus_exp_50.setChecked(True if product_data.get("bonus_exp_50") else False)
        self.checkBox_job_option_bonus_exp_100.setChecked(True if product_data.get("bonus_exp_100") else False)

        self.checkBox_job_option_chapter_exp_spirit.setChecked(True if product_data.get("chapter_spirit_exp") else False)
        self.checkBox_job_option_chapter_gift_spirit.setChecked(True if product_data.get("chapter_spirit_gift") else False)
        self.checkBox_job_option_chapter_coin_spirit.setChecked(True if product_data.get("chapter_spirit_coin") else False)
        self.checkBox_job_option_chapter_map_seal.setChecked(True if product_data.get("chapter_map_seal") else False)
        self.checkBox_job_option_chapter_map_gift.setChecked(True if product_data.get("chapter_map_gift") else False)

        self.radioButton_job_option_dog_food_n.setChecked(True if product_data.get("dog_food_n") else False)
        self.radioButton_job_option_dog_food_m.setChecked(True if product_data.get("dog_food_m") else False)

        self.radioButton_job_option_chapter_2v2.setChecked(True if product_data.get("chapter_2v2") else False)
        self.radioButton_job_option_chapter_1v3.setChecked(True if product_data.get("chapter_1v3") else False)
        self.radioButton_job_option_chapter_0v3.setChecked(True if product_data.get("chapter_0v3") else False)
        self.radioButton_job_option_chapter_1v2.setChecked(True if product_data.get("chapter_1v2") else False)
        self.radioButton_job_option_chapter_0v0.setChecked(True if product_data.get("chapter_0v0") else False)

        self.radioButton_job_option_dog_food_star_2.setChecked(True if product_data.get("chapter_dog_food_2") else False)
        self.radioButton_job_option_dog_food_star_3.setChecked(True if product_data.get("chapter_dog_food_3") else False)
        self.radioButton_job_option_dog_food_star_4.setChecked(True if product_data.get("chapter_dog_food_4") else False)

        self.checkBox_job_option_use_yingbing.setChecked(True if product_data.get("use_yingbing") else False)
        self.checkBox_job_option_lock_cast.setChecked(True if product_data.get("lock_cast") else False)
        self.checkBox_job_option_encounter_boss.setChecked(True if product_data.get("encounter_boss") else False)

        self.checkBox_job_option_gymnasium_only_watch.setChecked(True if product_data.get("gymnasium_only_watch") else False)
        self.checkBox_job_option_gymnasium_mass.setChecked(True if product_data.get("gymnasium_mass") else False)

        self.checkBox_job_option_guild_mall_grade_daruma.setChecked(True if product_data.get("guild_mall_grade_daruma") else False)
        self.checkBox_job_option_guild_mall_souls.setChecked(True if product_data.get("guild_mall_souls") else False)
        self.checkBox_job_option_guild_mall_amulet.setChecked(True if product_data.get("guild_mall_amulet") else False)
        self.checkBox_job_option_guild_mall_skill_daruma.setChecked(True if product_data.get("guild_mall_skill_daruma") else False)
        self.checkBox_job_option_guild_mall_skin_ticket.setChecked(True if product_data.get("guild_mall_skin_ticket") else False)
        self.checkBox_job_option_guild_mall_yingbing.setChecked(True if product_data.get("guild_mall_yingbing") else False)

        self.checkBox_job_option_story_buy_ap.setChecked(True if product_data.get("story_buy_ap") else False)
        self.checkBox_job_option_story_realm_raid.setChecked(True if product_data.get("story_realm_raid") else False)

        self.checkBox_job_option_failed_stop.setChecked(True if product_data.get("battle_failed_stop") else False)
        self.checkBox_job_option_ap_use_up_close_game.setChecked(True if product_data.get("ap_use_up_close_game") else False)
        self.checkBox_job_option_ap_use_up_restart.setChecked(True if product_data.get("ap_use_up_restart") else False)

        self.checkBox_job_option_guild_coin.setChecked(True if product_data.get("guild_coin") else False)
        self.checkBox_job_option_guild_contribute.setChecked(True if product_data.get("guild_contribute") else False)
        self.checkBox_job_option_guild_invocation.setChecked(True if product_data.get("guild_invocation") else False)
        self.checkBox_job_option_guild_task.setChecked(True if product_data.get("guild_task") else False)
        self.checkBox_job_option_guild_task_contribute.setChecked(True if product_data.get("guild_task_contribute") else False)
        self.checkBox_job_option_guild_realm_ap.setChecked(True if product_data.get("realm_ap") else False)

        self.checkBox_job_option_guild_foster_m.setChecked(True if product_data.get("guild_foster_m") else False)
        self.checkBox_job_option_guild_foster_n.setChecked(True if product_data.get("guild_foster_n") else False)
        self.checkBox_job_option_guild_cultivate_m.setChecked(True if product_data.get("cultivate_m") else False)
        self.checkBox_job_option_guild_cultivate_n.setChecked(True if product_data.get("cultivate_n") else False)

    def get_product_option(self):
        counter_item = ""
        play_name = self.comboBox_job_option_play.currentData()
        play_name_second = self.comboBox_job_option_play_sub.currentData()
        play_stage = self.comboBox_job_option_stage.currentData()
        if not play_stage:
            play_stage = 0
        if play_name_second == "orochi":
            if play_stage == "11":
                counter_item = "orochi_11"
            elif play_stage == "10":
                counter_item = "orochi_10"
        elif play_name == "chapter" or \
                play_name == "totem" or \
                play_name == "evo_materials" or \
                play_name == "real_orochi" or \
                play_name == "summon" or \
                play_name == "pet" or \
                play_name == "area_boss" or \
                play_name == "demon_parade" or \
                play_name == "side_bet":
            counter_item = play_name
        else:
            counter_item = play_name_second
        self.data.update({
            "play_name": play_name,
            "play_name_second": play_name_second,
            "counter_item": counter_item,
            "chapter_stage": play_stage,
            "preset_count": int(self.lineEdit_count.text()),
            "approximate_count": 1 if self.checkBox_job_option_approximate_count.isChecked() else 0,

            "use_yingbing": 1 if self.checkBox_job_option_use_yingbing.isChecked() else 0,
            "lock_cast": 1 if self.checkBox_job_option_lock_cast.isChecked() else 0,

            "bonus_soul": 1 if self.checkBox_job_option_bonus_soul.isChecked() else 0,
            "bonus_evo": 1 if self.checkBox_job_option_bonus_evolution.isChecked() else 0,
            "bonus_coin_50": 1 if self.checkBox_job_option_bonus_coin_50.isChecked() else 0,
            "bonus_coin_100": 1 if self.checkBox_job_option_bonus_coin_100.isChecked() else 0,
            "bonus_exp_50": 1 if self.checkBox_job_option_bonus_exp_50.isChecked() else 0,
            "bonus_exp_100": 1 if self.checkBox_job_option_bonus_exp_100.isChecked() else 0,

            "chapter_spirit_exp": 1 if self.checkBox_job_option_chapter_exp_spirit.isChecked() else 0,
            "chapter_spirit_coin": 1 if self.checkBox_job_option_chapter_gift_spirit.isChecked() else 0,
            "chapter_spirit_gift": 1 if self.checkBox_job_option_chapter_coin_spirit.isChecked() else 0,
            "chapter_map_seal": 1 if self.checkBox_job_option_chapter_map_seal.isChecked() else 0,
            "chapter_map_gift": 1 if self.checkBox_job_option_chapter_map_gift.isChecked() else 0,

            "chapter_2v2": 1 if self.radioButton_job_option_chapter_2v2.isChecked() else 0,
            "chapter_1v3": 1 if self.radioButton_job_option_chapter_1v3.isChecked() else 0,
            "chapter_0v3": 1 if self.radioButton_job_option_chapter_0v3.isChecked() else 0,
            "chapter_1v2": 1 if self.radioButton_job_option_chapter_1v2.isChecked() else 0,
            "chapter_0v0": 1 if self.radioButton_job_option_chapter_0v0.isChecked() else 0,

            "chapter_dog_food_n": 1 if self.radioButton_job_option_dog_food_n.isChecked() else 0,
            "chapter_dog_food_m": 1 if self.radioButton_job_option_dog_food_m.isChecked() else 0,
            "chapter_dog_food_2": 1 if self.radioButton_job_option_dog_food_star_2.isChecked() else 0,
            "chapter_dog_food_3": 1 if self.radioButton_job_option_dog_food_star_3.isChecked() else 0,
            "chapter_dog_food_4": 1 if self.radioButton_job_option_dog_food_star_4.isChecked() else 0,

            "encounter_boss": 1 if self.checkBox_job_option_encounter_boss.isChecked() else 0,

            "guild_mall_grade_daruma": 1 if self.checkBox_job_option_guild_mall_grade_daruma.isChecked() else 0,
            "guild_mall_souls": 1 if self.checkBox_job_option_guild_mall_grade_daruma.isChecked() else 0,
            "guild_mall_amulet": 1 if self.checkBox_job_option_guild_mall_grade_daruma.isChecked() else 0,
            "guild_mall_skill_daruma": 1 if self.checkBox_job_option_guild_mall_grade_daruma.isChecked() else 0,
            "guild_mall_skin_ticket": 1 if self.checkBox_job_option_guild_mall_grade_daruma.isChecked() else 0,
            "guild_mall_yingbing": 1 if self.checkBox_job_option_guild_mall_grade_daruma.isChecked() else 0,

            "gymnasium_only_watch": 1 if self.checkBox_job_option_gymnasium_only_watch.isChecked() else 0,
            "gymnasium_mass": 1 if self.checkBox_job_option_gymnasium_mass.isChecked() else 0,

            "story_buy_ap": 1 if self.checkBox_job_option_story_buy_ap.isChecked() else 0,
            "story_realm_raid": 1 if self.checkBox_job_option_story_realm_raid.isChecked() else 0,
            "battle_failed_stop": 1 if self.checkBox_job_option_failed_stop.isChecked() else 0,
            "ap_use_up_close_game": 1 if self.checkBox_job_option_ap_use_up_close_game.isChecked() else 0,
            "ap_use_up_restart": 1 if self.checkBox_job_option_ap_use_up_restart.isChecked() else 0,

            "guild_coin": 1 if self.checkBox_job_option_guild_coin.isChecked() else 0,
            "guild_contribute": 1 if self.checkBox_job_option_guild_contribute.isChecked() else 0,
            "guild_invocation": 1 if self.checkBox_job_option_guild_invocation.isChecked() else 0,
            "guild_task": 1 if self.checkBox_job_option_guild_task.isChecked() else 0,
            "guild_task_contribute": 1 if self.checkBox_job_option_guild_task_contribute.isChecked() else 0,
            "realm_ap": 1 if self.checkBox_job_option_guild_realm_ap.isChecked() else 0,

            "guild_foster_m": 1 if self.checkBox_job_option_guild_foster_m.isChecked() else 0,
            "guild_foster_n": 1 if self.checkBox_job_option_guild_foster_n.isChecked() else 0,
            "cultivate_m": 1 if self.checkBox_job_option_guild_cultivate_m.isChecked() else 0,
            "cultivate_n": 1 if self.checkBox_job_option_guild_cultivate_n.isChecked() else 0

        })
        return self.data

    def setup_ui_products_chapter_by_all(self):
        if self.checkBox_job_option_chapter_all_spirit.isChecked():
            self.checkBox_job_option_chapter_exp_spirit.setChecked(True)
            self.checkBox_job_option_chapter_gift_spirit.setChecked(True)
            self.checkBox_job_option_chapter_coin_spirit.setChecked(True)
        else:
            pass

    def setup_ui_products_option_by_single(self):
        if self.checkBox_job_option_chapter_exp_spirit.isChecked() \
                and self.checkBox_job_option_chapter_gift_spirit.isChecked() \
                and self.checkBox_job_option_chapter_coin_spirit.isChecked():
            self.checkBox_job_option_chapter_all_spirit.setChecked(True)
        else:
            self.checkBox_job_option_chapter_all_spirit.setChecked(False)

    def setup_ui_products_option_enabled(self):
        self.setup_ui_products_option_all_enabled(False)
        play_name = self.comboBox_job_option_play.currentData()
        play_name_second = self.comboBox_job_option_play_sub.currentData()
        if play_name == "souls":
            self.setup_ui_products_combo_box_enabled(True, True, True)
            self.setup_ui_products_checkbox_cast_lock_enabled(True)
            self.setup_ui_products_checkbox_use_yingbing_enabled(True)
            self.setup_ui_products_checkbox_ap_use_up(True)
            self.setup_ui_products_checkbox_failed_stop(True)
            if play_name_second == "orochi":
                self.setup_ui_products_checkbox_bonus_enabled(True, False, True, True, True, True)
            else:
                self.setup_ui_products_checkbox_bonus_enabled(False, False, True, True, True, True)

        elif play_name == "chapter":
            self.setup_ui_products_combo_box_enabled(True, True, True)
            self.setup_ui_products_checkbox_cast_lock_enabled(True)
            self.setup_ui_products_checkbox_use_yingbing_enabled(True)
            self.setup_ui_products_checkbox_failed_stop(True)
            self.setup_ui_products_checkbox_chapter_enabled(True)
            self.setup_ui_products_checkbox_bonus_enabled(False, False, True, True, True, True)
        elif play_name == "story":
            self.setup_ui_products_combo_box_enabled(True, True, True)
            self.setup_ui_products_checkbox_cast_lock_enabled(True)
            self.setup_ui_products_checkbox_use_yingbing_enabled(True)
            self.setup_ui_products_checkbox_failed_stop(True)
            self.setup_ui_products_checkbox_chapter_enabled(True)
            self.setup_ui_products_checkbox_bonus_enabled(False, False, True, True, True, True)
            self.setup_ui_products_checkbox_story_enabled(True)

        elif play_name == "totem":
            self.setup_ui_products_combo_box_enabled(True, True, True)
            self.setup_ui_products_checkbox_cast_lock_enabled(True)
            self.setup_ui_products_checkbox_use_yingbing_enabled(True)
            self.setup_ui_products_checkbox_failed_stop(True)
            self.setup_ui_products_checkbox_bonus_enabled(False, False, True, True, True, True)

        elif play_name == "evo_materials":
            self.setup_ui_products_combo_box_enabled(True, True, True)
            self.setup_ui_products_checkbox_cast_lock_enabled(True)
            self.setup_ui_products_checkbox_use_yingbing_enabled(True)
            self.setup_ui_products_checkbox_failed_stop(True)
            self.setup_ui_products_checkbox_bonus_enabled(False, True, True, True, True, True)
            self.setup_ui_products_checkbox_ap_use_up(True)

        elif play_name == "realm_raid":
            self.setup_ui_products_combo_box_enabled(True, True, False)
            self.setup_ui_products_checkbox_cast_lock_enabled(True)
            self.setup_ui_products_checkbox_failed_stop(True)
            self.setup_ui_products_checkbox_bonus_enabled(False, False, True, True, True, True)

        else:
            self.setup_ui_products_checkbox_cast_lock_enabled(False)
            self.setup_ui_products_checkbox_use_yingbing_enabled(False)
            if play_name == "real_orochi":
                self.setup_ui_products_combo_box_enabled(False, False, False)

            elif play_name == "teamup":
                if play_name_second == "demon_seal":
                    self.setup_ui_products_combo_box_enabled(True, True, True)
                else:
                    self.setup_ui_products_combo_box_enabled(True, False, True)
                self.setup_ui_products_checkbox_bonus_enabled(False, False, True, True, True, True)

            elif play_name == "daily":
                self.setup_ui_products_combo_box_enabled(True, False, False)

            elif play_name == "mall":
                self.setup_ui_products_combo_box_enabled(True, False, False)

            elif play_name == "yard":
                self.setup_ui_products_combo_box_enabled(True, False, False)

            elif play_name == "shikigami":
                self.setup_ui_products_combo_box_enabled(True, False, False)

            elif play_name == "guild":
                if play_name_second == "guild_daily":
                    self.setup_ui_products_combo_box_enabled(True, False, False)
                    self.setup_ui_products_checkbox_guild_daily(True)
                elif play_name_second == "guild_realm":
                    self.setup_ui_products_combo_box_enabled(True, False, False)
                    self.setup_ui_products_checkbox_guild_realm(True)
                elif play_name_second == "guild_mall":
                    self.setup_ui_products_combo_box_enabled(True, False, False)
                    self.setup_ui_products_checkbox_guild_mall(True)
                else:
                    self.setup_ui_products_combo_box_enabled(True, True, False)
                    self.setup_ui_products_checkbox_guild_mall(False)

            elif play_name == "summon":
                if play_name_second == "summon_free":
                    self.setup_ui_products_combo_box_enabled(True, False, False)
                else:
                    self.setup_ui_products_combo_box_enabled(True, False, True)

            elif play_name == "pet":
                self.setup_ui_products_combo_box_enabled(True, False, False)

            elif play_name == "area_boss":
                self.setup_ui_products_combo_box_enabled(True, False, False)

            elif play_name == "demon_parade":
                self.setup_ui_products_combo_box_enabled(True, False, True)

            elif play_name == "side_bet":
                self.setup_ui_products_combo_box_enabled(False, False, True)
            elif play_name == "story":
                self.setup_ui_products_combo_box_enabled(True, False, False)

    def setup_ui_products_option_all_enabled(self, enabled: bool):

        self.setup_ui_products_checkbox_bonus_enabled(False, False, False, False, False, False)

        self.setup_ui_products_checkbox_chapter_enabled(enabled)

        self.setup_ui_products_checkbox_gymnasium_mass(enabled)

        self.setup_ui_products_checkbox_guild_daily(enabled)

        self.setup_ui_products_checkbox_guild_realm(enabled)

        self.setup_ui_products_checkbox_guild_mall(enabled)

        self.setup_ui_products_checkbox_use_yingbing_enabled(enabled)

        self.setup_ui_products_checkbox_cast_lock_enabled(enabled)

        self.setup_ui_products_checkbox_encounter_boss(enabled)

        self.setup_ui_products_checkbox_failed_stop(enabled)

        self.setup_ui_products_checkbox_story_enabled(enabled)

    def setup_ui_products_line_edit_count(self, enabled=True):
        self.lineEdit_count.setEnabled(enabled)

    def setup_ui_products_combo_box_enabled(self, play_sub: bool, stage: bool, count: bool):
        self.comboBox_job_option_play_sub.setEnabled(play_sub)
        self.comboBox_job_option_stage.setEnabled(stage)
        self.lineEdit_count.setEnabled(count)
        self.checkBox_job_option_approximate_count.setEnabled(count)
        if not play_sub:
            self.comboBox_job_option_play_sub.clear()
        if not stage:
            self.comboBox_job_option_stage.clear()
        if not count:
            self.lineEdit_count.setText("0")
        if not count:
            self.checkBox_job_option_approximate_count.setChecked(False)

    def setup_ui_products_checkbox_bonus_enabled(self, soul: bool, evo: bool, coin_50: bool, coin_100: bool, exp_50: bool, exp_100: bool):
        self.checkBox_job_option_bonus_soul.setEnabled(soul)
        self.checkBox_job_option_bonus_evolution.setEnabled(evo)
        self.checkBox_job_option_bonus_coin_50.setEnabled(coin_50)
        self.checkBox_job_option_bonus_coin_100.setEnabled(coin_100)
        self.checkBox_job_option_bonus_exp_50.setEnabled(exp_50)
        self.checkBox_job_option_bonus_exp_100.setEnabled(exp_100)
        if not soul:
            self.checkBox_job_option_bonus_soul.setChecked(soul)
        if not evo:
            self.checkBox_job_option_bonus_evolution.setChecked(evo)
        if not coin_50:
            self.checkBox_job_option_bonus_coin_50.setChecked(coin_50)
        if not coin_100:
            self.checkBox_job_option_bonus_coin_100.setChecked(coin_100)
        if not exp_50:
            self.checkBox_job_option_bonus_exp_50.setChecked(exp_50)
        if not exp_100:
            self.checkBox_job_option_bonus_exp_100.setChecked(exp_100)

    def setup_ui_products_checkbox_chapter_enabled(self, enabled: bool):
        self.checkBox_job_option_chapter_all_spirit.setEnabled(enabled)
        self.checkBox_job_option_chapter_exp_spirit.setEnabled(enabled)
        self.checkBox_job_option_chapter_coin_spirit.setEnabled(enabled)
        self.checkBox_job_option_chapter_gift_spirit.setEnabled(enabled)
        self.checkBox_job_option_chapter_map_gift.setEnabled(enabled)
        self.checkBox_job_option_chapter_map_seal.setEnabled(enabled)

        self.radioButton_job_option_chapter_2v2.setEnabled(enabled)
        self.radioButton_job_option_chapter_1v3.setEnabled(enabled)
        self.radioButton_job_option_chapter_0v3.setEnabled(enabled)
        self.radioButton_job_option_chapter_1v2.setEnabled(enabled)
        self.radioButton_job_option_chapter_0v0.setEnabled(enabled)

        self.setup_ui_products_checkbox_chapter_dog_food_enabled(enabled)

        self.setup_ui_products_checkbox_ap_use_up(enabled)

        if not enabled:
            self.checkBox_job_option_chapter_all_spirit.setChecked(enabled)
            self.checkBox_job_option_chapter_exp_spirit.setChecked(enabled)
            self.checkBox_job_option_chapter_coin_spirit.setChecked(enabled)
            self.checkBox_job_option_chapter_gift_spirit.setChecked(enabled)
            self.checkBox_job_option_chapter_map_gift.setChecked(enabled)
            self.checkBox_job_option_chapter_map_seal.setChecked(enabled)

        if self.radioButton_job_option_chapter_0v0.isChecked():
            self.setup_ui_products_checkbox_chapter_dog_food_enabled(False)

    def setup_ui_products_checkbox_chapter_dog_food_enabled(self, enabled: bool):
        self.radioButton_job_option_dog_food_m.setEnabled(enabled)
        self.radioButton_job_option_dog_food_n.setEnabled(enabled)
        self.radioButton_job_option_dog_food_star_2.setEnabled(enabled)
        self.radioButton_job_option_dog_food_star_3.setEnabled(enabled)
        self.radioButton_job_option_dog_food_star_4.setEnabled(enabled)

    def setup_ui_products_checkbox_chapter_dog_food_change(self):
        if self.radioButton_job_option_chapter_0v0.isChecked():
            self.setup_ui_products_checkbox_chapter_dog_food_enabled(False)
        else:
            self.setup_ui_products_checkbox_chapter_dog_food_enabled(True)

    def setup_ui_products_checkbox_encounter_enabled(self, is_boss: bool):
        self.checkBox_job_option_encounter_boss.setEnabled(is_boss)
        self.checkBox_job_option_encounter_boss.setChecked(is_boss)

    def setup_ui_products_checkbox_cast_lock_enabled(self, enabled):
        self.checkBox_job_option_lock_cast.setEnabled(enabled)
        if not enabled:
            self.checkBox_job_option_lock_cast.setChecked(enabled)

    def setup_ui_products_checkbox_use_yingbing_enabled(self, enabled: bool):
        self.checkBox_job_option_use_yingbing.setEnabled(enabled)
        if not enabled:
            self.checkBox_job_option_use_yingbing.setChecked(enabled)

    def setup_ui_products_checkbox_failed_stop(self, enabled: bool):
        self.checkBox_job_option_failed_stop.setEnabled(enabled)
        if not enabled:
            self.checkBox_job_option_failed_stop.setChecked(enabled)

    def setup_ui_products_checkbox_gymnasium_mass(self, enabled: bool):
        self.checkBox_job_option_gymnasium_mass.setEnabled(enabled)
        self.checkBox_job_option_gymnasium_only_watch.setEnabled(enabled)
        if not enabled:
            self.checkBox_job_option_gymnasium_mass.setChecked(enabled)
            self.checkBox_job_option_gymnasium_only_watch.setChecked(enabled)

    def setup_ui_products_checkbox_guild_mall(self, enabled: bool):
        self.checkBox_job_option_guild_mall_grade_daruma.setEnabled(enabled)
        self.checkBox_job_option_guild_mall_souls.setEnabled(enabled)
        self.checkBox_job_option_guild_mall_amulet.setEnabled(enabled)
        self.checkBox_job_option_guild_mall_skill_daruma.setEnabled(enabled)
        self.checkBox_job_option_guild_mall_skin_ticket.setEnabled(enabled)
        self.checkBox_job_option_guild_mall_yingbing.setEnabled(enabled)

        if not enabled:
            self.checkBox_job_option_guild_mall_grade_daruma.setChecked(enabled)
            self.checkBox_job_option_guild_mall_souls.setChecked(enabled)
            self.checkBox_job_option_guild_mall_amulet.setChecked(enabled)
            self.checkBox_job_option_guild_mall_skill_daruma.setChecked(enabled)
            self.checkBox_job_option_guild_mall_skin_ticket.setChecked(enabled)
            self.checkBox_job_option_guild_mall_yingbing.setChecked(enabled)

    def setup_ui_products_checkbox_guild_daily(self, enabled: bool):
        self.checkBox_job_option_guild_coin.setEnabled(enabled)
        self.checkBox_job_option_guild_contribute.setEnabled(enabled)
        self.checkBox_job_option_guild_invocation.setEnabled(enabled)
        self.checkBox_job_option_guild_task.setEnabled(enabled)
        self.checkBox_job_option_guild_task_contribute.setEnabled(enabled)
        self.checkBox_job_option_guild_realm_ap.setEnabled(enabled)

        if not enabled:
            self.checkBox_job_option_guild_coin.setChecked(enabled)
            self.checkBox_job_option_guild_contribute.setChecked(enabled)
            self.checkBox_job_option_guild_invocation.setChecked(enabled)
            self.checkBox_job_option_guild_task.setChecked(enabled)
            self.checkBox_job_option_guild_task_contribute.setChecked(enabled)
            self.checkBox_job_option_guild_realm_ap.setChecked(enabled)

    def setup_ui_products_checkbox_guild_realm(self, enabled: bool):
        self.checkBox_job_option_guild_foster_m.setEnabled(enabled)
        self.checkBox_job_option_guild_foster_n.setEnabled(enabled)
        self.checkBox_job_option_guild_cultivate_m.setEnabled(enabled)
        self.checkBox_job_option_guild_cultivate_n.setEnabled(enabled)

        if not enabled:
            self.checkBox_job_option_guild_foster_m.setChecked(enabled)
            self.checkBox_job_option_guild_foster_n.setChecked(enabled)
            self.checkBox_job_option_guild_cultivate_m.setChecked(enabled)
            self.checkBox_job_option_guild_cultivate_n.setChecked(enabled)

    def setup_ui_products_checkbox_encounter_boss(self, enabled):
        self.checkBox_job_option_encounter_boss.setEnabled(enabled)
        if not enabled:
            self.checkBox_job_option_encounter_boss.setChecked(enabled)

    def setup_ui_products_checkbox_story_enabled(self, enabled):
        self.checkBox_job_option_story_buy_ap.setEnabled(enabled)
        self.checkBox_job_option_story_realm_raid.setEnabled(enabled)
        self.setup_ui_products_checkbox_ap_use_up(enabled)

    def setup_ui_products_checkbox_ap_use_up(self, enabled):
        self.checkBox_job_option_ap_use_up_close_game.setEnabled(enabled)
        self.checkBox_job_option_ap_use_up_restart.setEnabled(enabled)

    def setup_ui_products_play_stage(self, enabled=True):
        self.comboBox_job_option_stage.setEnabled(enabled)

    def setup_ui_products_play_name_second(self, enabled=True):
        self.comboBox_job_option_play_sub.setEnabled(enabled)


# 列表项创建/编辑对话框
class ProductsAddView(QtWidgets.QDialog, Ui_Dialog_plan_list_add):
    def __init__(self):
        super(ProductsAddView, self).__init__()
        self.setupUi(self)
        self.groupBox.hide()
        self.checkBox_close_env.hide()
        self.data = {}

    def show_add(self):
        self.data = {}
        self.setWindowTitle("新增产品")
        self.groupBox_list_item_name.setWindowTitle("输入产品名称")
        self.lineEdit_new_list_name.clear()
        self.show()

    def show_edit(self, data: dict):
        self.data = data
        self.setWindowTitle("编辑产品")
        self.groupBox_list_item_name.setWindowTitle("输入产品名称")
        self.lineEdit_new_list_name.setText(data.get("name"))
        self.show()

    def get_product_data(self):
        self.data.update({"name": self.lineEdit_new_list_name.text()})
        return self.data

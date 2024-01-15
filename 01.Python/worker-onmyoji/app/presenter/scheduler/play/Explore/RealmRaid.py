from ..Common import *
from ....sender import signal_run_list


class PlayRealmRaid(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayRealmRaid, self).__init__(play_input)
        self.need_to_refresh = False
        self.need_to_set_realm = False

    def run(self):
        self.is_scene_after_battling = False
        self.need_to_refresh = False
        self.stop_flag = False
        self.stop_status = False
        self.need_to_set_realm = False
        self.config_bonus = False
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            # print("realm_raid_stop_flag: ", self.run_id, self.stop_flag)
            if not self.stop_flag:
                if self.is_scene_after_battling:
                    if self.is_battle_manual():
                        signal_run_list.set_current_operation.emit(self.run_id, "设置自动")
                        self.change_auto_battle()
                    else:
                        signal_run_list.set_current_operation.emit(self.run_id, "等待战斗结束")
                        self.processing_after_battle()
                else:
                    if self.is_battle_win_prize_daruma():  # 战斗奖励
                        self.skip_battle_win_prize(random.randint(1, 3))
                    elif self.is_realm_raid_panel():
                        self.is_scene_after_battling = False
                        if self.product.play_name_second == "realm_raid_person":
                            self.realm_raid_person()
                        elif self.product.play_name_second == "realm_raid_guild":
                            self.realm_raid_guild()
                    elif self.is_battle_battling():
                        self .processing_battling()
                    elif self.is_battle_ready():
                        self .processing_battle_ready()
                    elif self.is_explore():
                        self .processing_explore()
                    elif self.is_yard():
                        if self.need_to_set_realm:
                            if self.is_bottom_menu_open():
                                if self.is_guild_entrance():
                                    self.open_guild()
                            else:
                                self.open_bottom_menu_in_yard()
                        else:
                            signal_run_list.set_current_scene.emit(self.run_id, "庭院")
                            signal_run_list.set_current_operation.emit(self.run_id, "进入探索地图")
                            self.processing_yard()
                    elif self.is_guild_panel():
                        if self.is_create_realm_button():
                            self.open_guild_realm()
                        elif self.is_guild_realm_entrance():
                            self.need_to_set_realm = False
                        else:
                            self.stop_flag = True
                    elif self.is_create_guild_realm_map():
                        if self.is_create_guild_button():
                            self.click_create_guild_realm_button()
                    elif self.is_create_guild_realm_map_done():
                        self.quit_create_guild_realm_map()
            else:
                self.is_finished = True
                self.processing_stop()
            self.sleep_in_run()

    def realm_raid_person(self):
        if self.is_realm_raid_panel_person():
            signal_run_list.set_current_scene.emit(self.run_id, "个人突破")
            if self.is_realm_raid_pass_use_up():  # 突破券用完
                self.stop_flag = True
            # 阵容锁定已经设置
            elif self.cast_lock_set:
                chapter_stage = self.product.chapter_stage
                if self.is_realm_raid_frog():
                    if chapter_stage == 3 and self.is_realm_raid_break_3_frog():
                        self.need_to_refresh = True
                    elif chapter_stage == 6 and self.is_realm_raid_break_6_frog():
                        self.need_to_refresh = True
                    elif chapter_stage == 9:
                        pass
                else:
                    if chapter_stage == 3 and self.is_realm_raid_break_3():
                        self.need_to_refresh = True
                    elif chapter_stage == 6 and self.is_realm_raid_break_6():
                        self.need_to_refresh = True
                    elif chapter_stage == 9:
                        pass

                if self.is_battle_win_prize_daruma():  # 达摩奖励
                    self.skip_battle_win_prize(random.randint(1, 3))
                elif self.need_to_refresh:
                    if self.is_realm_raid_refresh_confirm_button():
                        signal_run_list.set_current_operation.emit(self.run_id, "刷新")
                        while self.is_realm_raid_refresh_confirm_button():
                            self.confirm_refresh_realm_raid()
                            time.sleep(1)
                        else:
                            self.need_to_refresh = False
                            time.sleep(1)
                    elif self.is_realm_raid_refresh_button():
                        self.refresh_realm_raid()
                    elif self.is_realm_raid_refresh_button_frog():
                        self.refresh_realm_raid_frog()
                    else:
                        signal_run_list.set_current_operation.emit(self.run_id, "等待刷新")
                        time.sleep(1)

                else:
                    signal_run_list.set_current_operation.emit(self.run_id, "查找攻击")
                    result, coord = self.find_realm_raid_attack_button()  # 查找进攻按键
                    if result:
                        signal_run_list.set_current_operation.emit(self.run_id, "攻击")
                        self.click_in_circle(coord, 32)
                        time.sleep(1)
                    else:
                        signal_run_list.set_current_operation.emit(self.run_id, "查找目标")
                        self.find_realm_raid_person_target_row_and_col()

            # 设置阵容锁定
            else:
                self.check_cast_lock()
        else:
            self.select_realm_raid_panel_person()

    def realm_raid_guild(self):
        if self.is_realm_raid_panel_guild():
            signal_run_list.set_current_scene.emit(self.run_id, "寮突破")
            if self.is_realm_raid_guild_not_start():
                self.stop_flag = True
            elif self.is_realm_raid_guild_all_break():
                self.stop_flag = True
            # 阵容锁定已经设置
            elif self.cast_lock_set:
                if self.need_to_refresh:
                    signal_run_list.set_current_operation.emit(self.run_id, "等待次数刷新")
                    if not self.is_realm_raid_guild_attack_use_up():
                        self.need_to_refresh = False
                else:
                    if self.is_realm_raid_guild_attack_use_up():
                        self.need_to_refresh = True
                    else:
                        signal_run_list.set_current_operation.emit(self.run_id, "查找攻击")
                        result, coord = self.find_realm_raid_attack_button()  # 查找进攻按键
                        if result:
                            signal_run_list.set_current_operation.emit(self.run_id, "攻击")
                            self.click_in_circle(coord, 32)
                            time.sleep(1)
                            result, coord = self.find_realm_raid_attack_button()  # 查找进攻按键
                            if result:
                                signal_run_list.set_current_operation.emit(self.run_id, "取消攻击")
                                self.click_in_circle([coord[0] + 100, coord[1] - 50], 32)
                                time.sleep(1)
                        else:
                            signal_run_list.set_current_operation.emit(self.run_id, "查找目标")
                            self.find_realm_raid_guild_target()

            # 设置阵容锁定
            else:
                self.check_cast_lock()
        else:
            self.select_guild_realm_raid_panel_guild()

    def check_cast_lock(self):
        signal_run_list.set_current_operation.emit(self.run_id, "设置阵容锁定")
        if self.product.lock_cast:
            if self.product.play_name_second == "realm_raid_person":
                if self.is_realm_raid_cast_lock() or self.is_realm_raid_cast_lock_frog():
                    self.cast_lock_set = True
                    self.cast_lock_up = True
                elif self.is_realm_raid_cast_unlock():
                    self.lock_realm_raid_cast()
                elif self.is_realm_raid_cast_unlock_frog():
                    self.lock_realm_raid_cast_frog()
                else:
                    self.cast_lock_set = True
                    self.cast_lock_up = True
            elif self.product.play_name_second == "realm_raid_guild":
                if self.is_realm_raid_guild_cast_lock():
                    self.cast_lock_set = True
                    self.cast_lock_up = True
                elif self.is_realm_raid_guild_cast_unlock():
                    self.lock_realm_raid_guild_cast()
                else:
                    self.cast_lock_set = True
                    self.cast_lock_up = True
        else:
            if self.product.play_name_second == "realm_raid_person":
                if self.is_realm_raid_cast_unlock() or self.is_realm_raid_cast_unlock_frog():
                    self.cast_lock_set = True
                    self.cast_lock_up = False
                elif self.is_realm_raid_cast_lock():
                    self.unlock_realm_raid_cast()
                elif self.is_realm_raid_cast_lock_frog():
                    self.unlock_realm_raid_cast_frog()
                else:
                    self.cast_lock_set = True
                    self.cast_lock_up = False
            elif self.product.play_name_second == "realm_raid_guild":
                if self.is_realm_raid_guild_cast_unlock():
                    self.cast_lock_set = True
                    self.cast_lock_up = False
                elif self.is_realm_raid_guild_cast_lock():
                    self.unlock_realm_raid_guild_cast()
                else:
                    self.cast_lock_set = True
                    self.cast_lock_up = False

    def find_realm_raid_person_target_row_and_col(self):
        result, coord = self.find_realm_raid_person_target_row_3()  # 查找第3行目标
        if result:
            self.click_in_circle([coord[0] - 80, coord[1] + 35], 30)
        else:
            result, coord = self.find_realm_raid_person_target_col_1()  # 查找第1列目标
            if result:
                self.click_in_circle([coord[0] - 80, coord[1] + 35], 30)
            else:
                result, coord = self.find_realm_raid_person_target_row_2()  # 查找第2行目标
                if result:
                    self.click_in_circle([coord[0] - 80, coord[1] + 35], 30)
                else:
                    result, coord = self.find_realm_raid_person_target_col_2()  # 查找第2列目标
                    if result:
                        self.click_in_circle([coord[0] - 80, coord[1] + 35], 30)
                    else:
                        result, coord = self.find_realm_raid_person_target_row_1()  # 查找第1行目标
                        if result:
                            self.click_in_circle([coord[0] - 80, coord[1] + 35], 30)
                        else:
                            result, coord = self.find_realm_raid_person_target_col_3()  # 查找第3列目标
                            if result:
                                self.click_in_circle([coord[0] - 80, coord[1] + 35], 30)
                            else:
                                # 找不到目标，设置刷新
                                self.need_to_refresh = True

    def find_realm_raid_guild_target(self):
        chapter_stage = self.product.chapter_stage
        find_target = False
        if chapter_stage:
            # 遍历星级
            for star in reversed(range(chapter_stage)):
                # 遍历区域
                for area in range(6):
                    result, coord = self.find_guild_realm_raid_medal(star, area)
                    if result:
                        if self.is_realm_raid_guild_target_failed(coord):
                            continue
                        else:
                            self.click_in_circle(coord)
                            find_target = True
                            break
                if find_target:
                    break
                else:
                    continue
            else:
                result, coord = self.find_guild_realm_raid_target_break()
                if result:
                    self.stop_flag = True
                else:
                    self.slide_up_guild_realm_raid_list()

    def processing_explore(self):
        signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
        if self.bonus_all_set or not self.config_bonus:
            if self.is_bonus_panel():
                self.close_bonus_panel()
            else:
                signal_run_list.set_current_operation.emit(self.run_id, "打开结界突破")
                if self.need_to_set_realm:
                    self.quit_explore()
                elif self.is_need_to_set_realm():
                    self.need_to_set_realm = True
                elif self.is_realm_raid_entrance():
                    self.open_realm_raid()
                elif not self.is_realm_raid_entrance():  # 没有结界突破入口， 设置结界突破完成
                    self.stop_flag = True
                    self.is_play_finished = True
        else:
            self.set_bonus(where="explore")

    def processing_stop(self):
        if self.is_realm_raid_refresh_confirm_button():
            self.confirm_refresh_realm_raid()
        elif self.is_realm_raid_panel():
            self.close_realm_raid_panel()
        elif self.is_battle_win_prize_daruma():
            self.process_battle_win_prize_daruma()
        elif self.is_battle_failed_drum():
            self.process_battle_failed_drum()
        elif self.is_battle_battling():
            self.processing_battling()
        elif self.is_explore():
            self.process_explore_after_task()
        elif self.is_yard():
            self.processing_yard()

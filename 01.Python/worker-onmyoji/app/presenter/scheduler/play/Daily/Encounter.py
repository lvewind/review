from ..Common import *


class PlayEncounter(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayEncounter, self).__init__(play_input)
        self.encounter_done = False
        self.encounter_prize_got = False
        self.encounter_1 = False
        self.encounter_2 = False
        self.encounter_3 = False
        self.encounter_4 = False

    def run(self):
        self.encounter_done = False
        self.encounter_prize_got = False
        self.encounter_1 = False
        self.encounter_2 = False
        self.encounter_3 = False
        self.encounter_4 = False
        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                if self.is_scene_after_battling:
                    if self.is_encounter_boss_mark_got_panel():
                        self.skip_encounter_boss_mark_got_panel()
                    elif self.is_battle_win_prize_daruma():
                        self.stop_flag = True
                else:
                    if self.is_battle_battling():
                        self.is_scene_after_battling = True
                    elif self.is_battle_ready():
                        self.set_battle_ready()
                    elif self.is_encounter_boss_mass_room():
                        pass
                    elif self.is_encounter_boss_panel():
                        if self.is_encounter_boss_confirm_panel():
                            if self.is_encounter_confirm_panel_checked():
                                self.confirm_encounter_boss_mass()
                            else:
                                self.check_encounter_confirm_panel()
                        elif self.is_encounter_boss_panel_time_up() or self.is_encounter_boss_panel_full():
                            self.close_encounter_boss_panel()
                        else:
                            self.click_encounter_panel_challenge_button()
                    elif self.is_encounter_map():
                        if self.encounter_done:
                            week_day = time.localtime(time.time())[6]
                            if week_day == 0:
                                result, coord = self.find_encounter_boss_guilingvgeji()  # 鬼灵歌妓
                                if result:
                                    self.click_in_circle(coord)
                                else:
                                    self.click_find_encounter_boss_button()
                            elif week_day == 1:
                                result, coord = self.find_encounter_boss_shenqilou()  # 蜃气楼
                                if result:
                                    self.click_in_circle(coord)
                                else:
                                    self.click_find_encounter_boss_button()
                            elif week_day == 2:
                                result, coord = self.find_encounter_boss_tuzhizhu()  # 土蜘蛛
                                if result:
                                    self.click_in_circle(coord)
                                else:
                                    self.click_find_encounter_boss_button()
                            elif week_day == 3:
                                result, coord = self.find_encounter_boss_huangkulou()  # 荒骷髅
                                if result:
                                    self.click_in_circle(coord)
                                else:
                                    self.click_find_encounter_boss_button()
                            elif week_day == 4:
                                result, coord = self.find_encounter_boss_dizhennian()  # 地震鲶
                                if result:
                                    self.click_in_circle(coord)
                                else:
                                    self.click_find_encounter_boss_button()
                            elif week_day == 5:
                                result, coord = self.find_encounter_boss_longche()  # 胧车
                                if result:
                                    self.click_in_circle(coord)
                                else:
                                    self.click_find_encounter_boss_button()
                        else:
                            result, coord = self.find_collection_prize_panel_common()
                            if result:
                                self.click_in_circle([coord[0] + 255, coord[1]])
                            else:
                                if self.encounter_prize_got:
                                    if not self.encounter_1:
                                        self.check_encounter_step(1)
                                    elif not self.encounter_2:
                                        self.check_encounter_step(2)
                                    elif not self.encounter_3:
                                        self.check_encounter_step(3)
                                    elif not self.encounter_4:
                                        self.check_encounter_step(4)
                                    else:
                                        self.encounter_done = True
                                else:
                                    if self.is_encounter_prize_got():
                                        self.encounter_prize_got = True
                                    elif self.is_encounter_use_up():
                                        self.click_encounter_prize_got()
                                    else:
                                        self.click_encounter_button_4()
                    elif self.is_daily_panel_daily():
                        if self.is_daily_encounter_entrance_panel():
                            if self.is_daily_goto_button():
                                self.click_daily_go_to_button()
                            else:
                                self.stop_flag = True
                        elif self.is_daily_encounter_entrance():
                            self.open_encounter_panel()
                    elif self.is_explore():
                        self.quit_explore()
                    else:
                        self.open_daily_panel_in_yard()
            else:
                if self.is_yard() or self.is_explore():
                    self.stop_status = True
                elif self.is_encounter_boss_mass_room():
                    self.quit_encounter_map()
                elif self.is_encounter_boss_mark_got_panel():
                    self.skip_encounter_boss_mark_got_panel()
                elif self.is_battle_win_prize_daruma():
                    self.skip_battle_win_prize(random.randint(1, 3))

    def check_encounter_step(self, step: int):
        if step == 1:
            if self.is_encounter_mail_panel():  # 密信面板
                self.check_mail_answer()
            elif self.is_encounter_box_panel():  # 宝箱面板
                if self.is_encounter_box_panel_amulet():
                    self.click_encounter_box_panel_button()
                else:
                    while self.is_encounter_box_panel():
                        self.close_encounter_box_panel()
                    else:
                        self.encounter_1 = True
            elif self.is_encounter_task_1():  # 任务图标
                self.encounter_1 = True
            elif self.is_encounter_finish_1():  # 封
                self.encounter_1 = True
            else:
                self.click_encounter_1()
        elif step == 2:
            if self.is_encounter_mail_panel():  # 密信面板
                self.check_mail_answer()
            elif self.is_encounter_box_panel():  # 宝箱面板
                if self.is_encounter_box_panel_amulet():
                    self.click_encounter_box_panel_button()
                else:
                    while self.is_encounter_box_panel():
                        self.close_encounter_box_panel()
                    else:
                        self.encounter_2 = True
            elif self.is_encounter_task_2():  # 任务图标
                self.encounter_2 = True
            elif self.is_encounter_finish_2():  # 封
                self.encounter_2 = True
            else:
                self.click_encounter_2()
        elif step == 3:
            if self.is_encounter_mail_panel():  # 密信面板
                self.check_mail_answer()
            elif self.is_encounter_box_panel():  # 宝箱面板
                if self.is_encounter_box_panel_amulet():
                    self.click_encounter_box_panel_button()
                else:
                    while self.is_encounter_box_panel():
                        self.close_encounter_box_panel()
                    else:
                        self.encounter_3 = True
            elif self.is_encounter_task_3():  # 任务图标
                self.encounter_3 = True
            elif self.is_encounter_finish_3():  # 封
                self.encounter_3 = True
            else:
                self.click_encounter_3()
        elif step == 4:
            if self.is_encounter_mail_panel():  # 密信面板
                self.check_mail_answer()
            elif self.is_encounter_box_panel():  # 宝箱面板
                if self.is_encounter_box_panel_amulet():
                    self.click_encounter_box_panel_button()
                else:
                    while self.is_encounter_box_panel():
                        self.close_encounter_box_panel()
                    else:
                        self.encounter_4 = True
            elif self.is_encounter_task_4():  # 任务图标
                self.encounter_4 = True
            elif self.is_encounter_finish_4():  # 封
                self.encounter_4 = True
            else:
                self.click_encounter_4()

    def check_mail_answer(self):
        if random.randint(1, 3) == 1:
            self.check_encounter_mail_panel_answer_1()
        elif random.randint(1, 3) == 2:
            self.check_encounter_mail_panel_answer_2()
        elif random.randint(1, 3) == 3:
            self.check_encounter_mail_panel_answer_3()

    def close_encounter_box_panel(self):
        if random.randint(1, 3) == 1:
            self.close_encounter_box_panel_1()
        elif random.randint(1, 3) == 2:
            self.close_encounter_box_panel_2()
        elif random.randint(1, 3) == 3:
            self.close_encounter_box_panel_3()
        time.sleep(1)

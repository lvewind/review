import random
import time

from app.presenter.data import *
from app.presenter.scheduler.RunStatus import run_status, task_record
from hiworker import Thread
from app.presenter.scheduler.click import Operate
from app.presenter.scheduler.detect import Detect
from app.presenter.sender import signal_run_list, signal_counter_record
from app.presenter.scheduler.play.Common.PlayInput import PlayInput


class Common(Detect, Operate, Thread):
    def __init__(self, play_input: PlayInput):
        self.play_input = play_input
        self.run_id = self.play_input.run_list.id
        self.product = play_input.current_product
        self.run_status = run_status
        self.product_record = task_record
        window_title = "[#] [" + self.play_input.run_env.name + "] 阴阳师-网易游戏 [#]"

        super(Detect, self).__init__()
        super(Detect, self).set_data(window_title, im_data, coord_data)
        super(Detect, self).set_handle_option(offset_x=self.play_input.app_setting.offset_x,
                                              offset_y=self.play_input.app_setting.offset_y)
        super(Operate, self).__init__()
        super(Operate, self).set_data(window_title, coord_data)
        super(Operate, self).set_handle_option(offset_x=self.play_input.app_setting.offset_x,
                                               offset_y=self.play_input.app_setting.offset_y)
        Thread.__init__(self)

        self.can_team_up = False
        self.stage_selected = False
        self.cast_lock_set = False
        self.cast_lock_up = False
        self.auto_doll_set = False
        self.doll_active = False
        self.counter = 0
        self.preset_count = 0
        self.config_bonus = True
        self.bonus = False
        self.bonus_off = False

        self.bonus_status = {"soul": 0, "evo": 0, "exp_100": 0, "exp_50": 0, "coin_100": 0, "coin_50": 0}
        self.bonus_status_total = False

        self.bonus_set = {"soul": False, "evo": False, "exp_100": False, "exp_50": False, "coin_100": False, "coin_50": False}
        self.bonus_all_set = False
        self.bonus_off_total = False

        self.invite_status = False
        self.invite_time_start = 0
        self.invite_time_end = 0
        self.run_time = 0

        self.is_scene_after_battling = False
        self.teamup_mode = 0
        self.team_position = ""
        self.auto_invite_prepare = False
        self.auto_invite = False
        self.auto_accept_prepare = False
        self.auto_accept = False

        self.current_step = 0
        self.is_finished = False
        self.is_play_finished = False
        self.play_sleep_time = 0.2

        self.is_doll_auto_feed = False

        self.start_time = 0
        self.running_time = 0
        self.waite_for_time = False

        self.is_novice_mode = False
        self.is_story_lock = False
        self.is_battle_failed = 0

        self.ap_use_up = False

        self.approximate_count_set = False

        self.after_boss_battle = False
        self.is_kick_boss = False

        # self.set_detect_option(cpu_down_time=round(self.play_input.app_setting.cpu_sleep_time / 15, 1))
        self.cpu_down_time = (self.play_input.app_setting.cpu_sleep_time / 100)

    def sleep_in_run(self, *args):
        if len(args) > 0:
            if type(args[0]) == float:
                time.sleep(args[0])
        elif self.play_input.app_setting.cpu_sleep_time:
            time.sleep(round(self.play_input.app_setting.cpu_sleep_time / 10, 1))
        else:
            time.sleep(0.1)

    def set_run_status_default(self):
        self.is_scene_after_battling = False
        self.is_finished = False
        self.is_play_finished = False
        self.stop_flag = False
        self.stop_status = False
        self.doll_active = False
        self.is_doll_auto_feed = False
        self.auto_doll_set = False
        self.counter = 0
        self.start_time = time.time()
        self.running_time = 0
        self.is_battle_failed = 0
        self.is_story_lock = False
        self.ap_use_up = False
        self.approximate_count_set = False

        self.after_boss_battle = False
        self.is_kick_boss = False
        if self.play_input.run_list.teamup_mode == "single_solo" or self.play_input.run_list.teamup_mode == "double_captain" \
                or self.play_input.run_list.teamup_mode == "free_captain":
            self.team_position = "captain"
        else:
            self.team_position = "teammate"
        play_name = "".join([
            data_chs.product.get(str(self.product.play_name)), "·",
            data_chs.product.get(str(self.product.play_name_second)), "·",
            data_chs.product.get(str(self.product.chapter_stage))
        ])
        signal_run_list.set_current_product.emit(self.run_id, play_name)

    def set_preset_count(self):
        if not self.preset_count:
            preset_count = self.product.preset_count
            if self.product.approximate_count:
                if random.randint(0, 1):
                    self.preset_count = preset_count + random.randint(1, (int(preset_count * 0.2) + 1))
                else:
                    self.preset_count = preset_count - random.randint(1, (int(preset_count * 0.2) + 1))
            else:
                self.preset_count = preset_count
            print("preset_count", self.preset_count)

    def is_teammate_finished(self):
        return task_record.get_record_finish_status(self.play_input.teammate_task_record_id)

    def set_bonus(self, where="explore", set_on=True):
        if self.is_bonus_panel():
            if self.is_new_area_bonus():  # 新区超绝加成
                self.bonus_all_set = 1
            else:
                bonus_need_set_on = {
                    "soul": True if (self.product.bonus_soul and self.product.play_name == "souls" and set_on) else False,
                    "evo": True if (self.product.bonus_evo and self.product.play_name == "evo_materials" and set_on) else False,
                    "exp_100": True if (self.product.bonus_exp_100 and set_on) else False,
                    "exp_50": True if (self.product.bonus_exp_50 and set_on) else False,
                    "coin_100": True if (self.product.bonus_coin_100 and set_on) else False,
                    "coin_50": True if (self.product.bonus_coin_50 and set_on) else False
                }
                for bonus_name in self.bonus_set.keys():
                    if not self.bonus_set.get(bonus_name):
                        signal_run_list.set_current_operation.emit(self.run_id, "设置" + data_chs.bonus.get(bonus_name, ""))
                        result, coord = False, [0, 0]
                        if bonus_name == "evo":
                            result, coord = self.find_bonus_evo()  # 查找觉醒加成
                            coord = [coord[0] + 153, coord[1] + 2]
                        elif bonus_name == "soul":
                            result, coord = self.find_bonus_souls()
                            coord = [coord[0] + 153, coord[1] + 2]
                        elif bonus_name == "exp_100":
                            result, coord = self.find_bonus_exp_100()
                            coord = [coord[0] + 170, coord[1] + 5]
                        elif bonus_name == "exp_50":
                            result, coord = self.find_bonus_exp_50()
                            coord = [coord[0] + 178, coord[1] + 5]
                        elif bonus_name == "coin_100":
                            result, coord = self.find_bonus_coin_100()
                            coord = [coord[0] + 173, coord[1] + 5]
                        elif bonus_name == "coin_50":
                            result, coord = self.find_bonus_coin_50()
                            coord = [coord[0] + 177, coord[1]]
                        if result:
                            if bonus_need_set_on.get(bonus_name):
                                while (not self.bonus_status.get(bonus_name) == 1) and (not self.stop_flag):
                                    if self.is_bonus_on(coord):
                                        self.bonus_status[bonus_name] = 1
                                        self.bonus_set[bonus_name] = True
                                    else:
                                        self.change_bonus_status(coord)
                                        break
                            else:
                                while not self.bonus_status.get(bonus_name) == -1:
                                    if self.is_bonus_on(coord):
                                        self.change_bonus_status(coord)
                                        break
                                    else:
                                        self.bonus_status[bonus_name] = -1
                                        self.bonus_set[bonus_name] = True
                            time.sleep(0.2)
                        else:
                            self.bonus_status[bonus_name] = -1
                            self.bonus_set[bonus_name] = True
                else:
                    self.bonus_set = {"soul": False, "evo": False, "exp_100": False, "exp_50": False, "coin_100": False, "coin_50": False}
                    if set_on:
                        self.bonus_all_set = True
                        self.bonus_off_total = False
                    else:
                        self.bonus_all_set = False
                        self.bonus_off_total = True
        elif where == "explore":
            self.sleep_in_run(2)
            result, coord = self.find_bonus_button_in_explore()
            if result:
                signal_run_list.set_current_operation.emit(self.run_id, "打开加成面板")

                self.click_in_circle(coord)
            else:
                self.bonus_all_set = 1
        elif where == "cooperation_teamup":
            if self.is_bonus_button_in_cooperation_teamup():
                signal_run_list.set_current_operation.emit(self.run_id, "打开加成面板")
                self.open_bonus_panel_teamup()
            else:
                self.bonus_all_set = 1
        elif where == "yard":
            if self.is_bonus_button_in_yard():
                signal_run_list.set_current_operation.emit(self.run_id, "打开加成面板")
                self.open_bonus_panel_yard()
            else:
                self.bonus_all_set = 1

    # 战斗结束
    def processing_battle_ready(self):
        if self.doll_active:
            signal_run_list.set_current_operation.emit(self.run_id, "自动准备")
        else:
            time.sleep(1)
            if self.is_battle_ready():
                signal_run_list.set_current_operation.emit(self.run_id, "战斗准备")
                self.set_battle_ready()

    def processing_battling(self):
        signal_run_list.set_current_scene.emit(self.run_id, "战斗中")
        run_status.set_cooperation_teamup_standby_status(self.run_id, False)
        if self.is_battle_auto():
            signal_run_list.set_current_operation.emit(self.run_id, "等待战斗结束")
            self.is_scene_after_battling = True
        elif self.is_battle_manual():
            signal_run_list.set_current_operation.emit(self.run_id, "设置自动")
            self.change_auto_battle()

    def processing_after_battle(self):
        if self.is_battle_win_prize_daruma():  # 战斗奖励
            self.processing_battle_win_prize()
        elif self.is_battle_win_drum() or self.is_battle_win_drum_evo():  # 战斗胜利
            signal_run_list.set_current_scene.emit(self.run_id, "战斗胜利")
            if self.doll_active:
                signal_run_list.set_current_operation.emit(self.run_id, "自动胜利")
            else:
                signal_run_list.set_current_operation.emit(self.run_id, "跳过胜利")
                self.skip_battle_win(random.randint(1, 3))
        elif self.is_battle_failed_drum():  # 失败鼓
            self.processing_battle_failed()
        elif self.is_explore():
            self.is_scene_after_battling = False
            self.auto_invite = False
            signal_run_list.set_current_scene.emit(self.run_id, "探索")
        elif self.is_disconnected():
            self.confirm_disconnected()
        elif self.is_realm_raid_panel():
            self.is_scene_after_battling = False

    def processing_battle_failed(self):
        signal_run_list.set_current_scene.emit(self.run_id, "战斗失败")
        signal_run_list.set_current_operation.emit(self.run_id, "跳过失败")
        while self.is_battle_failed_drum():
            if self.is_battle_failed_continue_to_invite():
                self.confirm_continue_to_invite()
            else:
                self.skip_battle_failed(random.randint(1, 3))
        else:
            self.is_scene_after_battling = False
            if self.product.use_yingbing:
                self.auto_doll_set = False
                self.doll_active = False
            if self.is_novice_mode:
                self.is_battle_failed += 1

    def processing_battle_win_prize(self):
        signal_run_list.set_current_scene.emit(self.run_id, "战利品")
        while self.is_battle_win_prize_daruma():
            if self.doll_active:
                signal_run_list.set_current_operation.emit(self.run_id, "自动领取")
            else:
                signal_run_list.set_current_operation.emit(self.run_id, "领取奖励")
                self.skip_battle_win_prize(random.randint(1, 3))
                time.sleep(random.randint(5, 8) / 10)
        else:
            self.is_scene_after_battling = False
            self.counter += 1
            self.upgrade_daily_counter()
            if self.product.use_yingbing:
                self.auto_doll_set = False
                self.doll_active = False
            if self.is_kick_boss:
                self.after_boss_battle = True
            else:
                self.after_boss_battle = False

    def processing_auto_invite_after_battle(self):
        if self.is_battle_auto_invite_panel():
            if self.product.preset_count <= 1:
                self.cancel_auto_accept_panel()
            signal_run_list.set_current_operation.emit(self.run_id, "继续邀请")
            if self.is_battle_auto_invite_checked():
                self.confirm_auto_invite()
                time.sleep(random.randint(5, 8) / 10)
                if not self.is_battle_auto_invite_panel():
                    self.auto_invite = True
            else:
                self.check_battle_auto_invite()

    # 组队邀请
    def processing_teamup(self):
        signal_run_list.set_current_scene.emit(self.run_id, "组队界面")
        if self.is_create_team_panel():
            if self.play_input.run_list.teamup_mode == "free_captain":
                if self.is_create_team_panel_any_selected():
                    signal_run_list.set_current_operation.emit(self.run_id, "创建队伍")
                    self.create_team_2()
                else:
                    signal_run_list.set_current_operation.emit(self.run_id, "设置队伍权限")
                    self.select_create_team_panel_any()
            elif self.play_input.run_list.teamup_mode == "free_captain_with_friend":
                if self.is_create_team_panel_friend_selected():
                    signal_run_list.set_current_operation.emit(self.run_id, "创建队伍")
                    self.create_team_2()
                else:
                    signal_run_list.set_current_operation.emit(self.run_id, "设置队伍权限")
                    self.select_create_team_panel_friend()
            elif self.play_input.run_list.teamup_mode == "double_captain":
                if self.is_create_team_panel_only_selected():
                    signal_run_list.set_current_operation.emit(self.run_id, "创建队伍")
                    self.create_team_2()
                else:
                    signal_run_list.set_current_operation.emit(self.run_id, "设置队伍权限")
                    self.select_create_team_panel_only()
        else:
            self.create_team_1()

    def processing_cooperation_teamup(self):
        signal_run_list.set_current_scene.emit(self.run_id, "协战队伍")
        self.after_boss_battle = False
        if self.auto_doll_set:
            if self.team_position == "captain":
                if self.doll_active:
                    if self.play_input.run_list.teamup_mode == "double_captain":
                        self.cooperation_teamup_invite_friend()
                    else:
                        signal_run_list.set_current_operation.emit(self.run_id, "等待队友加入")
                else:
                    if self.is_cooperation_teamup_challenge_button_yellow() or self.is_cooperation_teamup_challenge_button_yellow_longche():
                        if run_status.get_cooperation_teamup_standby_status(self.play_input.teammate.id):  # 队友组队界面已就绪
                            signal_run_list.set_current_operation.emit(self.run_id, "开始挑战")
                            self.challenge_cooperation_teamup()
                        else:
                            signal_run_list.set_current_operation.emit(self.run_id, "等待队友设置")
                    else:
                        if self.play_input.run_list.teamup_mode == "double_captain":
                            self.cooperation_teamup_invite_friend()
                        else:
                            signal_run_list.set_current_operation.emit(self.run_id, "等待队友加入")
            else:
                if self.is_cooperation_teamup_challenge_button_gray() or self.is_cooperation_teamup_challenge_button_gray_longche():  # 队友变成队长，退出组队
                    if self.is_cooperation_teamup_panel_confirm_quit():
                        self.confirm_quit_cooperation_teamup_panel()
                    else:
                        self.close_cooperation_teamup_panel()
                else:
                    signal_run_list.set_current_operation.emit(self.run_id, "等待挑战")
                    run_status.set_cooperation_teamup_standby_status(self.run_id, True)
        elif self.cast_lock_set:
            self.set_cooperation_teamup_doll()
        elif self.bonus_set:
            self.set_cooperation_teamup_cast_lock()
        else:
            self.set_bonus("cooperation_teamup")

    def cooperation_teamup_invite_friend(self):
        if self.invite_status or self.auto_invite:
            signal_run_list.set_current_operation.emit(self.run_id, "等待队友接受")
            if time.time() - self.invite_time_start > 15:
                self.invite_status = False
        elif self.is_cooperation_teamup_friend_panel():
            if self.is_cooperation_teammate_selected():
                signal_run_list.set_current_operation.emit(self.run_id, "发送邀请")
                self.click_cooperation_teamup_friend_panel_invite_button()
                self.invite_status = True
                self.invite_time_start = time.time()
            elif self.play_input.run_list.teammate_type == 1:
                signal_run_list.set_current_operation.emit(self.run_id, "查找默认")
                self.find_and_select_teammate()
            elif self.play_input.run_list.teammate_type == 2:
                signal_run_list.set_current_operation.emit(self.run_id, "查找好友")
                if self.product.play_name == "chapter":
                    if self.is_cooperation_teamup_friend_panel_friend_chapter():
                        self.find_and_select_teammate()
                    else:
                        self.select_cooperation_teamup_friend_panel_friend_chapter()
                else:
                    if self.is_cooperation_teamup_friend_panel_friend():
                        self.find_and_select_teammate()
                    else:
                        self.select_cooperation_teamup_friend_panel_friend()
            elif self.play_input.run_list.teammate_type == 3:
                signal_run_list.set_current_operation.emit(self.run_id, "查找寮友")
                if self.is_cooperation_teamup_friend_panel_guild():
                    self.find_and_select_teammate()
                else:
                    self.select_cooperation_teamup_friend_panel_guild()
            elif self.play_input.run_list.teammate_type == 4:
                signal_run_list.set_current_operation.emit(self.run_id, "查找最近")
                if self.is_cooperation_teamup_friend_panel_recent():
                    self.find_and_select_teammate()
                else:
                    self.select_cooperation_teamup_friend_panel_recent()
            elif self.play_input.run_list.teammate_type == 5:
                signal_run_list.set_current_operation.emit(self.run_id, "查找跨服")
                if self.is_cooperation_teamup_friend_panel_cross():
                    self.find_and_select_teammate()
                else:
                    self.select_cooperation_teamup_friend_panel_cross()

        else:
            signal_run_list.set_current_operation.emit(self.run_id, "打开邀请面板")
            if self.product.play_name == "chapter":
                self.click_invite_teammate_plus_button_right()
            else:
                self.click_invite_teammate_plus_button()

    def find_and_invite_teammate(self):
        if self.invite_status or self.auto_invite:
            signal_run_list.set_current_operation.emit(self.run_id, "等待队友接受")
            if time.time() - self.invite_time_start > 15:
                self.invite_status = False
        elif self.is_cooperation_teamup_friend_panel():
            if self.is_cooperation_teammate_selected():
                signal_run_list.set_current_operation.emit(self.run_id, "发送邀请")
                self.click_cooperation_teamup_friend_panel_invite_button()
                self.invite_status = True
                self.invite_time_start = time.time()
            elif self.play_input.run_list.teammate_type == "default":
                signal_run_list.set_current_operation.emit(self.run_id, "查找默认")
                self.find_and_select_teammate()
            elif self.play_input.run_list.teammate_type == "friend":
                signal_run_list.set_current_operation.emit(self.run_id, "查找好友")
                if self.is_cooperation_teamup_friend_panel_friend():
                    self.find_and_select_teammate()
                else:
                    self.select_cooperation_teamup_friend_panel_friend()
            elif self.play_input.run_list.teammate_type == "recent":
                signal_run_list.set_current_operation.emit(self.run_id, "查找最近")
                if self.is_cooperation_teamup_friend_panel_recent():
                    self.find_and_select_teammate()
                else:
                    self.select_cooperation_teamup_friend_panel_recent()
            elif self.play_input.run_list.teammate_type == "cross":
                signal_run_list.set_current_operation.emit(self.run_id, "查找跨服")
                if self.is_cooperation_teamup_friend_panel_cross():
                    self.find_and_select_teammate()
                else:
                    self.select_cooperation_teamup_friend_panel_cross()
            elif self.play_input.run_list.teammate_type == "guild":
                signal_run_list.set_current_operation.emit(self.run_id, "查找寮友")
                if self.is_cooperation_teamup_friend_panel_guild():
                    self.find_and_select_teammate()
                else:
                    self.select_cooperation_teamup_friend_panel_guild()
        else:
            signal_run_list.set_current_operation.emit(self.run_id, "打开邀请面板")
            self.click_invite_teammate_plus_button()

    def find_and_select_teammate(self):
        teammate_teamup_img = self.play_input.teammate_account.teamup_img
        if teammate_teamup_img:
            result, coord, max_similarity = self.find_in_different_template_rect(teammate_teamup_img, "team_find_teammate_area", similarity=0.7)
            if result:
                self.click_in_circle(coord)
            else:
                self.slide_up_cooperation_friend_list()
        else:
            print("列表 " + str(self.run_id) + "的队友组队图片异常")
            self.stop()

    def accept_invite_common(self):
        result, coord = self.find_invite_accpet_auto_button()
        if result:
            self.accept_invite_auto(coord)
            self.auto_accept_prepare = True
        else:
            self.accept_invite()

    def set_cooperation_teamup_doll(self):
        signal_run_list.set_current_operation.emit(self.run_id, "设置樱饼")
        if self.product.use_yingbing:
            if self.is_doll_auto_feed:  # 自动喂食已开启
                if self.is_cooperation_hunger():  # 依旧饥饿
                    self.auto_doll_set = True
                    self.doll_active = False
                else:
                    if self.is_cooperation_doll_active():
                        self.doll_active = True
                        self.auto_doll_set = True
                    else:
                        # 这里需要检测
                        self.change_cooperation_doll_active()
            else:
                if self.is_feed_doll_panel():
                    if self.is_feed_doll_panel_auto_feed_active():
                        self.is_doll_auto_feed = True

                    else:
                        self.set_feed_doll_panel_auto_feed_active()
                else:
                    self.open_cooperation_feed_doll_panel()
        else:
            if self.is_cooperation_doll_active():
                self.change_cooperation_doll_active()
            else:
                self.auto_doll_set = True
                self.doll_active = False

    def set_cooperation_teamup_cast_lock(self):
        signal_run_list.set_current_operation.emit(self.run_id, "设置锁定")
        if self.product.lock_cast:
            if self.is_cooperation_cast_lock_up() or self.is_cooperation_cast_lock_up_longche():
                self.cast_lock_up = True
                self.cast_lock_set = True
            elif self.is_cooperation_cast_not_lock_up():
                self.change_cooperation_cast_lock()
            elif self.is_cooperation_cast_not_lock_up_longche():
                self.change_cooperation_cast_lock_longche()
        else:
            if self.is_cooperation_cast_not_lock_up():
                self.change_cooperation_doll_active()
                self.cast_lock_up = False
                self.cast_lock_set = True
            else:
                self.change_cooperation_cast_lock()

    def upgrade_daily_counter(self):
        current_day = time.localtime()
        record_id = "".join([
            str(current_day.tm_year),
            str(current_day.tm_mon),
            str(current_day.tm_mday),
            str(self.run_id),
            str(self.play_input.account.id)])
        signal_counter_record.increase_record_item_value_by_record_id.emit(record_id, self.product.counter_item)
        signal_run_list.load_run_list_counter_item.emit(self.run_id, self.product.counter_item)

    def open_daily_panel_in_yard(self):
        if self.is_yard():
            result, coord = self.is_daily_panel_entrance()
            print("查找活动入口")
            if result:
                self.click_in_circle(coord)
            else:
                self.slide_yard_to_left()

    def process_battle_win_prize_daruma(self):
        click_position = random.randint(1, 3)
        signal_run_list.set_current_operation.emit(self.run_id, "领取奖励")
        while self.is_battle_win_prize_daruma():
            self.skip_battle_win_prize(click_position)
            time.sleep(random.randint(3, 8) / 10)
        else:
            self.upgrade_daily_counter()
            self.is_scene_after_battling = False

    def process_battle_failed_drum(self):
        click_position = random.randint(1, 3)
        signal_run_list.set_current_operation.emit(self.run_id, "跳过失败")
        while self.is_battle_failed_drum():
            self.skip_battle_failed(click_position)
        else:
            self.is_scene_after_battling = False

    def processing_yard(self):
        signal_run_list.set_current_scene.emit(self.run_id, "庭院")
        signal_run_list.set_current_operation.emit(self.run_id, "进入探索地图")
        if self.is_explore_entrance():
            self.open_explore()
        elif self.is_explore_entrance_left():
            self.open_explore_left()
        else:
            self.slide_yard_to_right()

    def process_explore_after_task(self):
        signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
        if self.is_continue_invite_chapter_panel():
            self.cancel_continue_invite_chapter_panel()
        elif not self.bonus_off_total and self.config_bonus:
            self.set_bonus(set_on=False)
        else:
            if self.is_bonus_panel():
                self.close_bonus_panel()
            else:
                signal_run_list.set_current_operation.emit(self.run_id, " ")
                run_status.set_play_standby_status(self.run_id, False)
                self.is_play_finished = self.stop_status = True
                self.stop_flag = False

    def process_quit_cooperation_teamup_panel(self):
        if self.is_cooperation_teamup_panel_confirm_quit():
            self.confirm_quit_cooperation_teamup_panel()
            time.sleep(1.2)
        else:
            self.close_cooperation_teamup_panel()

    def check_chat_panel(self):
        # if self.is_bounty_seals_invite_panel():
        #     self.close_bounty_seals_panel()
        if self.is_chat_panel():
            self.close_chat_panel()

    # 设置阵容、樱饼
    def check_cast_lock_in_stage_panel(self):
        signal_run_list.set_current_operation.emit(self.run_id, "设置阵容锁定")
        if self.product.lock_cast:
            if self.is_souls_cast_lock():
                self.cast_lock_set = True
                self.cast_lock_up = True
            elif self.is_souls_cast_unlock():
                self.lock_souls_cast()
        elif self.is_souls_cast_unlock():
            self.cast_lock_set = True
            self.cast_lock_up = False
        elif self.is_souls_cast_lock():
            self.unlock_souls_cast()

    def check_auto_doll_in_stage_panel(self):
        signal_run_list.set_current_operation.emit(self.run_id, "设置小纸人")
        if self.product.use_yingbing:
            if self.is_doll_auto_feed:  # 自动喂食已开启
                if self.is_souls_doll_orochi_hunger() or self.is_souls_doll_sougenbi_hunger() or self.is_souls_doll_himiko_hunger():  # 依旧饥饿
                    self.auto_doll_set = True
                    self.doll_active = False
                else:
                    if self.is_souls_auto_challenge_active():  # 已喂饱工人
                        self.auto_doll_set = True
                        self.doll_active = True
                    else:
                        self.change_souls_auto_challenge()
            else:
                if self.is_feed_doll_panel():
                    if self.is_feed_doll_panel_auto_feed_active():
                        self.is_doll_auto_feed = True

                    else:
                        self.set_feed_doll_panel_auto_feed_active()
                else:
                    self.open_souls_feed_doll_panel()
        elif self.is_souls_auto_challenge_active():
            self.change_souls_auto_challenge()
        else:
            self.auto_doll_set = True
            self.doll_active = False

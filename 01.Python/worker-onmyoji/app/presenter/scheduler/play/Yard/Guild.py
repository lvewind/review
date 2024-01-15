from ..Common import *


class PlayGuild(Common):
    def __init__(self, play_input: PlayInput):
        super(PlayGuild, self).__init__(play_input)
        self.guild_daily_finish = False
        self.guild_coin_finish = False
        self.guild_contribute_finish = False
        self.guild_invocation_finish = False
        self.guild_task_finish = False
        self.realm_ap_finish = False

        self.guild_realm_finish = False
        self.guild_foster = False
        self.realm_cultivate = False

        self.guild_mall_finish = False
        self.yingbing_buy = False
        self.grade_daruma_buy = False
        self.souls_buy = False
        self.amulet_buy = False
        self.skill_daruma_buy = False
        self.skin_ticket_buy = False

        self.guild_realm_card_setting_finish = False
        self.guild_realm_card_synthesis_finish = False

        self.is_realm_shikigami_full = False
        self.is_dog_food_list_set = False

        self.is_realm_card_type_set = False
        self.is_realm_card_synthesis_continue_button_clicked = False
        self.is_realm_foster_selected = False

    def run(self):

        self.set_run_status_default()
        while not self.stop_status:
            self.check_chat_panel()
            if not self.stop_flag:
                play_name_second = self.product.play_name_second
                if play_name_second == "guild_daily" and not self.guild_daily_finish:
                    self.run_guild_daily()
                elif play_name_second == "guild_realm" and not self.guild_realm_finish:
                    self.run_guild_realm()
                elif play_name_second == "guild_mall" and not self.finish:
                    self.run_guild_mall()
                elif play_name_second == "guild_realm_card_setting" and not self.guild_realm_card_setting_finish:
                    self.run_guild_contribute()
                elif play_name_second == "guild_realm_card_synthesis" and not self.guild_realm_card_synthesis_finish:
                    self.run_guild_contribute()
                else:
                    self.is_finished = True
            else:
                self.run_status.set_play_standby_status(self.run_id, False)
                self .processing_stop()
                self.sleep_in_run()

    def run_guild_daily(self):
        if not self.guild_coin_finish:
            if self.product.guild_coin:
                if self.is_guild_panel():
                    if self.find_collection_prize_panel_common():
                        self.is_finished = True
                        self.close_guild_panel()
                    elif self.is_guild_get_coin_confirm_button():
                        self.confirm_get_guild_coin()
                    elif self.is_guild_get_coin_button_not_get():
                        self.get_guild_coin()
                    else:
                        self.is_finished = True
                else:
                    self.open_guild_panel()
            else:
                self.guild_coin_finish = True
        elif not self.guild_contribute_finish:
            if self.product.guild_contribute:
                if self.is_guild_panel():
                    result, coord = self.find_collection_prize_panel_common()
                    if result:
                        self.is_finished = True
                    else:
                        if self.is_guild_contribute_jade_panel():
                            chapter_stage = str(self.product.chapter_stage)
                            if chapter_stage == "100":
                                if self.is_guild_contribute_jade_button_100() or self.is_guild_contribute_jade_slide_right():
                                    self.click_guild_contribute_jade_button_100()
                                else:
                                    current_contribute_jade = self.check_current_contribute_jade()
                                    if current_contribute_jade < 100:
                                        self.add_contribute_guild_jade()
                            elif chapter_stage == "80":
                                if self.is_guild_contribute_jade_button_80() or self.is_guild_contribute_jade_slide_right():
                                    self.click_guild_contribute_jade_button_80()
                                else:
                                    current_contribute_jade = self.check_current_contribute_jade()
                                    if current_contribute_jade < 80:
                                        self.add_contribute_guild_jade()
                                    elif current_contribute_jade > 80:
                                        self.dec_contribute_guild_jade()
                            elif chapter_stage == "60":
                                if self.is_guild_contribute_jade_button_60() or self.is_guild_contribute_jade_slide_right():
                                    self.click_guild_contribute_jade_button_60()
                                else:
                                    current_contribute_jade = self.check_current_contribute_jade()
                                    if current_contribute_jade < 60:
                                        self.add_contribute_guild_jade()
                                    elif current_contribute_jade > 60:
                                        self.dec_contribute_guild_jade()
                            elif chapter_stage == "40":
                                if self.is_guild_contribute_jade_button_40() or self.is_guild_contribute_jade_slide_right():
                                    self.click_guild_contribute_jade_button_40()
                                else:
                                    current_contribute_jade = self.check_current_contribute_jade()
                                    if current_contribute_jade < 40:
                                        self.add_contribute_guild_jade()
                                    elif current_contribute_jade > 40:
                                        self.dec_contribute_guild_jade()
                            elif chapter_stage == "20":
                                if self.is_guild_contribute_jade_button_20() or self.is_guild_contribute_jade_slide_right():
                                    self.click_guild_contribute_jade_button_20()
                                else:
                                    current_contribute_jade = self.check_current_contribute_jade()
                                    if current_contribute_jade < 20:
                                        self.add_contribute_guild_jade()
                                    elif current_contribute_jade > 20:
                                        self.dec_contribute_guild_jade()
                        else:
                            self.open_guild_contribute_panel()
                else:
                    self.open_guild_panel()
            else:
                self.guild_contribute_finish = True
        elif not self.guild_invocation_finish:
            if self.product.guild_invocation:
                pass
            else:
                self.guild_invocation_finish = True
        elif not self.guild_task_finish:
            if self.product.guild_task_contribute or self.product.guild_task:
                if self.is_guild_shrine_guild_task_panel():
                    chapter_stage = self.product.chapter_stage
                    if chapter_stage == "task_30":
                        if self.is_guild_task_battle_30():
                            result, coord = self.find_collection_prize_panel_common()
                            if result:
                                pass
                            elif self.is_guild_task_battle_30_get_prize_button():
                                self.get_guild_task_battle_30_prize()
                            else:
                                self.close_guild_task_panel()
                    elif chapter_stage == "evo_materials":
                        pass
                    elif chapter_stage == "souls":
                        pass
                elif self.is_guild_panel():
                    if self.is_guild_panel_shrine():
                        self.open_guild_shrine_guild_task()
                    else:
                        self.select_guild_panel_shrine()
                else:
                    self.open_guild_panel()
            else:
                self.guild_task_finish = True
        elif not self.realm_ap_finish:
            if self.product.realm_ap:
                if self.is_guild_realm_ap_exp_panel():
                    if self.is_guild_realm_get_ap_panel():
                        result, coord = self.find_collection_prize_panel_common()
                        if result:
                            self.realm_ap_finish = True
                        elif self.is_guild_realm_get_ap_use_up():
                            self.realm_ap_finish = True
                        elif self.is_guild_realm_get_ap_set_top():
                            self.get_realm_ap()
                        else:
                            self.set_realm_get_ap_top()
                    else:
                        self.select_realm_ap_panel()
                elif self.is_guild_realm():
                    result, coord = self.find_guild_realm_ap_full()
                    if result:
                        self.click_in_circle(coord)
                    else:
                        self.realm_ap_finish = True
                elif self.is_guild_panel():
                    self.open_guild_realm()
                else:
                    self.open_guild_panel()
            else:
                self.realm_ap_finish = True
        else:
            self.guild_daily_finish = True

    def run_guild_realm(self):
        if not self.guild_foster:
            if self.is_realm_shikigami_cultivate_panel():
                if self.is_someone_else_realm():
                    if self.is_realm_foster_vacancy():
                        if self.is_dog_food_list_set:
                            if self.is_confirm_foster_panel():
                                self.confirm_realm_foster()
                            else:
                                self.click_first_dog_food_in_realm()
                        else:
                            self.set_realm_dog_food_list()
                    else:
                        self.guild_foster = True
                elif self.is_realm_foster_friend_list_panel():
                    if self.is_realm_foster_selected:
                        self.go_to_friend_realm()
                    else:
                        for i in range(1, 4):
                            if i == 1:
                                self.click_realm_friend_1()
                            elif i == 2:
                                self.click_realm_friend_2()
                            elif i == 3:
                                self.click_realm_friend_3()
                            elif i == 4:
                                self.click_realm_friend_4()
                            if self.is_realm_foster_friend_taigu():
                                self.is_realm_foster_selected = True
                            elif self.is_realm_foster_friend_douyu():
                                self.is_realm_foster_selected = True
                        else:
                            self.is_realm_foster_selected = True

                elif self.is_realm_foster_plus_button():
                    self.click_realm_foster_plus_button()
            elif self.is_guild_realm():
                self.open_realm_shikigami_cultivate_panel()
            elif self.is_guild_panel():
                self.open_guild_realm()
            else:
                self.open_guild_panel()
        elif not self.realm_cultivate:
            if self.is_realm_shikigami_cultivate_panel():
                if self.is_dog_food_list_set:
                    result, coord = self.find_realm_cultivate_full_shikigami()
                    if result:
                        self.click_in_circle([coord[0] + 56, coord[1] + 80], 36)
                    else:
                        result, coord = self.find_realm_cultivate_empty_shikigami()
                        if result:
                            result, coord = self.find_realm_cultivate_shikigami_in_list()
                            if result:
                                self.click_in_circle(coord, 36)
                            else:
                                self.slide_realm_cultivate_shikigami_list_to_right()
                        else:
                            self.close_guild_panel()    # 退出式神育成界面
                            self.is_realm_shikigami_full = False
                else:
                    self.set_realm_dog_food_list()

            elif self.is_guild_realm_ap_exp_panel():
                if self.is_realm_shikigami_full:
                    self.close_realm_ap_exp_panel()
                elif self.is_guild_realm_get_exp_panel():
                    if self.is_realm_shikigami_level_full_panel():
                        self.cancel_realm_shikigami_level_full_panel()
                        self.is_realm_shikigami_full = True
                    else:
                        self.get_realm_exp()
                        self.is_realm_shikigami_full = False
                else:
                    self.select_realm_exp_panel()
            elif self.is_guild_realm():
                if self.is_realm_shikigami_full:
                    self.open_realm_shikigami_cultivate_panel()
                elif not self.realm_cultivate:
                    result, coord = self.find_guild_realm_exp_full()
                    if result:
                        self.click_in_circle(coord)
                    else:
                        self.realm_cultivate = True
            elif self.is_guild_panel():
                self.open_guild_realm()
            else:
                self.open_guild_panel()
        else:
            self.guild_realm_finish = True

    def run_guild_mall(self):
        if self.is_guild_mall_panel():
            result, coord = self.find_collection_prize_panel_common()
            if result:
                self.click_in_circle([coord[0] + 200, coord[1] + 50])
            else:
                if not self.yingbing_buy:
                    if self.product.guild_mall_yingbing:
                        if self.is_guild_mall_yingbing_panel():
                            self.guild_mall_buy_multiple()
                        elif self.is_guild_mall_yingbing():
                            if self.is_yingbing_use_up():
                                self.yingbing_buy = True
                            else:
                                self.open_yingbing()
                        else:
                            self.slide_to_top()
                    else:
                        self.yingbing_buy = True
                elif not self.grade_daruma_buy:
                    if self.product.guild_mall_grade_daruma:
                        if self.is_guild_mall_grade_daruma_panel():
                            self.click_buy_button_2()
                        elif self.is_guild_mall_grade_daruma():
                            if self.is_grade_daruma_use_up():
                                self.grade_daruma_buy = True
                            else:
                                self.open_grade_daruma()
                        else:
                            self.slide_to_top()
                    else:
                        self.grade_daruma_buy = True
                elif not self.souls_buy:
                    if self.product.guild_mall_souls:
                        if self.is_guild_mall_souls_panel():
                            self.guild_mall_buy_multiple()
                        elif self.is_guild_mall_souls():
                            if self.is_souls_use_up():
                                self.souls_buy = True
                            else:
                                self.open_souls()
                        else:
                            self.slide_to_top()
                    else:
                        self.souls_buy = True
                elif not self.amulet_buy:
                    if self.product.guild_mall_amulet:
                        if self.is_guild_mall_amulet_panel():
                            self.guild_mall_buy_multiple()
                        elif self.is_guild_mall_amulet():
                            if self.is_amulet_use_up():
                                self.amulet_buy = True
                            else:
                                self.open_amulet()
                        else:
                            self.slide_to_bottom()
                    else:
                        self.amulet_buy = True
                elif not self.skill_daruma_buy:
                    if self.product.guild_mall_skill_daruma:
                        if self.is_guild_mall_skill_daruma_panel():
                            self.click_buy_button_2()
                        elif self.is_guild_mall_skill_daruma():
                            if self.is_skill_daruma_use_up():
                                self.skill_daruma_buy = True
                            else:
                                self.open_skill_daruma()
                        else:
                            self.slide_to_bottom()
                    else:
                        self.skill_daruma_buy = True
                elif not self.skin_ticket_buy:
                    if self.product.guild_mall_skin_ticket:
                        if self.is_guild_mall_skin_ticket_panel():
                            self.guild_mall_buy_multiple()
                        elif self.is_guild_mall_skin_ticket():
                            if self.is_skin_ticket_use_up():
                                self.skin_ticket_buy = True
                            else:
                                self.open_skin_ticket()
                        else:
                            self.slide_to_bottom()
                    else:
                        self.skin_ticket_buy = True
                else:
                    self.is_finished = True

        elif self.is_guild_panel():
            if self.is_guild_panel_shrine():
                if self.is_guild_mall_entrance():
                    self.open_guild_mall()
                else:
                    self.is_finished = True
            else:
                self.select_guild_panel_shrine()
        else:
            self.open_guild_panel()

    def guild_mall_buy_multiple(self):
        self.click_set_top_button()
        self.click_buy_button()

    def run_guild_realm_card_setting(self):
        if self.is_realm_card_panel():
            if self.is_realm_card_setting_panel():
                if self.is_realm_card_panel_active():
                    self.is_finished = True
                elif self.is_realm_card_panel_active_button():
                    self.click_realm_card_panel_active_button()
                else:
                    chapter_stage = self.product.chapter_stage
                    if chapter_stage == "taigu":
                        if self.is_realm_card_taigu_list():
                            if self.is_realm_card_empty():
                                self.is_finished = True
                            else:
                                self.select_realm_card()
                        elif self.is_realm_card_list_panel():
                            self.select_realm_card_taigu()
                        else:
                            self.open_realm_card_list_panel()
                    elif chapter_stage == "douyu":
                        if self.is_realm_card_douyu_list():
                            if self.is_realm_card_empty():
                                self.is_finished = True
                            else:
                                self.select_realm_card()
                        elif self.is_realm_card_list_panel():
                            self.select_realm_card_douyu()
                        else:
                            self.open_realm_card_list_panel()
                    elif chapter_stage == "sanshinei":
                        if self.is_realm_card_sanshinei_list():
                            if self.is_realm_card_empty():
                                self.is_finished = True
                            else:
                                self.select_realm_card()
                        elif self.is_realm_card_list_panel():
                            self.select_realm_card_sanshinei()
                        else:
                            self.open_realm_card_list_panel()
                    elif chapter_stage == "taiyinfuzhou":
                        if self.is_realm_card_taiyinfuzhou_list():
                            if self.is_realm_card_empty():
                                self.is_finished = True
                            else:
                                self.select_realm_card()
                        elif self.is_realm_card_list_panel():
                            self.select_realm_card_taiyinfuzhou()
                        else:
                            self.open_realm_card_list_panel()
                    elif chapter_stage == "teshubianyi":
                        if self.is_realm_card_teshubianyi_list():
                            if self.is_realm_card_empty():
                                self.is_finished = True
                            else:
                                self.select_realm_card()
                        elif self.is_realm_card_list_panel():
                            self.select_realm_card_teshubianyi()
                        else:
                            self.open_realm_card_list_panel()
            else:
                self.select_realm_card_setting_panel()

        elif self.is_guild_realm():
            self.open_realm_card_panel()
        elif self.is_guild_panel():
            self.open_guild_realm()
        else:
            self.open_guild_panel()

    def run_guild_realm_card_synthesis(self):
        if self.is_realm_card_panel():
            if self.is_realm_card_synthesis_panel():
                chapter_stage = str(self.product.chapter_stage)
                if self.is_realm_card_type_set:
                    if self.is_realm_card_synthesis_continue_button_clicked:
                        if self.is_realm_card_synthesis_empty_left() \
                                or self.is_realm_card_synthesis_empty_center() \
                                or self.is_realm_card_synthesis_empty_right():
                            self.is_finished = True
                        else:
                            self.start_realm_synthesis()
                            self.is_realm_card_synthesis_continue_button_clicked = False
                            time.sleep(2)
                    else:
                        if self.is_realm_card_synthesis_continue_button():
                            self.click_realm_card_synthesis_continue_button()
                            self.is_realm_card_synthesis_continue_button_clicked = True
                        elif self.is_realm_card_synthesis_empty_left() \
                                or self.is_realm_card_synthesis_empty_center() \
                                or self.is_realm_card_synthesis_empty_right():
                            result, coord = False, [0, 0]
                            if "1" in chapter_stage:
                                result, coord = self.find_realm_card_star_1()
                            elif "2" in chapter_stage:
                                result, coord = self.find_realm_card_star_2()
                            elif "3" in chapter_stage:
                                result, coord = self.find_realm_card_star_3()
                            elif "4" in chapter_stage:
                                result, coord = self.find_realm_card_star_4()
                            if result:
                                if self.is_realm_card_synthesis_not_check([coord[0] + 255, coord[1] - 65], [20, 20, 20, 20]):
                                    self.click_in_circle([coord[0] + 60, coord[1]])
                                else:
                                    self.slide_realm_card_list_to_bottom()
                            else:
                                self.is_finished = True
                        else:
                            self.start_realm_synthesis()

                else:

                    if "taigu" in chapter_stage:
                        if self.is_realm_card_taigu_list():
                            if self.is_realm_card_empty():
                                self.is_finished = True
                                self.is_realm_card_type_set = False
                            else:
                                self.is_realm_card_type_set = True
                        elif self.is_realm_card_list_panel():
                            self.select_realm_card_taigu()
                        else:
                            self.open_realm_card_list_panel()
                    elif "douyu" in chapter_stage:
                        if self.is_realm_card_douyu_list():
                            if self.is_realm_card_empty():
                                self.is_finished = True
                                self.is_realm_card_type_set = False
                            else:
                                self.is_realm_card_type_set = True
                        elif self.is_realm_card_list_panel():
                            self.select_realm_card_douyu()
                        else:
                            self.open_realm_card_list_panel()
                    elif "sanshinei" in chapter_stage:
                        if self.is_realm_card_sanshinei_list():
                            if self.is_realm_card_empty():
                                self.is_finished = True
                                self.is_realm_card_type_set = False
                            else:
                                self.is_realm_card_type_set = True
                        elif self.is_realm_card_list_panel():
                            self.select_realm_card_sanshinei()
                        else:
                            self.open_realm_card_list_panel()
                    elif "taiyinfuzhou" in chapter_stage:
                        if self.is_realm_card_taiyinfuzhou_list():
                            if self.is_realm_card_empty():
                                self.is_finished = True
                                self.is_realm_card_type_set = False
                            else:
                                self.is_realm_card_type_set = True
                        elif self.is_realm_card_list_panel():
                            self.select_realm_card_taiyinfuzhou()
                        else:
                            self.open_realm_card_list_panel()
                    elif "teshubianyi" in chapter_stage:
                        if self.is_realm_card_teshubianyi_list():
                            if self.is_realm_card_empty():
                                self.is_finished = True
                                self.is_realm_card_type_set = False
                            else:
                                self.is_realm_card_type_set = True
                        elif self.is_realm_card_list_panel():
                            self.select_realm_card_teshubianyi()
                        else:
                            self.open_realm_card_list_panel()
            else:
                self.select_realm_card_synthesis_panel()

        elif self.is_guild_realm():
            self.open_realm_card_panel()
        elif self.is_guild_panel():
            self.open_guild_realm()
        else:
            self.open_guild_panel()

    def check_current_contribute_jade(self):
        if self.is_guild_contribute_jade_button_100():
            return 100
        elif self.is_guild_contribute_jade_button_80():
            return 80
        elif self.is_guild_contribute_jade_button_60():
            return 60
        elif self.is_guild_contribute_jade_button_40():
            return 40
        elif self.is_guild_contribute_jade_button_20():
            return 20
        elif self.is_guild_contribute_jade_button_0():
            return 0

    def set_realm_dog_food_list(self):
        if self.product.cultivate_m or self.product.guild_foster_m:
            if self.is_chapter_change_dog_food_m_list():
                self.is_dog_food_list_set = True
            elif self.is_chapter_change_dog_food_m_list_button():
                self.select_chapter_change_dog_food_m_list_button()
            else:
                self.open_chapter_change_dog_food_type_select_panel()
        elif self.product.cultivate_n or self.product.guild_foster_n:
            if self.is_chapter_change_dog_food_n_list():
                self.is_dog_food_list_set = True
            elif self.is_chapter_change_dog_food_n_list_button():
                self.select_chapter_change_dog_food_n_list_button()
            else:
                self.open_chapter_change_dog_food_type_select_panel()

    def open_guild_panel(self):
        if self.is_yard():
            signal_run_list.set_current_scene.emit(self.run_id, "庭院")
            signal_run_list.set_current_operation.emit(self.run_id, "打开寮界面")
            self.open_guild()
        elif self.is_explore():  # 探索地图
            signal_run_list.set_current_scene.emit(self.run_id, "探索地图")
            signal_run_list.set_current_operation.emit(self.run_id, "退出探索地图")
            self.quit_explore()

    def processing_stop(self):
        pass

from hiworker import *


class OperateGuild(Win32Click):
    def __init__(self):
        super(OperateGuild, self).__init__()

    def close_guild_panel(self):
        """
        关闭阴阳寮界面
        :return:
        """
        self.click_in_template("guild_is_guild_panel_quit_button")

    def open_guild_realm(self):
        """
        打开寮结界
        :return:
        """
        self.click_in_template("guild_is_guild_realm_raid_entrance")

    def select_guild_panel_info(self):
        """
        打开寮信息面板
        :return:
        """
        self.click_in_template("guild_is_guild_panel_info")

    def select_guild_panel_invocation(self):
        """
        打开祈愿面板
        :return:
        """
        self.click_in_template("guild_is_guild_panel_invocation")

    def select_guild_panel_shrine(self):
        """
        选择神社面板
        :return:
        """
        self.click_in_template("guild_is_guild_panel_shrine")

    def get_guild_coin(self):
        """
        领取寮金币
        :return:
        """
        self.click_in_template("guild_is_guild_get_coin_button")

    def confirm_get_guild_coin(self):
        """
        确认领取寮金币
        :return:
        """
        self.click_in_template("guild_is_guild_get_coin_confirm_button")

    def contribute_guild_jade(self):
        """
        捐赠勾玉
        :return:
        """
        self.click_in_template("guild_is_guild_contribute_jade_button")

    def add_contribute_guild_jade(self):
        """
        增加勾玉捐赠数量
        :return:
        """
        self.click_in_template("guild_is_guild_contribute_jade_add_button")

    def dec_contribute_guild_jade(self):
        """
        减少勾玉捐赠数量
        :return:
        """
        self.click_in_template("guild_is_guild_contribute_jade_dec_button")

    def confirm_contribute_guild_jade(self):
        """
        确认捐赠勾玉
        :return:
        """
        self.click_in_template("guild_is_guild_contribute_jade_confirm_button")

    def open_invocation_panel(self):
        """
        打开祈愿面板
        :return:
        """
        self.click_in_template("guild_is_guild_invocation_button")

    def select_invocation_sp(self):
        """
        祈愿SP
        :return:
        """
        self.click_in_template("guild_is_guild_invocation_shikigami_list_sp")

    def select_invocation_ssr(self):
        """
        祈愿SSR
        :return:
        """
        self.click_in_template("guild_is_guild_invocation_shikigami_list_ssr")

    def select_invocation_sr(self):
        """
        祈愿SR
        :return:
        """
        self.click_in_template("guild_is_guild_invocation_shikigami_list_sr")

    def confirm_invocation(self):
        """
        确认祈愿
        :return:
        """
        self.click_in_template("guild_is_guild_invocation_confirm_button")

    def open_guild_shrine_guild_task(self):
        """
        打开寮任务面板
        :return:
        """
        self.click_in_template("guild_is_guild_shrine_guild_task_entrance")

    def open_guild_shrine_feats_store(self):
        """
        打开神社商店
        :return:
        """
        self.click_in_template("guild_is_guild_shrine_meda_store_entrance")

    def buy_guild_shrine_grade_daruma(self):
        """
        购买奉为达摩
        :return:
        """
        self.click_in_template("guild_is_guild_shrine_feats_store_grade_daruma")

    def buy_guild_shrine_six_star_souls(self):
        """
        购买六星御魂
        :return:
        """
        self.click_in_template("guild_is_guild_shrine_feats_store_six_star_souls")

    def buy_guild_shrine_mystery_amulet(self):
        """
        购买蓝票
        :return:
        """
        self.click_in_template("guild_is_guild_shrine_feats_store_mystery_amulet")

    def buy_guild_shrine_skill_daruma(self):
        """
        购买御行达摩
        :return:
        """
        self.click_in_template("guild_is_guild_shrine_feats_store_skill_daruma")

    def buy_guild_shrine_skin_token(self):
        """
        购买皮肤券
        :return:
        """
        self.click_in_template("guild_is_guild_shrine_feats_store_skin_token")

    def open_guild_contribute_panel(self):
        """
        打开捐赠面板
        :return:
        """
        self.click_in_template("guild_open_guild_contribute_panel")

    def click_guild_contribute_jade_button_20(self):
        """
        捐赠20勾玉
        :return:
        """
        self.click_in_template("guild_is_guild_contribute_jade_button_20")

    def click_guild_contribute_jade_button_40(self):
        """
        捐赠40勾玉
        :return:
        """
        self.click_in_template("guild_is_guild_contribute_jade_button_40")

    def click_guild_contribute_jade_button_60(self):
        """
        捐赠60勾玉
        :return:
        """
        self.click_in_template("guild_is_guild_contribute_jade_button_60")

    def click_guild_contribute_jade_button_80(self):
        """
        捐赠80勾玉
        :return:
        """
        self.click_in_template("guild_is_guild_contribute_jade_button_80")

    def click_guild_contribute_jade_button_100(self):
        """
        捐赠100勾玉
        :return:
        """
        self.click_in_template("guild_is_guild_contribute_jade_button_100")

    def select_realm_ap_panel(self):
        """
        打开结界体力面板
        :return:
        """
        self.click_in_template("guild_select_realm_ap_panel")

    def select_realm_exp_panel(self):
        """
        打开结界经验面板
        :return:
        """
        self.click_in_template("guild_select_realm_exp_panel")

    def set_realm_get_ap_top(self):
        """
        设置所有体力
        :return:
        """
        self.click_in_template("guild_is_guild_realm_get_ap_set_top_button")

    def get_realm_ap(self):
        """
        领取体力
        :return:
        """
        self.click_in_template("guild_is_guild_realm_get_ap_button")

    def get_realm_exp(self):
        """
        领取经验
        :return:
        """
        self.click_in_template("guild_is_guild_realm_get_exp_button")

    def cancel_realm_shikigami_level_full_panel(self):
        """
        取消满级提示界面
        :return:
        """
        self.click_in_template("guild_cancel_realm_shikigami_level_full_panel")

    def close_realm_ap_exp_panel(self):
        """
        关闭经验体力面板
        :return:
        """
        self.click_in_template("guild_close_realm_ap_exp_panel")

    def open_realm_shikigami_cultivate_panel(self):
        """
        打开结界寄养面板
        :return:
        """
        self.click_in_template("guild_open_realm_shikigami_cultivate_panel")

    def slide_realm_cultivate_shikigami_list_to_right(self):
        """
        滑动结界寄养狗粮列表到右边
        :return:
        """
        self.slide_distance_with_template("guild_slide_realm_cultivate_shikigami_list_to_right", -200, 30)

    def get_guild_task_battle_30_prize(self):
        """
        领取寮30奖励
        :return:
        """
        self.click_in_template("guild_is_guild_task_battle_30_get_prize_button")

    def close_guild_task_panel(self):
        """
        关闭寮任务面板
        :return:
        """
        self.click_in_template("guild_is_guild_shrine_guild_task_close_button")

    def open_guild_mall(self):
        """
        打开寮商店
        :return:
        """
        self.click_in_template("guild_is_guild_mall_entrance")

    def slide_guild_mall_to_top(self):
        """
        滑动寮商店到顶部
        :return:
        """
        self.slide_distance_with_template("guild_slide_guild_mall_to_top", 50, 200)

    def slide_guild_mall_to_bottom(self):
        """
        滑动寮商店到底部
        :return:
        """
        self.slide_distance_with_template("guild_slide_guild_mall_to_bottom", 50, -200)

    def click_guild_mall_set_top_button(self):
        """
        点击拉满图标
        :return:
        """
        self.click_in_template("guild_click_guild_mall_set_top_button")

    def click_guild_mall_buy_button(self):
        """
        点击购买
        :return:
        """
        self.click_in_template("guild_click_guild_mall_buy_button")

    def click_guild_mall_buy_button_2(self):
        """
        点击购买2
        :return:
        """
        self.click_in_template("guild_click_guild_mall_buy_button_2")

    def open_guild_mall_yingbing(self):
        """
        打开购买樱饼
        :return:
        """
        self.click_in_template("guild_is_guild_mall_yingbing")

    def open_guild_mall_grade_daruma(self):
        """
        打开购买奉为达摩
        :return:
        """
        self.click_in_template("guild_is_guild_mall_grade_daruma")

    def open_guild_mall_souls(self):
        """
        打开购买御魂
        :return:
        """
        self.click_in_template("guild_is_guild_mall_souls")

    def open_guild_mall_amulet(self):
        """
        打开购买蓝票
        :return:
        """
        self.click_in_template("guild_is_guild_mall_amulet")

    def open_guild_mall_skill_daruma(self):
        """
        打开购买御行达摩
        :return:
        """
        self.click_in_template("guild_is_guild_mall_skill_daruma")

    def open_guild_mall_skin_ticket(self):
        """
        打开购买皮肤券
        :return:
        """
        self.click_in_template("guild_is_guild_mall_skin_ticket")

    def open_realm_card_panel(self):
        """
        打开结界卡界面
        :return:
        """
        self.click_in_template("guild_open_realm_card_panel")

    def click_realm_card_panel_active_button(self):
        """
        激活结界卡
        :return:
        """
        self.click_in_template("guild_is_realm_card_panel_active_button")

    def open_realm_card_list_panel(self):
        """
        打开结界卡列表
        :return:
        """
        self.click_in_template("guild_open_realm_card_list_panel")

    def select_realm_card_taigu(self):
        """
        选择太古
        :return:
        """
        self.click_in_template("guild_select_realm_card_taigu")

    def select_realm_card(self):
        """
        选择结界卡
        :return:
        """
        self.click_in_template("guild_select_realm_card")

    def select_realm_card_setting_panel(self):
        """
        选择结界卡设置界面
        :return:
        """
        self.click_in_template("guild_is_realm_card_setting_panel")

    def select_realm_card_douyu(self):
        """
        选择斗鱼列表
        :return:
        """
        self.click_in_template("guild_select_realm_card_douyu")

    def select_realm_card_sanshinei(self):
        """
        选择伞室内列表
        :return:
        """
        self.click_in_template("guild_select_realm_card_sanshinei")

    def select_realm_card_taiyinfuzhou(self):
        """
        选择太阴符咒列表
        :return:
        """
        self.click_in_template("guild_select_realm_card_taiyinfuzhou")

    def select_realm_card_teshubianyi(self):
        """
        选择特殊编译列表
        :return:
        """
        self.click_in_template("guild_select_realm_card_teshubianyi")

    def select_realm_card_synthesis_panel(self):
        """
        选择合成界面
        :return:
        """
        self.click_in_template("guild_is_realm_card_synthesis_panel")

    def start_realm_synthesis(self):
        """
        开始合成
        :return:
        """
        self.click_in_template("guild_start_realm_synthesis")

    def click_realm_card_synthesis_continue_button(self):
        """
        继续合成
        :return:
        """
        self.click_in_template("guild_is_realm_card_synthesis_continue_button")

    def slide_realm_card_list_to_bottom(self):
        """
        滑动结界卡列表到底部
        :return:
        """
        self.slide_distance_with_template("guild_slide_realm_card_list_to_bottom", 50, -200)

    def click_realm_foster_plus_button(self):
        """
        点击结界寄养加号
        :return:
        """
        self.click_in_template("guild_is_realm_foster_puls_button")

    def go_to_friend_realm(self):
        """
        前往好友结界
        :return:
        """
        self.click_in_template("guild_go_to_friend_realm")

    def click_realm_friend_1(self):
        """
        点击好友结界1
        :return:
        """
        self.click_in_template("guild_click_realm_friend_1")

    def click_realm_friend_2(self):
        """
        点击好友结界2
        :return:
        """
        self.click_in_template("guild_click_realm_friend_2")

    def click_realm_friend_3(self):
        """
        点击好友结界3
        :return:
        """
        self.click_in_template("guild_click_realm_friend_3")

    def click_realm_friend_4(self):
        """
        点击好友结界4
        :return:
        """
        self.click_in_template("guild_click_realm_friend_4")

    def click_first_dog_food_in_realm(self):
        """
        点击第一个狗粮
        :return:
        """
        self.click_in_template("guild_click_first_dog_food_in_realm")

    def confirm_realm_foster(self):
        """
        确认寄样
        :return:
        """
        self.click_in_template("guild_confirm_realm_foster")

    def set_guild_create_position(self):
        """
        设置寮创建位置
        :return:
        """
        self.click_in_template("guild_set_guild_create_position")

    def click_create_guild_realm_button(self):
        """
        点击创建寮
        :return:
        """
        self.click_in_template("guild_is_create_guild_button")

    def quit_create_guild_realm_map(self):
        """
        退出寮创建地图
        :return:
        """
        self.click_in_template("guild_quit_create_guild_realm_map")

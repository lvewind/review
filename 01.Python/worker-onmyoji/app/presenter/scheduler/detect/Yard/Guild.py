from hiworker import *


class DetectGuild(DetectImage):
    def __init__(self):
        super(DetectGuild, self).__init__()

    def is_guild_panel(self):
        """
        阴阳寮界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_panel")
        return result

    def is_guild_panel_quit_button(self):
        """
        阴阳寮界面退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_panel_quit_button")
        return result

    def is_guild_panel_info(self):
        """
        阴阳寮界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_panel_info", 0.9)
        return result

    def is_guild_realm_entrance(self):
        """
        阴阳寮结界入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_raid_entrance")
        return result

    def is_create_realm_button(self):
        """
        阴阳寮创建按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_create_realm_button")
        return result

    def is_guild_panel_invocation(self):
        """
        阴阳寮祈愿面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_panel_invocation", 0.9)
        return result

    def is_guild_panel_shrine(self):
        """
        阴阳寮神社面板
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_panel_shrine", 0.9)
        return result

    def is_guild_get_coin_button(self):
        """
        阴阳寮领取金币按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_get_coin_button")
        return result

    def is_guild_get_coin_button_not_get(self):
        """
        金币未领取
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_get_coin_button_not_get")
        return result

    def is_guild_get_coin_confirm_button(self):
        """
        确认领取金币
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_get_coin_confirm_button")
        return result

    def is_guild_contribute_jade_button(self):
        """
        捐勾玉按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_button")
        return result

    def is_guild_contribute_jade_panel(self):
        """
        捐勾玉界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_panel")
        return result

    def is_guild_contribute_jade_1(self):
        """
        捐一定数量勾玉
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_1")
        return result

    def is_guild_contribute_jade_2(self):
        """
        捐一定数量勾玉
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_2")
        return result

    def is_guild_contribute_jade_3(self):
        """
        捐一定数量勾玉
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_3")
        return result

    def is_guild_contribute_jade_4(self):
        """
        捐一定数量勾玉
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_4")
        return result

    def is_guild_contribute_jade_5(self):
        """
        捐一定数量勾玉
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_5")
        return result

    def is_guild_contribute_jade_button_0(self):
        """
        捐一定数量勾玉按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_button_0")
        return result

    def is_guild_contribute_jade_button_20(self):
        """
        捐一定数量勾玉按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_button_20")
        return result

    def is_guild_contribute_jade_button_40(self):
        """
        捐一定数量勾玉按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_button_40")
        return result

    def is_guild_contribute_jade_button_60(self):
        """
        捐一定数量勾玉按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_button_60")
        return result

    def is_guild_contribute_jade_button_80(self):
        """
        捐一定数量勾玉按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_button_80")
        return result

    def is_guild_contribute_jade_button_100(self):
        """
        捐一定数量勾玉按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_button_100")
        return result

    def is_guild_contribute_jade_slide_right(self):
        """
        捐勾玉拉满
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_slide_right")
        return result

    def is_guild_contribute_jade_confirm_button(self):
        """
        确认捐勾玉
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_contribute_jade_confirm_button")
        return result

    def is_guild_invocation_button(self):
        """
        起祈愿按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_invocation_button")
        return result

    def is_guild_invocation_shikigami_list(self):
        """
        祈愿界面式神列表
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_invocation_shikigami_list")
        return result

    def is_guild_invocation_shikigami_list_sp(self):
        """
        祈愿界面式神列表
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_invocation_shikigami_list_sp", 0.9)
        return result

    def is_guild_invocation_shikigami_list_ssr(self):
        """
        祈愿界面式神列表
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_invocation_shikigami_list_ssr", 0.9)
        return result

    def is_guild_invocation_shikigami_list_sr(self):
        """
        祈愿界面式神列表
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_invocation_shikigami_list_sr", 0.9)
        return result

    def is_guild_invocation_confirm_button(self):
        """
        确认祈愿按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_invocation_confirm_button")
        return result

    def is_guild_shrine_guild_task_entrance(self):
        """
        寮任务入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_entrance")
        return result

    def is_guild_shrine_feats_store_entrance(self):
        """
        功勋商店入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_meda_store_entrance")
        return result

    def is_guild_shrine_guild_task_panel(self):
        """
        寮任务界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_panel")
        return result

    def find_guild_shrine_guild_task_evo_1(self):
        """
        寮任务1
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_evo_1")
        return result, coord

    def find_guild_shrine_guild_task_evo_2(self):
        """
        寮任务2
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_evo_2")
        return result, coord

    def is_guild_shrine_guild_task_submit_button_left(self):
        """
        寮任务捐材料按钮左
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_submit_button_left")
        return result

    def is_guild_shrine_guild_task_submit_button_center(self):
        """
        寮任务捐材料按钮中
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_submit_button_center")
        return result

    def is_guild_shrine_guild_task_submit_button_right(self):
        """
        寮任务捐材料按钮右边
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_submit_button_right")
        return result

    def is_guild_shrine_guild_task_close_button(self):
        """
        寮任务关闭按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_close_button")
        return result

    def is_guild_shrine_guild_task_finished(self):
        """
        寮任务已完成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_finished")
        return result

    def is_guild_shrine_guild_task_together(self):
        """
        结伴同行任务
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_together")
        return result

    def is_guild_shrine_guild_task_submit_panel(self):
        """
        寮任务提交界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_submit_panel")
        return result

    def is_guild_shrine_guild_task_submit_panel_full(self):
        """
        寮任务提交界面拉满
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_submit_panel_full")
        return result

    def find_guild_shrine_guild_task_submit_panel_slide_button(self):
        """
        查找任务提交面板滑动按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_submit_panel_slide_button")
        return result, coord

    def find_guild_shrine_guild_task_submit_panel_submit_button(self):
        """
        查找任务提交按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_guild_task_submit_panel_submit_button")
        return result, coord

    def is_guild_shrine_feats_store(self):
        """
        功勋商店
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_feats_store")
        return result

    def is_guild_shrine_feats_store_grade_daruma(self):
        """
        功勋商店奉为达摩
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_feats_store_grade_daruma")
        return result

    def is_guild_shrine_feats_store_six_star_souls(self):
        """
        功勋商店六星御魂
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_feats_store_six_star_souls")
        return result

    def is_guild_shrine_feats_store_mystery_amulet(self):
        """
        功勋商店蓝票
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_feats_store_mystery_amulet")
        return result

    def is_guild_shrine_feats_store_skill_daruma(self):
        """
        功勋商店御行达摩碎片
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_feats_store_skill_daruma")
        return result

    def is_guild_shrine_feats_store_skin_token(self):
        """
        功勋商店皮肤券
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_feats_store_skin_token")
        return result

    def is_guild_shrine_feats_store_grade_daruma_buy_button(self):
        """
        功勋商店奉为达摩购买按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_feats_store_grade_daruma_buy_button")
        return result

    def is_guild_shrine_feats_store_six_star_souls_buy_button(self):
        """
        功勋商店六星御魂购买按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_feats_store_six_star_souls_buy_button")
        return result

    def is_guild_shrine_feats_store_mystery_amulet_buy_button(self):
        """
        功勋商店蓝票购买按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_feats_store_mystery_amulet_buy_button")
        return result

    def is_guild_shrine_feats_store_skill_daruma_buy_button(self):
        """
        功勋商店御行达摩碎片购买按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_feats_store_skill_daruma_buy_button")
        return result

    def is_guild_shrine_feats_store_skin_token_buy_button(self):
        """
        功勋商店皮肤券购买按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_shrine_feats_store_skin_token_buy_button")
        return result

    def is_guild_realm(self):
        """
        阴阳寮结界
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm")
        return result

    def find_guild_realm_ap_full(self):
        """
        阴阳寮结界体力满
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_ap_full")
        return result, coord

    def is_guild_realm_get_ap_panel(self):
        """
        阴阳寮结界体力界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_get_ap_panel")
        return result, coord

    def is_guild_realm_ap_exp_panel(self):
        """
        阴阳寮结界经验界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_ap_exp_panel")
        return result

    def is_guild_realm_get_ap_set_top(self):
        """
        体力领取拉满
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_get_ap_set_top")
        return result

    def is_guild_realm_get_ap_set_top_button(self):
        """
        体力领取拉满按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_get_ap_set_top_button")
        return result

    def is_guild_realm_get_ap_button(self):
        """
        体力领取按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_get_ap_button")
        return result

    def is_guild_realm_get_ap_use_up(self):
        """
        体力已经领完
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_get_use_up", 0.9)
        return result

    def find_guild_realm_exp_full(self):
        """
        经验满
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_exp_full")
        return result, coord

    def is_guild_realm_get_exp_panel(self):
        """
        经验领取界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_get_exp_panel")
        return result, coord

    def is_guild_realm_get_exp_button(self):
        """
        经验拉满按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_get_exp_button")
        return result

    def is_guild_realm_get_exp_use_up(self):
        """
        经验已领完
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_get_exp_use_up", 0.9)
        return result

    def is_guild_realm_card_panel(self):
        """
        结界卡界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_card_panel")
        return result

    def is_guild_realm_card_panel_quit_button(self):
        """
        结界卡界面退出按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_card_panel_quit_button")
        return result

    def is_guild_realm_card_panel_setting(self):
        """
        结界卡设置界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_card_panel_setting")
        return result

    def is_guild_realm_card_panel_synthesis(self):
        """
        合成界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_card_panel_synthesis")
        return result

    def is_guild_realm_card_panel_synthesis_taiyin_list(self):
        """
        合成界面太阴符咒列表
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_card_panel_synthesis_taiyin_list")
        return result

    def is_guild_realm_card_panel_synthesis_taiyin_list_taiyin(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_card_panel_synthesis_taiyin_list_taiyin")
        return result

    def is_guild_realm_card_synthesis_empty_1(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_card_synthesis_empty_1")
        return result

    def is_guild_realm_card_synthesis_empty_2(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_card_synthesis_empty_2")
        return result

    def is_guild_realm_card_synthesis_empty_3(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_card_synthesis_empty_3")
        return result

    def is_guild_realm_card_synthesis_button(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_card_synthesis_button")
        return result

    def is_guild_realm_card_synthesis_continue_button(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_realm_card_synthesis_continue_button")
        return result

    def is_realm_shikigami_level_full_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_shikigami_level_full_panel")
        return result

    def is_realm_shikigami_cultivate_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_shikigami_cultivate_panel")
        return result

    def find_realm_cultivate_full_shikigami(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_find_realm_cultivate_full_shikigami")
        return result, coord

    def find_realm_cultivate_empty_shikigami(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_find_realm_cultivate_empty_shikigami")
        return result, coord

    def find_realm_cultivate_shikigami_in_list(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_find_realm_cultivate_shikigami_in_list")
        return result, coord

    def is_guild_task_battle_30(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_task_battle_30")
        return result

    def is_guild_task_battle_30_in_progress(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_task_battle_30_in_progress")
        return result

    def is_guild_task_battle_30_get_prize_button(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_task_battle_30_get_prize_button")
        return result

    def is_guild_mall_entrance(self):
        """
        寮商店入口
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_entrance")
        return result

    def is_guild_mall_panel(self):
        """
        寮商店界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_panel")
        return result

    def is_guild_mall_yingbing(self):
        """
        寮商店樱饼
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_yingbing")
        return result

    def is_guild_mall_grade_daruma(self):
        """
        寮商店奉为达摩
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_grade_daruma")
        return result

    def is_guild_mall_souls(self):
        """
        寮商店御魂
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_souls")
        return result

    def is_guild_mall_amulet(self):
        """
        寮商店蓝票
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_amulet")
        return result

    def is_guild_mall_skill_daruma(self):
        """
        寮商店御行达摩碎片
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_skill_daruma")
        return result

    def is_guild_mall_skin_ticket(self):
        """
        寮商店皮肤券
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_skin_ticket")
        return result

    def is_guild_mall_yingbing_panel(self):
        """
        寮商店樱饼购买界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_yingbing_panel")
        return result

    def is_realm_card_panel(self):
        """
        结界卡界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_panel")
        return result

    def is_guild_mall_yingbing_use_up(self):
        """
        樱饼已买完
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_yingbing_use_up")
        return result

    def is_guild_mall_skin_ticket_use_up(self):
        """
        皮肤券已买完
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_skin_ticket_use_up")
        return result

    def is_guild_mall_grade_daruma_use_up(self):
        """
        奉为达摩已买完
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_grade_daruma_use_up")
        return result

    def is_guild_mall_souls_use_up(self):
        """
        六星御魂已买完
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_souls_use_up")
        return result

    def is_guild_mall_amulet_use_up(self):
        """
        蓝票已卖完
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_amulet_use_up")
        return result

    def is_guild_mall_skill_daruma_use_up(self):
        """
        御行达摩已买完
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_skill_daruma_use_up")
        return result

    def is_guild_mall_grade_daruma_panel(self):
        """
        奉为达摩购买界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_grade_daruma_panel")
        return result

    def is_guild_mall_souls_panel(self):
        """
        御魂购买界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_souls_panel")
        return result

    def is_guild_mall_amulet_panel(self):
        """
        蓝票购买界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_amulet_panel")
        return result

    def is_guild_mall_skill_daruma_panel(self):
        """
        御行达摩购买界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_skill_daruma_panel")
        return result

    def is_guild_mall_skin_ticket_panel(self):
        """
        皮肤券购买界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_guild_mall_skin_ticket_panel")
        return result

    def is_realm_card_panel_active(self):
        """
        结界卡已激活
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_panel_active")
        return result

    def is_realm_card_panel_active_button(self):
        """
        结界卡激活按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_panel_active_button", 0.985)
        return result

    def is_realm_card_taigu_list(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_taigu_list")
        return result

    def is_realm_card_empty(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_empty")
        return result

    def is_realm_card_list_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_list_panel")
        return result

    def is_realm_card_setting_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_setting_panel")
        return result

    def is_realm_card_douyu_list(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_douyu_list")
        return result

    def is_realm_card_sanshinei_list(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_sanshinei_list")
        return result

    def is_realm_card_taiyinfuzhou_list(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_taiyinfuzhou_list")
        return result

    def is_realm_card_teshubianyi_list(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_teshubianyi_list")
        return result

    def is_realm_card_synthesis_panel(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_synthesis_panel")
        return result

    def is_realm_card_synthesis_empty_left(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_synthesis_empty_left")
        return result

    def is_realm_card_synthesis_empty_center(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_synthesis_empty_center")
        return result

    def is_realm_card_synthesis_empty_right(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_synthesis_empty_right")
        return result

    def is_realm_card_synthesis_continue_button(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_card_synthesis_continue_button")
        return result

    def is_realm_card_synthesis_not_check(self, point: list, box: list):
        result, coord, max_similarity = self.find_with_point_ext_area("guild_is_realm_card_synthesis_not_check", point, box)
        return result

    def find_realm_card_star_1(self):
        """
        查找1星结界卡
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_find_realm_card_star_1", 0.885)
        return result, coord

    def find_realm_card_star_2(self):
        """
        查找2星结界卡
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_find_realm_card_star_2", 0.885)
        return result, coord

    def find_realm_card_star_3(self):
        """
        查找3星结界卡
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_find_realm_card_star_3", 0.885)
        return result, coord

    def find_realm_card_star_4(self):
        """
        查找4星结界卡
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_find_realm_card_star_4", 0.885)
        return result, coord

    def is_someone_else_realm(self):
        """
        别人的结界
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_someone_else_realm")
        return result

    def is_realm_foster_plus_button(self):
        """
        寄养按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_foster_puls_button")
        return result

    def is_realm_foster_friend_list_panel(self):
        """
        寄养结界列表
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_foster_friend_list_panel")
        return result

    def is_realm_foster_friend_taigu(self):
        """
        寄养太古
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_foster_friend_taigu")
        return result

    def is_realm_foster_friend_douyu(self):
        """
        寄养斗鱼
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_foster_friend_douyu")
        return result

    def is_confirm_foster_panel(self):
        """
        寄养确认界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_confirm_foster_panel")
        return result

    def is_realm_foster_vacancy(self):
        result, coord, max_similarity = self.find_in_template_rect("guild_is_realm_foster_vacancy")
        return result

    def is_create_guild_realm_map(self):
        """
        创建结界地图界面
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_create_guild_realm_map", 0.7)
        return result

    def is_create_guild_button(self):
        """
        阴阳寮创建按钮
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_create_guild_button")
        return result

    def is_create_guild_realm_map_done(self):
        """
        结界创建完成
        :return:
        """
        result, coord, max_similarity = self.find_in_template_rect("guild_is_create_guild_realm_map_done")
        return result

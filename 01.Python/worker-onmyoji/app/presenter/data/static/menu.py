class DataContextMenu:
    def __init__(self):
        self.run_list = {}

        self.common = {
            "add": "创建",
            "edit": "编辑",
            "delete": "删除",
            "delete_selected": "删除选中",
            "delete_all": "删除全部",
            "refresh": "刷新"
        }
        self.worker_list = {
            "add": "招聘工人",
            "edit": "变更工人",
            "delete": "解雇工人",
            "delete_selected": "解雇选中",
            "delete_all": "解雇全部",
            "refresh": "刷新"
        }

        self.worker_sub_list = {
            "add": "新增工位",
            "edit": "更换任务",
            "delete": "删除工位",
            "delete_selected": "删除选中",
            "delete_all": "删除全部",
            "refresh": "刷新"
        }

        self.job_list = {
            "add": "创建任务",
            "edit": "修改名称",
            "delete": "删除任务",
            "delete_selected": "删除选中",
            "delete_all": "删除全部",
            "refresh": "刷新"
        }

        self.plan_day_list = {
            "add": "创建日计划",
            "edit": "变更日计划",
            "delete": "删除日计划",
            "delete_selected": "删除选中",
            "delete_all": "删除全部",
            "refresh": "刷新"
        }

        self.plan_day_sub_list = {
            "add": "创建子计划",
            "edit": "变更子计划",
            "delete": "删除子计划",
            "delete_selected": "删除选中",
            "delete_all": "删除全部",
            "refresh": "刷新"
        }

        self.plan_week_list = {
            "add": "创建周计划",
            "edit": "变更周计划",
            "delete": "删除计划",
            "delete_selected": "删除选中",
            "delete_all": "删除全部",
            "refresh": "刷新"
        }

        self.plan_week_sub_list = {
            "add": "创建子计划",
            "edit": "变更子计划",
            "delete": "删除子计划",
            "delete_selected": "删除选中",
            "delete_all": "删除全部",
            "refresh": "刷新"
        }

        self.plan_month_list = {
            "add": "创建月计划",
            "edit": "变更月计划",
            "delete": "删除月计划",
            "delete_selected": "删除选中",
            "delete_all": "删除全部",
            "refresh": "刷新"
        }

        self.plan_month_sub_list = {
            "add": "创建子计划",
            "edit": "变更子计划",
            "delete": "删除子计划",
            "delete_selected": "删除选中",
            "delete_all": "删除全部",
            "refresh": "刷新"
        }

        self.account_list = {
            "add": "创建子计划",
            "edit": "变更子计划",
            "delete": "删除子计划",
            "delete_selected": "删除选中",
            "delete_all": "删除全部",
            "refresh": "刷新"
        }

        self.account_list = {
            "add": "新客户",
            "edit": "变更客户",
            "delete": "删除客户",
            "delete_selected": "删除选中",
            "delete_all": "删除全部",
            "refresh": "刷新"
        }


data_menu = DataContextMenu()

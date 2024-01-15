from .media_static import *
from .fly_type import fly_type
from app.utils.utils import get_font_color

header_collection = {
    "id": {
        "col": 0, "header_name": "ID", "width": 40, "extend": None, "color_switch": False},
    "name": {
        "col": 1, "header_name": "名称", "width": 170, "extend": None, "color_switch": False,
    }
}

header_episode = {
    "sort": {
        "col": 0, "header_name": "ID", "width": 40, "extend": None, "color_switch": False},
    "name": {
        "col": 1, "header_name": "名称", "width": 250, "extend": None, "color_switch": False,
    },

    "speech_audio_synchronize": {
        "col": 2, "header_name": "同步", "width": 40, "extend": None, "color_switch": "speech_audio_synchronize",
        "display_type": True,
        "color": {
            "1": [255, 255, 255],
            "0": [43, 43, 43]
        }
    },
    "display_subtitles": {
        "col": 3, "header_name": "字幕", "width": 40, "extend": None, "color_switch": False, "display_type": bool,
    },

}

header_subtitle = {
    "sort": {
        "col": 0, "header_name": "ID", "width": 40, "extend": None},
    "name": {
        "col": 1, "header_name": "字幕", "width": 290, "extend": None},
    "audio_file": {
        "col": 2, "header_name": "语音", "width": 40, "extend": None, "display_type": bool,
        "color_switch": "audio_file",
        "color": {
            "1": [255, 255, 255],
            "0": [43, 43, 43]
        }
    },
    "audio_time": {
        "col": 3, "header_name": "语音时长", "width": 60, "extend": None, "display_type": str,
    },
    "ext_time": {
        "col": 4, "header_name": "扩展时间", "width": 60, "extend": None, "display_type": str,
    },
    "media_count": {
        "col": 5, "header_name": "媒体", "width": 40, "extend": None, "display_type": str,
    },
    "fly_type": {
        "col": 6, "header_name": "动作", "width": 60, "extend": fly_type, "display_type": str,
    },

    "font": {
        "col": 7, "header_name": "字体", "width": 80, "extend": None, "display_type": str,
    },
    "font_size": {
        "col": 8, "header_name": "字号", "width": 50, "extend": None, "display_type": str,
    },
    "font_color": {
        "col": 9, "header_name": "字色", "width": 40, "extend": get_font_color(), "display_type": str,
    },
    "voice_local_name": {
        "col": 10, "header_name": "配音", "width": 40, "extend": None, "color_switch": False
    },
    "voice_role": {
        "col": 11, "header_name": "角色", "width": 40, "extend": None, "color_switch": False
    },
    "voice_style": {
        "col": 12, "header_name": "风格", "width": 40, "extend": None, "color_switch": False
    },

}

header_media = {
    "sort": {
        "col": 0, "header_name": "ID", "width": 40, "extend": None
    },
    "name": {
        "col": 1, "header_name": "名称", "width": 240, "extend": None,
    },
    "show_type": {
        "col": 2, "header_name": "显示模式", "width": 80, "extend": None, "display_type": str,
    },
    "media_type": {
        "col": 3, "header_name": "媒体类型", "width": 80, "extend": media_type_preset_for_table,
    },
    "media_delay": {
        "col": 4, "header_name": "延迟显示", "width": 80, "extend": None, "display_type": str,
    },
    "media_time": {
        "col": 5, "header_name": "显示时间", "width": 80, "extend": None, "display_type": str,
    }
}

header_subtitles_sub = {
    "fly_type": {
        "row": 0, "header_name": "动作类型", "width": 90, "extend": fly_type, "display_type": str,
    },
    "fly_to_place": {
        "row": 1, "header_name": "地名", "width": 90, "extend": None, "display_type": str,
    },
    "fly_to_longitude": {
        "row": 2, "header_name": "经度", "width": 90, "extend": None, "display_type": str,
    },
    "fly_to_latitude": {
        "row": 3, "header_name": "纬度", "width": 90, "extend": None, "display_type": str,
    },
    "fly_to_altitude": {
        "row": 4, "header_name": "海拔", "width": 90, "extend": None, "display_type": str,
    },
    "heading": {
        "row": 5, "header_name": "朝向", "width": 90, "extend": None, "display_type": str,
    },
    "tilt": {
        "row": 6, "header_name": "倾斜", "width": 90, "extend": None, "display_type": str,
    },
    "set_3d_view": {
        "row": 7, "header_name": "3D视图", "width": 90, "extend": None, "display_type": bool,
    },
    "set_2d_view": {
        "row": 8, "header_name": "2D视图", "width": 90, "extend": None, "display_type": bool,
    },
    "fly_speed": {
        "row": 9, "header_name": "飞行速度", "width": 90, "extend": None, "display_type": str,
    },
    "start_x": {
        "row": 10, "header_name": "起点 X", "width": 90, "extend": None, "display_type": str,
    },
    "start_y": {
        "row": 11, "header_name": "起点 Y", "width": 90, "extend": None, "display_type": str,
    },
    "end_x": {
        "row": 12, "header_name": "终点 X", "width": 90, "extend": None, "display_type": str,
    },
    "end_y": {
        "row": 13, "header_name": "终点 Y", "width": 90, "extend": None, "display_type": str,
    },
    "slide_speed": {
        "row": 14, "header_name": "滑动速度", "width": 90, "extend": None, "display_type": str,
    },
    "zoom_times": {
        "row": 15, "header_name": "滚轮次数", "width": 90, "extend": None, "display_type": str,
    },
    "voice_rate": {
        "row": 16, "header_name": "语速", "width": 90, "extend": None, "display_type": str,
    },
    "voice_volume": {
        "row": 17, "header_name": "音量", "width": 90, "extend": None, "display_type": str,
    },
    "voice_pitch": {
        "row": 18, "header_name": "音高", "width": 90, "extend": None, "display_type": str,
    }
}

header_media_2d_text = {
    "file": {
        "row": 0, "header_name": "内容", "width": 350, "extend": None, "display_type": str,
    },

    "font": {
        "row": 1, "header_name": "字体", "width": 350, "extend": None, "display_type": str,
    },
    "font_size": {
        "row": 2, "header_name": "字号", "width": 350, "extend": None, "display_type": str,
    },
    "font_color": {
        "row": 3, "header_name": "字色", "width": 350, "extend": get_font_color(), "display_type": str,
    },

    "width": {
        "row": 4, "header_name": "宽度", "width": 90, "extend": None, "display_type": str,
    },
    "height": {
        "row": 5, "header_name": "高度", "width": 350, "extend": None, "display_type": str,
    },

    "top": {
        "row": 6, "header_name": "TOP", "width": 350, "extend": None, "display_type": int,
    },
    "left": {
        "row": 7, "header_name": "LEFT", "width": 350, "extend": None, "display_type": int,
    },

    "opacity": {
        "row": 8, "header_name": "不透明度", "width": 350, "extend": None, "display_type": str,
    },

    "transaction_to_3d": {
        "row": 9, "header_name": "2D转3D", "width": 350, "extend": None, "display_type": bool,
    },
    "full_screen": {
        "row": 10, "header_name": "全屏", "width": 350, "extend": None, "display_type": bool,
    },
    "keep": {
        "row": 11, "header_name": "结束保留", "width": 350, "extend": None, "display_type": bool,
    }
}

header_media_2d_bgm = {
    "file": {
        "row": 0, "header_name": "内容", "width": 350, "extend": None, "display_type": str,
    },
}

header_media_2d_image_video = {
    "file": {
        "row": 0, "header_name": "内容", "width": 350, "extend": None, "display_type": str,
    },

    "width": {
        "row": 1, "header_name": "宽度", "width": 90, "extend": None, "display_type": str,
    },
    "height": {
        "row": 2, "header_name": "高度", "width": 350, "extend": None, "display_type": str,
    },

    "top": {
        "row": 3, "header_name": "TOP", "width": 350, "extend": None, "display_type": int,
    },
    "left": {
        "row": 4, "header_name": "LEFT", "width": 350, "extend": None, "display_type": int,
    },

    "opacity": {
        "row": 5, "header_name": "不透明度", "width": 350, "extend": None, "display_type": str,
    },

    "transaction_to_3d": {
        "row": 6, "header_name": "2D转3D", "width": 350, "extend": None, "display_type": bool,
    },
    "full_screen": {
        "row": 7, "header_name": "全屏", "width": 350, "extend": None, "display_type": bool,
    },
    "keep": {
        "row": 8, "header_name": "结束保留", "width": 350, "extend": None, "display_type": bool,
    },
    "aspect": {
        "row": 9, "header_name": "原图比例", "width": 350, "extend": None, "display_type": str,
    }
}

header_media_3d_text = {
    "file": {
        "row": 0, "header_name": "内容", "width": 350, "extend": None, "display_type": str,
    },

    "font": {
        "row": 1, "header_name": "字体", "width": 350, "extend": None, "display_type": str,
    },
    "font_size": {
        "row": 2, "header_name": "字号", "width": 350, "extend": None, "display_type": str,
    },
    "font_color": {
        "row": 3, "header_name": "字色", "width": 350, "extend": get_font_color(), "display_type": str,
    },

    "longitude": {
        "row": 4, "header_name": "经度", "width": 350, "extend": None, "display_type": str,
    },
    "latitude": {
        "row": 5, "header_name": "纬度", "width": 350, "extend": None, "display_type": str,
    },
    "altitude": {
        "row": 6, "header_name": "海拔", "width": 350, "extend": None, "display_type": str,
    },
    "width": {
        "row": 7, "header_name": "宽度", "width": 350, "extend": None, "display_type": str,
    },
    "height": {
        "row": 8, "header_name": "高度", "width": 350, "extend": None, "display_type": str,
    },
    "depth": {
        "row": 9, "header_name": "纵深", "width": 350, "extend": None, "display_type": str,
    },
    "parallel": {
        "row": 10, "header_name": "躺着", "width": 350, "extend": None, "display_type": bool,
    }
}

header_media_3d_image_video = {
    "file": {
        "row": 0, "header_name": "内容", "width": 350, "extend": None, "display_type": str,
    },

    "longitude": {
        "row": 1, "header_name": "经度", "width": 350, "extend": None, "display_type": str,
    },
    "latitude": {
        "row": 2, "header_name": "纬度", "width": 350, "extend": None, "display_type": str,
    },
    "altitude": {
        "row": 3, "header_name": "海拔", "width": 350, "extend": None, "display_type": str,
    },
    "width": {
        "row": 4, "header_name": "宽度", "width": 350, "extend": None, "display_type": str,
    },
    "height": {
        "row": 5, "header_name": "高度", "width": 350, "extend": None, "display_type": str,
    },
    "depth": {
        "row": 6, "header_name": "纵深", "width": 350, "extend": None, "display_type": str,
    },
    "parallel": {
        "row": 7, "header_name": "躺着", "width": 350, "extend": None, "display_type": bool,
    },
    "aspect": {
        "row": 8, "header_name": "原图比例", "width": 350, "extend": None, "display_type": str,
    }
}

header_media_3d_kml = {
    "file": {
        "row": 0, "header_name": "文件", "width": 350, "extend": None, "display_type": str,
    },
    "keep": {
        "row": 1, "header_name": "保留", "width": 350, "extend": None, "display_type": bool,
    }
}

header_media_3d_overlay = {
    "file": {
        "row": 0, "header_name": "内容", "width": 350, "extend": None, "display_type": str,
    },
    "longitude_1": {
        "row": 1, "header_name": "经度一", "width": 350, "extend": None, "display_type": str,
    },
    "latitude_1": {
        "row": 2, "header_name": "纬度一", "width": 350, "extend": None, "display_type": str,
    },

    "longitude_2": {
        "row": 3, "header_name": "经度二", "width": 350, "extend": None, "display_type": str,
    },
    "latitude_2": {
        "row": 4, "header_name": "纬度二", "width": 350, "extend": None, "display_type": str,
    },
    "longitude_3": {
        "row": 5, "header_name": "经度三", "width": 350, "extend": None, "display_type": str,
    },
    "latitude_3": {
        "row": 6, "header_name": "纬度三", "width": 350, "extend": None, "display_type": str,
    },
    "longitude_4": {
        "row": 7, "header_name": "经度四", "width": 350, "extend": None, "display_type": str,
    },
    "latitude_4": {
        "row": 8, "header_name": "纬度四", "width": 350, "extend": None, "display_type": str,
    },
    "keep": {
        "row": 9, "header_name": "保留", "width": 350, "extend": None, "display_type": bool,
    }
}

header_media_3d_motion_line = {
    "file": {
        "row": 0, "header_name": "内容", "width": 350, "extend": None, "display_type": str,
    },

    "color": {
        "row": 1, "header_name": "颜色", "width": 350, "extend": None, "display_type": str,
    },
    "line_weight": {
        "row": 2, "header_name": "线粗", "width": 350, "extend": None, "display_type": str,
    },
    "motion_speed": {
        "row": 3, "header_name": "速度", "width": 350, "extend": None, "display_type": str,
    },

    "motion_time": {
        "row": 4, "header_name": "时间", "width": 350, "extend": None, "display_type": str,
    },
    "line_divide": {
        "row": 5, "header_name": "分段", "width": 350, "extend": None, "display_type": str,
    },
    "height": {
        "row": 6, "header_name": "高度", "width": 350, "extend": None, "display_type": str,
    }
}

header_local_subtitles_move = {
    "id": {
        "col": 0, "header_name": "ID", "width": 40, "extend": None},
    "subtitle": {
        "col": 1, "header_name": "字幕", "width": 400, "extend": None}
}

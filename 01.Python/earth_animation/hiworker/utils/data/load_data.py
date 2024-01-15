import time

from .img import InitImage
from .coord import Coordinate
from ...signal.signal import signal_hi_worker
# from hiworker.darknet_v3 import yolo3
# from hiworker.darknet_v4 import yolo4


def load_data(img_data: InitImage, coord_data: Coordinate, from_zip=True):
    """
    加载应用数据
    :param img_data: 图像数据对象
    :param coord_data: 坐标数据对象
    :param from_zip:  bool 是否从压缩包加载
    :return:
    """
    signal_hi_worker.show_load_data.emit("正在加载[基础数据]，请稍后。。。")
    if coord_data.load_coord(from_zip=from_zip):
        signal_hi_worker.show_load_data.emit("正在加载[图像数据]，请稍后。。。")
        if img_data.load_all_image(from_zip=from_zip):
            signal_hi_worker.show_load_data.emit("[图像数据]加载完成")
            time.sleep(2)
            signal_hi_worker.close_info.emit()
        else:
            signal_hi_worker.show_load_data.emit("[数据image]加载失败，请检查数据")
    else:
        signal_hi_worker.show_load_data.emit("[数据coordinate]加载失败，请检查数据")

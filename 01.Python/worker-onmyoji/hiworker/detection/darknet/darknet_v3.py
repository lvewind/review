#!python3
"""
Python 3 wrapper for identifying objects in images

Requires DLL compilation

Both the GPU and no-GPU version should be compiled; the no-GPU version should be renamed "yolo_cpp_dll_nogpu.dll".

On a GPU system, you can force CPU evaluation by any of:

- Set global variable DARKNET_FORCE_CPU to True
- Set environment variable CUDA_VISIBLE_DEVICES to -1
- Set environment variable "FORCE_CPU" to "true"


To use, either image_coordinate performDetect() after import, or modify the end of this file.

See the docstring of performDetect() for parameters.

Directly viewing or returning bounding-boxed images requires scikit-image to be installed (`pip install scikit-image`)


Original *nix 2.7: https://github.com/pjreddie/darknet/blob/0f110834f4e18b30d5f101bf8f1724c34b7b83db/python/darknet.py
Windows Python 2.7 version: https://github.com/AlexeyAB/darknet/blob/fc496d52bf22a0bb257300d3c79be9cd80e722cb/build/darknet/x64/darknet.py

@author: Philip Kahn
@date: 20180503
"""
# pylint: disable=R, W0401, W0614, W0703
from ctypes import *
# import math
import cv2
import random
import os


def sample(probs):
    s = sum(probs)
    probs = [a / s for a in probs]
    r = random.uniform(0, 1)
    for i in range(len(probs)):
        r = r - probs[i]
        if r <= 0:
            return i
    return len(probs) - 1


def c_array(ctype, values):
    arr = (ctype * len(values))()
    arr[:] = values
    return arr


class BOX(Structure):
    _fields_ = [("x", c_float),
                ("y", c_float),
                ("w", c_float),
                ("h", c_float)]


class DETECTION(Structure):
    _fields_ = [("bbox", BOX),
                ("classes", c_int),
                ("prob", POINTER(c_float)),
                ("mask", POINTER(c_float)),
                ("objectness", c_float),
                ("sort_class", c_int),
                ("uc", POINTER(c_float)),
                ("points", c_int)]


class IMAGE(Structure):
    _fields_ = [("w", c_int),
                ("h", c_int),
                ("c", c_int),
                ("storage", POINTER(c_float))]


class METADATA(Structure):
    _fields_ = [("classes", c_int),
                ("names", POINTER(c_char_p))]


# bin = CDLL("/home/pjreddie/documents/net/libdarknet.so", RTLD_GLOBAL)
# bin = CDLL("libdarknet.so", RTLD_GLOBAL)
hasGPU = True

# cwd = os.path.dirname(__file__)
# os.environ['PATH'] = cwd + ';' + os.environ['PATH']
# winGPUdll = os.path.join(cwd, "v3.dll")
# winNoGPUdll = os.path.join(cwd, "yolo_cpp_dll_nogpu.dll")

cwd = os.path.abspath("..") + os.path.sep + "bin" + os.path.sep
print(cwd)
os.environ['PATH'] = cwd + ';' + os.environ['PATH']
winGPUdll = os.path.join(cwd, "v3.dll")
# winGPUdll = os.path.join(cwd, "dark.dll")
# winGPUdll = os.path.join(cwd, "v4.dll")
winNoGPUdll = os.path.join(cwd, "yolo_cpp_dll_nogpu.dll")
# winNoGPUdll = os.path.abspath(".") + os.path.sep + "bin" + os.path.sep + "yolo_cpp_dll_nogpu.dll"
# bin = CDLL(winGPUdll, RTLD_GLOBAL)
# envKeys = list()    # 初始化环境变量名列表
# for k, v in os.environ.items(): # 生成环境变量名列表
#     envKeys.append(k)
# bin = CDLL(winGPUdll, RTLD_GLOBAL)
lib = CDLL(winGPUdll, RTLD_GLOBAL)
# bin = cdll.LoadLibrary(winGPUdll)

lib.network_width.argtypes = [c_void_p]
lib.network_width.restype = c_int
lib.network_height.argtypes = [c_void_p]
lib.network_height.restype = c_int

copy_image_from_bytes = lib.copy_image_from_bytes
copy_image_from_bytes.argtypes = [IMAGE, c_char_p]


def network_width(net):
    return lib.network_width(net)


def network_height(net):
    return lib.network_height(net)


predict = lib.network_predict_ptr
predict.argtypes = [c_void_p, POINTER(c_float)]
predict.restype = POINTER(c_float)

if hasGPU:
    set_gpu = lib.cuda_set_device
    set_gpu.argtypes = [c_int]

init_cpu = lib.init_cpu

make_image = lib.make_image
make_image.argtypes = [c_int, c_int, c_int]
make_image.restype = IMAGE

get_network_boxes = lib.get_network_boxes
get_network_boxes.argtypes = [c_void_p, c_int, c_int, c_float, c_float, POINTER(c_int), c_int, POINTER(c_int), c_int]
get_network_boxes.restype = POINTER(DETECTION)

make_network_boxes = lib.make_network_boxes
make_network_boxes.argtypes = [c_void_p]
make_network_boxes.restype = POINTER(DETECTION)

free_detections = lib.free_detections
free_detections.argtypes = [POINTER(DETECTION), c_int]

free_ptrs = lib.free_ptrs
free_ptrs.argtypes = [POINTER(c_void_p), c_int]

network_predict = lib.network_predict_ptr
network_predict.argtypes = [c_void_p, POINTER(c_float)]

reset_rnn = lib.reset_rnn
reset_rnn.argtypes = [c_void_p]

load_net = lib.load_network
load_net.argtypes = [c_char_p, c_char_p, c_int]
load_net.restype = c_void_p

load_net_custom = lib.load_network_custom
load_net_custom.argtypes = [c_char_p, c_char_p, c_int, c_int]
load_net_custom.restype = c_void_p

do_nms_obj = lib.do_nms_obj
do_nms_obj.argtypes = [POINTER(DETECTION), c_int, c_int, c_float]

do_nms_sort = lib.do_nms_sort
do_nms_sort.argtypes = [POINTER(DETECTION), c_int, c_int, c_float]

free_image = lib.free_image
free_image.argtypes = [IMAGE]

letterbox_image = lib.letterbox_image
letterbox_image.argtypes = [IMAGE, c_int, c_int]
letterbox_image.restype = IMAGE

load_meta = lib.get_metadata
lib.get_metadata.argtypes = [c_char_p]
lib.get_metadata.restype = METADATA

load_image = lib.load_image_color
load_image.argtypes = [c_char_p, c_int, c_int]
load_image.restype = IMAGE

rgbgr_image = lib.rgbgr_image
rgbgr_image.argtypes = [IMAGE]

predict_image = lib.network_predict_image
predict_image.argtypes = [c_void_p, IMAGE]
predict_image.restype = POINTER(c_float)

predict_image_letterbox = lib.network_predict_image_letterbox
predict_image_letterbox.argtypes = [c_void_p, IMAGE]
predict_image_letterbox.restype = POINTER(c_float)


def array_to_image(arr):
    import numpy as np
    # need to return old values to avoid python freeing memory
    arr = arr.transpose(2, 0, 1)
    c = arr.shape[0]
    h = arr.shape[1]
    w = arr.shape[2]
    arr = np.ascontiguousarray(arr.flat, dtype=np.float32) / 255.0
    data = arr.ctypes.data_as(POINTER(c_float))
    im = IMAGE(w, h, c, data)
    return im, arr


class Yolov3:
    def __init__(self, configPath="./net/yolov3.cfg", weightPath="./net/yolov3.weights", metaPath="./net/fish.storage",
                 thresh=0.25, hier_thresh=.5, nms=.45):
        self.thresh = thresh
        self.hier_thresh = hier_thresh
        self.nms = nms

        self.configPath = configPath
        self.weightPath = weightPath
        self.metaPath = metaPath

        self.netMain = None
        self.metaMain = None
        self.altNames = None

        # global metaMain, netMain, altNames  # pylint: disable=W0603
        assert 0 < thresh < 1, "Threshold should be a float between zero and one (non-inclusive)"
        if not os.path.exists(configPath):
            raise ValueError("Invalid config path `" + os.path.abspath(configPath) + "`")
        if not os.path.exists(weightPath):
            raise ValueError("Invalid weight path `" + os.path.abspath(weightPath) + "`")
        if not os.path.exists(metaPath):
            raise ValueError("Invalid storage file path `" + os.path.abspath(metaPath) + "`")

    def load_net(self):
        if self.netMain is None:
            self.netMain = load_net_custom(self.configPath.encode("ascii"), self.weightPath.encode("ascii"), 0, 1)  # batch size = 1
        if self.metaMain is None:
            self.metaMain = load_meta(self.metaPath.encode("ascii"))
        if self.altNames is None:
            # In Python 3, the metafile default access craps out on Windows (but not Linux)
            # Read the names file and create a list to feed to detect
            try:
                with open(self.metaPath) as metaFH:
                    metaContents = metaFH.read()
                    import re
                    match = re.search("names *= *(.*)$", metaContents, re.IGNORECASE | re.MULTILINE)
                    if match:
                        result = match.group(1)
                    else:
                        result = None
                    try:
                        if os.path.exists(result):
                            with open(result) as namesFH:
                                namesList = namesFH.read().strip().split("\n")
                                self.altNames = [x.strip() for x in namesList]
                    except TypeError:
                        pass
            except Exception as e:
                print(e)

    def detect_cv2(self, im_cv2, debug=False, showImage=False):
        custom_image = cv2.cvtColor(im_cv2, cv2.COLOR_BGR2RGB)
        im, arr = array_to_image(custom_image)  # you should comment line below: free_image(im)
        num = c_int(0)
        if debug:
            print("Assigned num")
        pnum = pointer(num)
        if debug:
            print("Assigned pnum")
        predict_image(self.netMain, im)
        letter_box = 0
        # predict_image_letterbox(net, im)
        # letter_box = 1
        if debug:
            print("did prediction")
        # dets = get_network_boxes(net, custom_image_bgr.shape[1], custom_image_bgr.shape[0], thresh, hier_thresh, None, 0, pnum, letter_box) # OpenCV
        dets = get_network_boxes(self.netMain, im.w, im.h, self.thresh, self.hier_thresh, None, 0, pnum, letter_box)
        if debug:
            print("Got dets")
        num = pnum[0]
        if debug:
            print("got zeroth index of pnum")
        if self.nms:
            do_nms_sort(dets, num, self.metaMain.classes, self.nms)
        if debug:
            print("did sort")
        res = []
        if debug:
            print("about to range")
        for j in range(c_int(num).value):
            if debug:
                print("Ranging on " + str(j) + " of " + str(num))
            if debug:
                print("Classes: " + str(self.metaMain), self.metaMain.classes, self.metaMain.names)
            for i in range(self.metaMain.classes):
                if debug:
                    print("Class-ranging on " + str(i) + " of " + str(self.metaMain.classes) + "= " + str(dets[j].prob[i]))
                if dets[j].prob[i] > 0:
                    b = dets[j].bbox
                    if self.altNames is None:
                        nameTag = self.metaMain.names[i]
                    else:
                        nameTag = self.altNames[i]
                    if debug:
                        print("Got bbox", b)
                        print(nameTag)
                        print(dets[j].prob[i])
                        print((b.x, b.y, b.w, b.h))
                    res.append((nameTag, dets[j].prob[i], (b.x, b.y, b.w, b.h)))
        if debug:
            print("did range")
        res = sorted(res, key=lambda x: -x[1])
        if debug:
            print("did sort")
        free_detections(dets, num)
        if debug:
            print("freed detections")
        # if showImage:
        #     detections = res
        #     try:
        #         from skimage import io, draw
        #         import numpy as np
        #         # image = io.imread(imagePath)
        #         image = custom_image
        #         print("*** " + str(len(detections)) + " Results, color coded by confidence ***")
        #         imcaption = []
        #         for detection in detections:
        #             label = detection[0]
        #             confidence = detection[1]
        #             pstring = label + ": " + str(np.rint(100 * confidence)) + "%"
        #             imcaption.append(pstring)
        #             print(pstring)
        #             bounds = detection[2]
        #             shape = image.shape
        #             # x = shape[1]
        #             # xExtent = int(x * bounds[2] / 100)
        #             # y = shape[0]
        #             # yExtent = int(y * bounds[3] / 100)
        #             yExtent = int(bounds[3])
        #             xEntent = int(bounds[2])
        #             # Coordinates are around the center
        #             xCoord = int(bounds[0] - bounds[2] / 2)
        #             yCoord = int(bounds[1] - bounds[3] / 2)
        #             boundingBox = [
        #                 [xCoord, yCoord],
        #                 [xCoord, yCoord + yExtent],
        #                 [xCoord + xEntent, yCoord + yExtent],
        #                 [xCoord + xEntent, yCoord]
        #             ]
        #             # Wiggle it around to make a 3px border
        #             rr, cc = draw.polygon_perimeter([x[1] for x in boundingBox], [x[0] for x in boundingBox], shape=shape)
        #             rr2, cc2 = draw.polygon_perimeter([x[1] + 1 for x in boundingBox], [x[0] for x in boundingBox], shape=shape)
        #             rr3, cc3 = draw.polygon_perimeter([x[1] - 1 for x in boundingBox], [x[0] for x in boundingBox], shape=shape)
        #             rr4, cc4 = draw.polygon_perimeter([x[1] for x in boundingBox], [x[0] + 1 for x in boundingBox], shape=shape)
        #             rr5, cc5 = draw.polygon_perimeter([x[1] for x in boundingBox], [x[0] - 1 for x in boundingBox], shape=shape)
        #             boxColor = (int(255 * (1 - (confidence ** 2))), int(255 * (confidence ** 2)), 0)
        #             draw.set_color(image, (rr, cc), boxColor, alpha=0.8)
        #             draw.set_color(image, (rr2, cc2), boxColor, alpha=0.8)
        #             draw.set_color(image, (rr3, cc3), boxColor, alpha=0.8)
        #             draw.set_color(image, (rr4, cc4), boxColor, alpha=0.8)
        #             draw.set_color(image, (rr5, cc5), boxColor, alpha=0.8)
        #         io.imshow(image)
        #         io.show()
        #
        #     except Exception as e:
        #         print("Unable to show image: " + str(e))
        return res


yolo3 = Yolov3(thresh=0.25,
               configPath="./net/yolo3-fishing-zhuanzhuanyu.cfg",
               weightPath="./net/yolo3-fishing-zhuanzhuanyu_best.weights",
               metaPath="./net/zhuanzhuanyu.storage")

# if __name__ == "__main__":
#     # print(performDetect())
#     import time
#     imcv2 = cv2.imread("_training_v3/storage/zhuanzhuanyu/img/2020260154_1580918514.3426857.png")
#     time_start = time.time()
#     detect_result = yolo3.detect_cv2(imcv2, showImage=False)
#     print(time.time() - time_start)
#     print(detect_result)

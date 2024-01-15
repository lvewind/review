import json
import time
# from threading import Thread

import selenium.common
import os

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

from app.utils import get_font_list
from ..static import WebConfig


chrome_version = "112.0.5615.50"
chrome_folder = "data\\bin\\chrome\\"

chrome_path = os.path.join(chrome_folder, chrome_version, "chrome.exe")
driver_path = os.path.join(chrome_folder, chrome_version, "chromedriver.exe")
user_data = os.path.join(chrome_folder, chrome_version, "User Data")


class EarthDriver(Chrome):
    def __init__(self, chrome=chrome_path, driver_file=driver_path, user_data_dir=user_data, kiosk=False):
        self.options = ChromeOptions()
        self.options.binary_location = os.path.join(os.getcwd(), chrome)
        self.options.add_argument('window-size=2560,1440')
        self.user_data_dir = os.path.join(os.getcwd(), user_data_dir)
        self.street_view_on = False
        self.kiosk = kiosk
        self.earth_inited = False
        self.js_rul_list = []
        if self.user_data_dir:
            self.options.add_argument('user-data-dir=' + self.user_data_dir)
        # self.options.add_argument('--disable-web-security')
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        if self.kiosk:
            self.options.add_argument('--kiosk')
        self.driver_url = os.path.join(os.path.abspath(os.getcwd()), driver_file)
        try:
            super(EarthDriver, self).__init__(executable_path=self.driver_url, options=self.options, desired_capabilities=None)
            # super(EarthDriver, self).__init__(service=Service(ChromeDriverManager().install()), options=self.options, desired_capabilities=None)
        except selenium.common.exceptions.SessionNotCreatedException as e:
            print(e)
        except selenium.common.exceptions.InvalidArgumentException:
            print("请关闭浏览器再使用本工具")
        except selenium.common.exceptions.WebDriverException:
            print("请重新设置浏览器用户目录后重新启动本软件")

    def open_web_page(self):
        self.earth_inited = False
        self.set_window_rect(0, 0, 2560, 1400)
        try:
            print("正在打开页面")
            handles = self.window_handles
            # window_count = len(handles)
            # for n in range(1, window_count):
            #     self.switch_to.window(handles[n])
            #     self.run_js("window.close()")
            self.switch_to.window(handles[0])
            url = "https://earth.google.com/web"
            self.get(url)
            self.switch_to.default_content()
            print("页面已打开, 页面数据加载完全后点击 初始化")

        except selenium.common.exceptions.ElementNotInteractableException as e:
            print(e)
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
        except selenium.common.exceptions.WebDriverException as e:
            print(e)
            if "chrome not reachable" in str(e.msg):
                try:
                    super(EarthDriver, self).__init__(executable_path=self.driver_url, options=self.options,
                                                      desired_capabilities=None)
                except selenium.common.exceptions.SessionNotCreatedException as e:
                    print(e)
                except selenium.common.exceptions.InvalidArgumentException:
                    print("请关闭浏览器后重启本工具")

                self.open_web_page()
        except AttributeError as e:
            print(e)
        except TypeError as e:
            print(e)

    # 初始js注入
    def init_earth(self, js_server: str, media_server: str, font_server: str, cesium_base_url: str):
        if not self.earth_inited:
            self.init_inject_function(js_server, media_server, font_server, cesium_base_url)
            self.inject_earth_js_from_server()
            self.earth_inited = True

    # UI控制
    def hide_earth_ui(self):
        self.run_js("window.earthControl.showEarthUi(arguments[0])", "0")

    def show_earth_ui(self):
        self.run_js("window.earthControl.showEarthUi(arguments[0])", "1")

    def search_place(self, place: str):
        self.run_js("window.earthControl.searchPlace(arguments[0])", place)

    def close_current_search(self):
        self.run_js("window.earthControl.closeCurrentSearch()")

    def fly_to_lla(self, longitude, latitude, altitude):
        self.run_js("window.earthControl.flyToLla(arguments[0], arguments[1], arguments[2])", longitude, latitude, altitude)

    def zoom_to_space(self):
        self.run_js("window.earthControl.zoomToSpace()")

    def get_camera_state(self):
        return self.run_js("return window.earthPlay.parseCameraState()")

    def get_camera_position(self):
        return self.run_js("return window.earthControl.getCameraPosition()")

    def set_2d_view(self):
        self.run_js("window.earthControl.setView2d()")

    def set_3d_view(self):
        self.run_js("window.earthControl.setView3d()")

    def set_compass_heading_reset(self):
        self.run_js("window.earthControl.setCompassHeadingReset()")

    def show_street_view(self):
        if not self.street_view_on:
            self.run_js("window.earthControl.showStreetView()")
            self.street_view_on = True
        else:
            self.run_js("window.earthControl.hideStreetView()")
            self.street_view_on = False

    # 显示2D内容
    def display_subtitle(self, data_dict: dict):
        data_dict_str = json.dumps(data_dict)
        self.run_js("window.Subtitles.displaySubtitle(arguments[0])", data_dict_str)

    def clear_subtitle(self):
        self.run_js("window.Subtitles.clearSubtitle()")

    def display_screen_image(self, media: dict, media_prop: dict):
        self.run_js("window.earthPlay.Play2d.displayImage(arguments[0], arguments[1])", json.dumps(media), json.dumps(media_prop))

    def display_screen_video(self, media: dict, media_prop: dict):
        self.run_js("window.earthPlay.Play2d.displayVideo(arguments[0], arguments[1])", json.dumps(media), json.dumps(media_prop))

    def display_screen_text(self, media: dict, media_prop: dict):
        self.run_js("window.earthPlay.Play2d.displayText(arguments[0], arguments[1])", json.dumps(media), json.dumps(media_prop))

    # 显示3D内容
    def show_object_in_three(self, data_dict: dict):
        self.run_js("window.earthPlay.Play3d.showInThree(arguments[0])", json.dumps(data_dict))

    def display_three_image(self, media: dict, media_prop: dict):
        self.run_js("window.earthPlay.Play3d.showImage(arguments[0], arguments[1])", json.dumps(media), json.dumps(media_prop))

    def display_three_video(self, media: dict, media_prop: dict):
        self.run_js("window.earthPlay.Play3d.showVideo(arguments[0], arguments[1])", json.dumps(media), json.dumps(media_prop))

    def display_three_text(self, media: dict, media_prop: dict):
        self.run_js("window.earthPlay.Play3d.showText(arguments[0], arguments[1])", json.dumps(media), json.dumps(media_prop))

    def display_three_kml(self, media: dict, media_prop: dict):
        self.run_js("window.earthPlay.Play3d.showKml(arguments[0], arguments[1])", json.dumps(media), json.dumps(media_prop))

    def display_three_overlay(self, media: dict, media_prop: dict):
        self.run_js("window.earthPlay.Play3d.showOverlay(arguments[0], arguments[1])", json.dumps(media), json.dumps(media_prop))

    def display_three_motion_line(self, media: dict, media_prop: dict):
        self.run_js("window.earthPlay.Play3d.showMotionLine(arguments[0], arguments[1])", json.dumps(media), json.dumps(media_prop))

    def display_three_model(self, media: dict, media_prop: dict):
        self.run_js("window.earthPlay.Play3d.showModel(arguments[0], arguments[1])", json.dumps(media), json.dumps(media_prop))

    def clear_all_data(self, delay=0.001):
        time.sleep(delay)
        self.run_js("window.earthPlay.Play3d.clearAllThree()")
        self.close_current_search()
        self.clear_subtitle()

    def open_cesium(self):
        js = """
        function post_test() {
        window.cesiumWindow.postMessage("cesium_post_back", "*")
        console.log(window.cesiumWindow);
        }
        window.cesiumWindow = window.open("https://cesium.test/");
        setInterval(post_test, 1000);
        """
        self.run_js(js)

    def init_inject_function(self, js_server: str, media_server: str, font_server: str, cesium_base_url: str):
        """
        :return:
        """
        js = """window.CESIUM_BASE_URL = '""" + cesium_base_url + """';
                window.mediaServer = '""" + media_server + """';
                window.fontsServer = '""" + font_server + """';
                window.jsServer = '""" + js_server + """';
                window.jsURL = '';
                
                window.injectFunction = function (){
                const xhttp = new XMLHttpRequest();
                xhttp.open("GET", window.jsServer);
                xhttp.send();

                xhttp.onreadystatechange = (e) => {
                if (xhttp.readyState==4 && xhttp.status==200)
                    {
                        let text = xhttp.responseText;
                        let srcStart = text.indexOf("src=");
                        let srcEnd = text.indexOf('"></script>');
                        let src = text.slice(srcStart + 5, srcEnd);
                        console.log(src);
                        
                        let scriptElement=document.createElement('script');
                        scriptElement.type='module';
                        scriptElement.crossorigin='anonymous';
                        scriptElement.src=window.jsServer + src;
                        document.body.appendChild(scriptElement);
                    }
                    
                }}"""
        self.run_js(js)

    def inject_earth_js_from_server(self):
        self.run_js("window.injectFunction()")

    def inject_earth_js(self):
        self.load_earth_js(os.path.join(os.getcwd(), "data", "earthjs"))

    def load_earth_js(self, earth_js_path, sub_dir=None):
        self.js_rul_list = []
        files = os.listdir(earth_js_path)
        for file in files:
            if os.path.isfile(os.path.join(earth_js_path, file)):
                if os.path.splitext(file)[-1] == ".js":
                    if sub_dir:
                        file = sub_dir + "/" + file
                    self.run_js("window.injectFunction(arguments[0])", WebConfig.earth_js + file)
                    self.js_rul_list.append(WebConfig.earth_js + file)
            else:
                self.load_earth_js(os.path.join(earth_js_path, file), file)

    def init_fonts(self):
        font_list = get_font_list()
        if font_list:
            font_list = json.dumps(font_list)
            self.run_js("window.earthPlay.initFonts(arguments[0])", font_list)

    def open_window(self, url):
        self.run_js("window.open(arguments[0])", url)

    def sync_earth_cesium(self):
        while True:
            if len(self.window_handles) >= 2:
                self.switch_to.window(self.window_handles[0])
                camera_state = self.run_js("window.earthPlay.GetCameraState();")
                self.switch_to.window(self.window_handles[1])
                cesium_camera_matrix = self.run_js("window.getCurrentCameraPositionFromStr(arguments[0])", json.dumps(camera_state))
                self.switch_to.window(self.window_handles[0])
                self.run_js("window.earthPlay.setCameraMatrix(arguments[0]);", json.dumps(cesium_camera_matrix))

    def run_js(self, js: str, *args):
        try:
            return self.execute_script(js, *args)
        except selenium.common.exceptions.JavascriptException as e:
            print(str(e.msg))

    # NASA数据下载
    def open_nasa_page(self):
        try:
            print("正在打开页面")
            handles = self.window_handles
            self.switch_to.window(handles[0])
            url = "https://search.earthdata.nasa.gov/downloads/5234862342"
            self.get(url)
            print("Earth页面打开完成, 页面数据加载完全后继续")

        except selenium.common.exceptions.ElementNotInteractableException as e:
            print(e)
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
        except selenium.common.exceptions.WebDriverException as e:
            print(e)
        except AttributeError as e:
            print(e)
        except TypeError as e:
            print(e)

    def download_nasa_data(self):
        import pathlib
        with open("nasa-download.txt") as download_file:
            files = download_file.readlines()
            print(files)
            for file_url in files:
                file_name = file_url[file_url.rfind("/") + 1:].rstrip("\n")
                file_path = os.path.join("M:\\", "Downloads", file_name)
                file_path = pathlib.Path(file_path)
                if file_path.is_file():
                    continue
                else:
                    print(file_url)
                    time.sleep(0.5)
                    self.open_window(file_url)
                    if len(self.window_handles) >= 100:
                        time.sleep(100)


earth_driver = EarthDriver(kiosk=False)

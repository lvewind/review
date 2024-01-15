import requests
import json
import os
import hiworker
import webbrowser
import shutil
from threading import Thread
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError


def get_voice_list(azure_key):
    print("正在获取配音列表, 请稍等...")
    voice_list = []
    if azure_key:
        fetch_token_url = 'https://eastasia.tts.speech.microsoft.com/cognitiveservices/voices/list'
        headers = {
            'Ocp-Apim-Subscription-Key': azure_key
        }
        try:
            response = requests.get(fetch_token_url, headers=headers)
            if response.status_code == 200:
                data_list = response.text
                data_list = json.loads(data_list)
                if data_list:
                    voice_list_zh = []
                    for data in data_list:
                        voice_locale = data.get("Locale")
                        if voice_locale == "zh-CN" or voice_locale == "zh-TW" or voice_locale == "zh-HK":
                            voice_list_zh.append(data)
                    for voice_zh in voice_list_zh:
                        voice_list.append({
                            "short_name": voice_zh.get("ShortName"),
                            "local_name": voice_zh.get("LocalName"),
                            "style_list": voice_zh.get("StyleList"),
                            "role_play_list": voice_zh.get("RolePlayList"),
                        })
        except requests.exceptions.ConnectionError:
            pass
    hiworker.JsonReadWrite.save_json(voice_list, os.path.join(os.getcwd(), "data", "user"), "voices.json")
    print("配音列表获取完成.")
    return voice_list


def load_voice_list_from_json(azure_key):
    json_path = os.path.join(os.getcwd(), "data", "user", "voices.json")
    if not os.path.isfile(json_path):
        get_voice_list(azure_key)
    return hiworker.JsonReadWrite.load_json_file(json_path)


def get_font_list():
    font_list = []
    font_folder = os.path.join(os.getcwd(), "data", "fonts")
    if os.path.isdir(font_folder):
        file_list = os.listdir(font_folder)
        for file in file_list:
            if ".json" == os.path.splitext(file)[-1]:
                font_name = os.path.splitext(file)[0]
                if font_name == "工业黑简体":
                    font_list.insert(0, font_name)
                else:
                    font_list.append(font_name)

    return font_list


def rename_folder(old_folder, new_folder):
    if not os.path.exists(old_folder):
        os.makedirs(new_folder, exist_ok=True)
    elif old_folder == new_folder:
        return
    else:
        try:
            os.rename(old_folder, new_folder)
        except FileNotFoundError:
            print("目录不存在")
        except PermissionError:
            print("权限错误，请手动修改目录")


def create_new_file_name(source_file: str, media_name: str, file_id: str):
    old_file_name = os.path.basename(source_file)
    ext_name = old_file_name.split('.')[-1]
    if not media_name:
        media_name = "未命名" + str(file_id)
    return media_name + "." + ext_name


def copy_file(source_file, target_file):
    if os.path.isfile(source_file):
        Thread(target=shutil.copyfile, args=(source_file, target_file)).start()


def get_font_color():
    jrw = hiworker.JsonReadWrite()
    json_data = jrw.load_json_file(os.path.join(os.getcwd(), "data", "user", "font_color.json"))
    if not json_data:
        json_data = {}
    return json_data


def parse_coord(camera_position: dict):
    if camera_position:
        status = True
        camera_altitude = camera_position.get("camera_altitude", "")
        camera_altitude = camera_altitude.lstrip("相机：")
        camera_altitude = camera_altitude.replace(",", "")
        if "米" in camera_altitude:
            camera_altitude = int(camera_altitude.rstrip("米"))
        elif "公里" in camera_altitude:
            camera_altitude = int(camera_altitude.rstrip("公里")) * 1000
        pointer_coordinates = camera_position.get("pointer_coordinates", "")
        pointer_coordinates.replace("\n", "")
        pointer_coordinates = pointer_coordinates.split(" ")
        latitude = pointer_coordinates[0].strip()
        longitude = pointer_coordinates[1].strip()
        if "N" in latitude:
            latitude = latitude[:-2]
        else:
            latitude = "-" + latitude[:-2]

        if "E" in longitude:
            longitude = longitude[:-2]
        else:
            longitude = "-" + longitude[:-2]
        altitude = camera_position.get("pointer_elevation", "")
        if altitude:
            altitude = altitude.strip("米")
            altitude = altitude.strip()
            altitude = altitude.replace(",", "")
            altitude = altitude[:-2]

        return longitude, latitude, altitude, camera_altitude, status


def open_help_page():
    webbrowser.open_new("https://www.bilibili.com/read/cv17670442")


def show_message(message):
    print(message)


def get_wav_time(wav_path: str):
    if os.path.isfile(wav_path):
        try:
            wav = AudioSegment.from_wav(wav_path)
            if wav.duration_seconds > 1.5:
                audio_time = wav.duration_seconds - 0.5
            else:
                audio_time = wav.duration_seconds - 0.3
            return round(audio_time, 2)
        except CouldntDecodeError:
            return 0
        except FileNotFoundError:
            return 0
    else:
        return 0


def dict_sort(k):
    return k["sort"] if k["sort"] else k["id"]


def generate_overlay_kml(media_data: dict, collection_name, episode_name, earth_media_server):
    ll1 = str(media_data.get("longitude_1", " ")) + "," + str(media_data.get("latitude_1", " ")) + " "
    ll2 = str(media_data.get("longitude_2", " ")) + "," + str(media_data.get("latitude_2", " ")) + " "
    ll3 = str(media_data.get("longitude_3", " ")) + "," + str(media_data.get("latitude_3", " ")) + " "
    ll4 = str(media_data.get("longitude_4", " ")) + "," + str(media_data.get("latitude_4", " ")) + " "
    kml_name = media_data.get("file") + ".kml"
    kml_string = """<?xml version="1.0" encoding="UTF-8"?>
                            <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2"
                                 xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
                                <Document>
                                    <GroundOverlay>
                                        <Icon>
                                            <href>""" \
        + earth_media_server + collection_name + "/" + episode_name + "/three/overlay/" + media_data.get("file") \
        + """</href>
                                        </Icon>
                                        <altitude>0</altitude>
                                        <altitudeMode>clampToGround</altitudeMode>
                                        <gx:LatLonQuad>
                                            <coordinates>""" + ll1 + ll2 + ll3 + ll4 + """</coordinates>
                                        </gx:LatLonQuad>
                                    </GroundOverlay>
                                </Document>
                            </kml>
                        """
    kml_folder = os.path.join(os.getcwd(), "data", "media", collection_name, episode_name, "three", "overlay")
    if not os.path.exists(kml_folder):
        os.makedirs(kml_folder, exist_ok=True)
    kml_file = os.path.join(kml_folder, kml_name)
    with open(kml_file, mode="w+", encoding="utf-8") as k:
        k.write(kml_string)

    return earth_media_server + collection_name + "/" + episode_name + "/three/overlay/" + media_data.get("file") + ".kml"

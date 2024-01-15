from threading import Thread

from ..views import *
from ..utils import *
from ..models import SettingModel

import hiworker


class TTSPresenter:
    def __init__(self):
        self._view = TTSView()
        self._setting = SettingModel()
        view_sender.tts.generate_speech.connect(self.start_speech)
        self.voices = load_voice_list_from_json(self._setting.get_azure_key())

    def show(self):
        self._view.show_tts(self.voices)

    def start_speech(self, data):
        print(data)
        if data.get("content_type") == "content":
            self.speech_from_content()
        else:
            self.speech_from_file()

    def speech_from_content(self):
        content = self._view.textEdit_tts_content.toPlainText()
        output_path = self._view.lineEdit_output_path.text()
        voice_config = {
            "voice_name": self._view.comboBox_voice_name.currentData(),
            "voice_role": self._view.comboBox_voice_role.currentText(),
            "voice_style": self._view.comboBox_voice_style.currentText(),
        }
        if not output_path:
            return
        wav_name = self._view.lineEdit_output_name.text()
        if not wav_name:
            self.append_message("输出文件名为空.")
            return
        if content:

            file_name = os.path.join(output_path, wav_name + ".wav")
            speech = hiworker.Speech(subscription=self._setting.get_azure_key(), region=self._setting.get_azure_region())
            speech.set_voice_name(voice_config.get("voice_name"))
            Thread(target=speech.save_file_from_content, args=(content, file_name,)).start()
        else:
            self.append_message("合成内容为空.")

    def speech_from_file(self):
        speech = hiworker.Speech(subscription=self._setting.get_azure_key(), region=self._setting.get_azure_region())
        ssml_txt = self._view.lineEdit_tts_ssml_txt_path.text()
        output_path = self._view.lineEdit_output_path.text()
        if not output_path:
            return
        if ssml_txt:
            Thread(target=speech.save_file_from_ssml_txt, args=(ssml_txt, output_path)).start()
        else:
            self.append_message("合成内容为空.")

    def append_message(self, message):
        self._view.textBrowser_tts.append(str(message))

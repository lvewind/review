import os

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from app.views.ui import Ui_Dialog_tts
from app.views.sender import view_sender


class TTSView(QtWidgets.QDialog, Ui_Dialog_tts):
    def __init__(self, icon_path=None):
        super(TTSView, self).__init__()
        if icon_path:
            self.setWindowIcon(QIcon(os.path.join(os.getcwd(), icon_path)))
        self.setupUi(self)

        self.pushButton_voice_list.clicked.connect(view_sender.tts.refresh_voice_list.emit)

        self.radioButton_content.clicked.connect(self.toggle_ui)
        self.radioButton_ssml.clicked.connect(self.toggle_ui)
        self.pushButton_tts_ssml_txt_path.clicked.connect(self.select_ssml_txt)
        self.pushButton_output_path.clicked.connect(self.set_output_path)
        self.comboBox_voice_name.currentIndexChanged.connect(self.set_combobox_voice_role_style)

        self.pushButton_start.clicked.connect(self.send_data)

        self.voice_list = []
        self.data = {}

    def show_tts(self, voice_list: list):
        self.voice_list = voice_list
        self.set_combobox_voice_name()
        self.set_combobox_voice_role_style()
        self.show()

    def send_data(self):
        self.data.update({
            "content_type": "content" if self.radioButton_content.isChecked() else "ssml",
            "content": self.textEdit_tts_content.toPlainText(),
            "ssml_path": self.lineEdit_tts_ssml_txt_path.text(),
            "output_path": self.lineEdit_output_path.text(),
            "output_name": self.lineEdit_output_name.text(),
            "auto_overwrite": self.checkBox_auto_overwrite.isChecked(),
            "voice_name": self.comboBox_voice_name.currentData(),
            "voice_role": self.comboBox_voice_role.currentData(),
            "voice_style": self.comboBox_voice_style.currentData()
        })
        view_sender.tts.generate_speech.emit(self.data)

    def toggle_ui(self):
        if self.radioButton_ssml.isChecked():
            self.lineEdit_tts_ssml_txt_path.setEnabled(True)
            self.pushButton_tts_ssml_txt_path.setEnabled(True)
            self.textEdit_tts_content.setEnabled(False)
        else:
            self.lineEdit_tts_ssml_txt_path.setEnabled(False)
            self.pushButton_tts_ssml_txt_path.setEnabled(False)
            self.textEdit_tts_content.setEnabled(True)

    def select_ssml_txt(self):
        ssml_txt, result = QtWidgets.QFileDialog.getOpenFileName(caption="选择SSML或TXT", filter='(*.ssml; *.txt)', parent=self)
        if ssml_txt:
            self.lineEdit_tts_ssml_txt_path.setText(ssml_txt)

    def set_output_path(self):
        output_path = QtWidgets.QFileDialog.getExistingDirectory()
        if output_path:
            self.lineEdit_output_path.setText(output_path)

    def show_info(self, message: str):
        self.textBrowser_tts.append(message)

    def set_combobox_voice_name(self):
        self.comboBox_voice_name.clear()
        for index, voice in enumerate(self.voice_list):
            local_name = voice.get("local_name")
            short_name = voice.get("short_name")
            self.comboBox_voice_name.addItem(local_name, short_name)
            if local_name == "云希":
                self.comboBox_voice_name.setCurrentIndex(index)

    def set_combobox_voice_role_style(self):
        self.comboBox_voice_role.clear()
        self.comboBox_voice_style.clear()
        current_index = self.comboBox_voice_name.currentIndex()
        voice_style = self.voice_list[current_index].get("style_list")
        self.comboBox_voice_style.addItem("default")
        if voice_style:
            self.comboBox_voice_style.addItems(voice_style)
        voice_role = self.voice_list[current_index].get("role_play_list")
        self.comboBox_voice_role.addItem("default")
        if voice_role:
            self.comboBox_voice_role.addItems(voice_role)

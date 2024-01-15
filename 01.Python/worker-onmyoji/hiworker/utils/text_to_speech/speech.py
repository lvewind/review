import azure.cognitiveservices.speech as speech_sdk

from ...signal import signal_hi_worker


class Speech:
    def __init__(self,
                 language="zh_CN",
                 voice_name="zh-CN-YunxiNeural",
                 subscription="56636f6721b344339edc8c927b0d04a5",
                 region="eastasia"):
        # east_us_key = "2a8f4f206b7e400785cb9dda2c10cbee"
        # east_asia = "56636f6721b344339edc8c927b0d04a5"
        self.speech_config = speech_sdk.SpeechConfig(subscription=subscription, region=region)
        # Note: if only language is set, the default voice of that language is chosen.
        self.speech_config.speech_synthesis_language = language # For example, "de-DE"
        # The voice setting will overwrite the language setting.
        # The voice setting will [not overwrite] the voice element in input SSML.
        self.speech_config.speech_synthesis_voice_name =voice_name
        self.speech_config.set_speech_synthesis_output_format(speech_sdk.SpeechSynthesisOutputFormat.Riff48Khz16BitMonoPcm)
        # print(speech_sdk.version.__version__)

    def set_voice_name(self, voice_name: str):
        self.speech_config.speech_synthesis_voice_name = voice_name

    def save_file_from_content(self, text: str, output_filename: str, is_ssml=False):
        audio_config = speech_sdk.audio.AudioOutputConfig(filename=output_filename)
        synthesizer = speech_sdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_config)
        if is_ssml:
            synthesizer.speak_ssml(text)
        else:
            synthesizer.speak_text(text)
        signal_hi_worker.tts_finish.emit("文件保存成功.")

    def speech_from_content(self, text: str):
        audio_config = speech_sdk.audio.AudioOutputConfig(use_default_speaker=True)
        synthesizer = speech_sdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_config)
        synthesizer.speak_text_async(text)

    def output_stream_from_content(self, text: str, output_filename: str, is_ssml=False):
        synthesizer = speech_sdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=None)
        if is_ssml:
            result = synthesizer.speak_ssml_async(text).get()
        else:
            result = synthesizer.speak_text_async(text).get()
        stream = speech_sdk.AudioDataStream(result)
        if output_filename:
            stream.save_to_wav_file_async(output_filename)
            signal_hi_worker.tts_finish.emit("文件保存成功.")

    def save_file_from_ssml_txt(self, ssml_txt: str, output_filename):
        ssml_string, file_type = self.read_ssml_txt(ssml_txt)
        if ssml_string:
            if file_type == "txt":
                self.save_file_from_content(ssml_string, output_filename)
            elif file_type == "ssml":
                audio_config = speech_sdk.audio.AudioOutputConfig(filename=output_filename)
                synthesizer = speech_sdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_config)
                synthesizer.speak_ssml_async(ssml_string)
                signal_hi_worker.tts_finish.emit("文件保存成功.")

    def speech_from_ssml_txt(self, ssml_txt: str):
        ssml_string, file_type = self.read_ssml_txt(ssml_txt)
        if ssml_string:
            if file_type == "txt":
                self.speech_from_content(ssml_string)
            elif file_type == "ssml":
                audio_config = speech_sdk.audio.AudioOutputConfig(use_default_speaker=True)
                synthesizer = speech_sdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_config)
                synthesizer.speak_ssml_async(ssml_string)

    def output_stream_from_ssml_txt(self, ssml_txt: str, output_filename: str):
        ssml_string, file_type = self.read_ssml_txt(ssml_txt)
        if ssml_string:
            if file_type == "txt":
                self.output_stream_from_content(ssml_string, output_filename)
            elif file_type == "ssml":
                # audio_config = speech_sdk.audio.AudioOutputConfig(use_default_speaker=True)
                synthesizer = speech_sdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=None)
                result = synthesizer.speak_ssml_async(ssml_string).get()
                stream = speech_sdk.AudioDataStream(result)
                if output_filename:
                    stream.save_to_wav_file_async(output_filename)
                    signal_hi_worker.tts_finish.emit("文件保存成功.")

    @staticmethod
    def read_ssml_txt(ssml: str):
        file_type = ""
        if ".txt" in ssml:
            file_type = "txt"
        elif ".ssml" in ssml:
            file_type = "ssml"
        try:
            with open(ssml, "r", encoding="UTF-8") as ssml_string:
                return ssml_string.read(), file_type
        except FileNotFoundError:
            print("找不到文件：" + ssml)
            return False, False

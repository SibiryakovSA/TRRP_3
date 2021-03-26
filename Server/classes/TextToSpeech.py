import pyttsx3
import tempfile
from os import *
import io
from protobufDir import message_pb2
from datetime import datetime


class TextToSpeech:
    tts = pyttsx3.init()
    filePath = None
    bts = None
    text = ""

    def ConvertTextToSpeech(self, text=""):
        if text != "":
            self.text = text
            self.filePath = str(tempfile.NamedTemporaryFile().name).split('/')
            self.filePath = self.filePath[len(self.filePath)-1]
            filePath = self.filePath + ".wav"

            self.tts.save_to_file(text, filePath)
            self.tts.runAndWait()

            fd = io.open(filePath, 'rb')
            self.bts = fd.read()
            fd.close()
            remove(filePath)

            return self.bts
        return "-1"

    def SerializeWithProto(self):
        audio = message_pb2.audio()
        audio.content = self.bts
        audio.text = self.text
        audio.date = str(datetime.now())

        return audio.SerializeToString()

    @staticmethod
    def DeserializeText(data):
        audio = message_pb2.audio()
        audio.ParseFromString(data)
        return audio.text

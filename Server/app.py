from classes.TextToSpeech import TextToSpeech
from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=["post", "get"])
def server():
    text = TextToSpeech.DeserializeText(request.data)
    print(request.data)
    if text != "":
        tts = TextToSpeech()
        tts.ConvertTextToSpeech(text)
        res = tts.SerializeWithProto()
        print("Введенный текст: " + text)
        print("Возвращена строка байтов длинной " + str(len(res)) + " байт")
        return res
    return 'Текст не найден'


if __name__ == '__main__':
    app.run()

from classes.TextToSpeech import TextToSpeech
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def server():
    text = request.args.get('text', "")
    if text != "":
        tts = TextToSpeech()
        tts.ConvertTextToSpeech(text)
        return tts.SerializeWithProto()
    return 'Текст не найден'


if __name__ == '__main__':
    app.run()

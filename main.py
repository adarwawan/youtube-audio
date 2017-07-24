from flask import Flask, request, jsonify
from converter import *

app = Flask(__name__)


@app.route('/audio', methods=['GET'])
def downloadAudio():
    data = download_audio(request.args.get('id'))
    return jsonify(data)

@app.route('/video', methods=['GET'])
def downloadVideo():
    data = download_video(request.args.get('id'))
    return jsonify(data)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8888")
    )

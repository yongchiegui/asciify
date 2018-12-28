import ascii
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def asciify():
    data = request.get_json()
    image = data['image']
    width = data['width']
    height = data['height']

    result = {
        'result': ascii.asciify_base64(image, width, height)
    }

    return jsonify(result)

import base64
import cv2
import numpy


def asciify_base64(image_base64, width, height):
    numpy_array = numpy.fromstring(base64.b64decode(image_base64), numpy.uint8)
    image = cv2.imdecode(numpy_array, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, dsize=(width, height), fx=0, fy=0)
    return asciify(image)


def asciify_file(path, width, height):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, dsize=(width, height), fx=0, fy=0)
    return asciify(image)


def asciify(image):
    result = ''

    for a in image:
        for b in a:
            if b < 32:
                result += ' '
            elif b < 64:
                result += '.'
            elif b < 96:
                result += '*'
            elif b < 128:
                result += ':'
            elif b < 160:
                result += '!'
            elif b < 192:
                result += '+'
            elif b < 224:
                result += '#'
            else:
                result += '@'

        result += '\n'

    return result

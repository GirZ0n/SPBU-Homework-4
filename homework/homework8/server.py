from pathlib import Path

import numpy as np
import cv2
from flask import Flask, request, Response

from homework.homework8.object_detector import ObjectDetector

app = Flask(__name__)


@app.route("/", methods=["POST"])
def test():
    array = np.frombuffer(request.data, np.uint8)
    image = cv2.imdecode(array, cv2.IMREAD_COLOR)

    classes_path = Path("./resources/coco.names")
    configuration_path = Path("./resources/yolov3.cfg")
    weights_path = Path("./resources/yolov3.weights")
    detector = ObjectDetector(classes_path, configuration_path, weights_path)

    modified_image = detector.detect(image)

    _, modified_image_encoded = cv2.imencode(".png", modified_image)

    return Response(response=modified_image_encoded.tobytes(), mimetype="image/png")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)

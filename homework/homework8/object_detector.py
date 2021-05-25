from pathlib import Path
import cv2
import numpy as np


class ObjectDetector:
    conf_threshold = 0.5  # Confidence threshold
    nms_threshold = 0.4  # Non-maximum suppression threshold

    image_width = 416
    image_height = 416

    def __init__(self, classes: Path, configuration: Path, weights: Path):
        with open(classes) as file:
            self.classes = file.read().split("\n")

        self.net = cv2.dnn.readNetFromDarknet(str(configuration), str(weights))
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    def detect(self, image):
        blob = cv2.dnn.blobFromImage(image, 1 / 255, (self.image_width, self.image_height), [0, 0, 0], 1, crop=False)
        self.net.setInput(blob)

        outs = self.net.forward(self._get_output_layers_names())

        self._postprocess(image, outs)

        time, _ = self.net.getPerfProfile()
        return image

    def _get_output_layers_names(self):
        layers_names = self.net.getLayerNames()
        return [layers_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

    def _postprocess(self, image, outs):
        image_height = image.shape[0]
        image_width = image.shape[1]

        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = float(scores[class_id])
                if confidence > self.conf_threshold:
                    center_x = int(detection[0] * image_width)
                    center_y = int(detection[1] * image_height)

                    width = int(detection[2] * image_width)
                    height = int(detection[3] * image_height)

                    left = int(center_x - width / 2)
                    top = int(center_y - height / 2)

                    class_ids.append(class_id)
                    confidences.append(confidence)
                    boxes.append([left, top, width, height])

        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.conf_threshold, self.nms_threshold)
        for i in indices:
            i = i[0]
            box = boxes[i]
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]
            self._draw_prediction(image, class_ids[i], confidences[i], left, top, left + width, top + height)

    def _draw_prediction(self, image, class_id, confidence, left, top, right, bottom):
        indigo_bgr = (126, 35, 26)
        white_bgr = (0, 0, 0)

        cv2.rectangle(image, (left, top), (right, bottom), indigo_bgr, cv2.LINE_4)

        label = f"{self.classes[class_id]}: {confidence:.2f}"

        label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
        top = max(top, label_size[1])
        cv2.rectangle(
            image,
            (left, top - round(1.5 * label_size[1])),
            (left + round(1.5 * label_size[0]), top + base_line),
            (255, 255, 255),
            cv2.FILLED,
        )
        cv2.putText(image, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.75, white_bgr, 2)

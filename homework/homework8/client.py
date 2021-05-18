import PySimpleGUI as sg
import cv2
import numpy as np
import requests

URL = "http://localhost:5000/"


def main():
    sg.theme("Material1")

    layout = [
        [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="--IN--", file_types=(("png", "*.png"),))],
        [sg.Text("So far, only png files are supported", text_color="gray")],
        [sg.Button("Submit"), sg.Text("To close the image press ESC", text_color="red")],
    ]

    window = sg.Window("Object Detection", layout, resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Submit":
            path = values["--IN--"]

            original_image = cv2.imread(path)
            if original_image is None:
                sg.popup("No such file or directory")
                continue

            _, original_image_encoded = cv2.imencode(".png", original_image)
            response = requests.post(URL, data=original_image_encoded.tobytes(), headers={"content-type": "image/png"})

            modified_image_encoded = np.frombuffer(response.content, np.uint8)
            modified_image = cv2.imdecode(modified_image_encoded, cv2.IMREAD_COLOR)

            show_images(window, original_image, modified_image)


def show_images(window, original_image, modified_image):
    window.hide()

    cv2.namedWindow("image", cv2.WINDOW_GUI_NORMAL)

    height, width = original_image.shape[:2]
    if 1.7 * height >= width:
        image_to_show = np.concatenate([original_image, modified_image], axis=1)
    else:
        image_to_show = np.concatenate([original_image, modified_image])

    cv2.imshow("image", image_to_show)
    cv2.waitKeyEx(0)
    cv2.destroyAllWindows()

    window.un_hide()


if __name__ == "__main__":
    main()

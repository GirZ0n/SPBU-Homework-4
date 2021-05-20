# FAQ

**Q: Run fails on: `cv2.error: Transpose the weights (except for convolutional) is not implemented in function 'ReadDarknetFromWeightsStream'`?**

**A:** Try redownloading the repository. If the problem persists, download the file `yolov3.weights` from this [link](https://pjreddie.com/media/files/yolov3.weights) to the [resources/](resources/) folder

**Q: Why after closing the image, the program continues to work, but without the interface?**

**A:** Because of the GUI provided by OpenCV, the window with the image must always be closed with the `ESC` key. Forcibly stop the process and don't make similar mistakes again.

# Real-Time Face Detection using YOLOv8 and OpenCV

This project provides a lightweight and real-time solution for detecting faces from a webcam feed using the YOLOv8 object detection model and OpenCV.

The goal is to help you easily detect multiple faces, show a live count, and save frames—all using Python.

---

## Features

- Real-time face detection from your laptop/PC webcam
- Face count displayed on the screen
- Press `s` to save a screenshot of the current frame
- Press `q` to exit the program safely
- Easy-to-modify Python code for adding your own enhancements

---

## Requirements

Before getting started, make sure you have **Python 3.8 or later** installed on your system.

To install all the required libraries, simply open your terminal and run:

```bash
pip install -r requirements.txt
```

This command installs the following:

- `ultralytics` – Powers YOLOv8 for face detection
- `opencv-python` – Used to capture video from your webcam and display results
- `numpy` – Helps with numerical operations and array handling

---

## Acknowledgements

This project uses the YOLOv8 face detection model provided by [@arnabdhar](https://huggingface.co/arnabdhar) on Hugging Face:

🔗 [YOLOv8-Face-Detection Model on Hugging Face](https://huggingface.co/arnabdhar/YOLOv8-Face-Detection)

The model is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**. Please refer to the [original repository](https://huggingface.co/arnabdhar/YOLOv8-Face-Detection) for more information.

See the [LICENSE](LICENSE) file for more details.

---

If you're working inside a virtual environment (which is a good practice), make sure to activate it before running the install command.

That's it — you're ready to run the app!


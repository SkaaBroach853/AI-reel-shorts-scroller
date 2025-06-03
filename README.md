# AI-reel/shorts-scroller
🎮 Control YouTube Shorts or Insta Reels using AI-powered hand and face gestures with MediaPipe and OpenCV. Just move your thumb, index finger, or open your mouth — no mouse or keyboard needed!


# 🎮 Reel Shorts Controller

Control YouTube Shorts using just your face and fingers!  
- **Thumb Down** → Next short  
- **Index Finger Down** → Previous short  
- **Mouth Open** → Next short(Optional, Just for fun)

---

## 🔧 Setup Instructions (Beginner Friendly)

### 🖥 Requirements
- Windows 10
- A webcam
- Python 3.7+
- A little patience 

---

### 1. Clone or Download This Folder

If you're reading this on GitHub or shared folder, just download it and unzip.

---

### 2. Open Command Prompt (CMD)

Go to the folder using:

```bash
cd path\to\ReelShortsController
```

---

### 3. Create and Activate Virtual Environment (You may have done this)

```bash
python -m venv venv
```

Then activate it:

```bash
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your command line.

---

### 4. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 5. Run the Code

```bash
python Reel-Shorts_Controller.py
```

Press `q` to quit the webcam window anytime.

---

## 👆 How It Works

- It uses your **webcam** to detect:
  - Face (using MediaPipe Face Mesh)
  - Hands (using MediaPipe Hands)
- Actions are triggered using:
  - **Thumb moves down** → `↓` key (next)
  - **Index finger moves down** → `↑` key (previous)
  - **Mouth opens** → `↓` key (next)

So you can scroll Shorts with just simple gestures—no mouse or keyboard needed!

---

## 💡 Troubleshooting

- Make sure your **webcam** works and isn’t being used by another app.
- If `cv2` gives an error, make sure OpenCV is installed:
  ```bash
  pip install opencv-python
  ```
- For pyautogui to control keys, allow screen access on some systems.

---

### 💡 Pros of keeping mouth control for upward movement:
- Gives your hands a break, sharing the load with mouth gestures.
- Can make scrolling more fun and interactive.
- Adds an extra layer of control, so you’re not stuck with just fingers.

---

## 📞 Contact

Made with ❤️ by a beginner for beginners by AD. Feel free to contribute!

---
## DEMO IMAGES
![b159eea1-957b-4d6e-8357-f5062e744745](https://github.com/user-attachments/assets/b431c9e0-a9ad-421e-ad21-070b4f817860)

---
![646eb77f-4481-4b1c-ad46-7654ea0fa201](https://github.com/user-attachments/assets/6694e340-e634-4833-9471-4f139bf42ad7)

---
![da3f59b5-8090-41f1-b060-5be0720a9831](https://github.com/user-attachments/assets/a5fd4fd4-cdd6-49cb-b1fd-4ebcfc3192d3)

---
![a2efd684-7272-452b-a4c9-71b939b39213](https://github.com/user-attachments/assets/9611fda1-58df-4973-a400-5a66cc42f963)

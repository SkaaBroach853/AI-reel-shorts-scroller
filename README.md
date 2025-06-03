# AI-reel-shorts-scroller
🎮 Control YouTube Shorts or Insta Reels using AI-powered hand and face gestures with MediaPipe and OpenCV. Just move your thumb, index finger, or open your mouth — no mouse or keyboard needed!


# 🎮 Reel Shorts Controller

Control YouTube Shorts using just your face and fingers!  
- **Thumb Down** → Next short  
- **Index Finger Down** → Previous short  
- **Mouth Open** → Next short


## 🔧 Setup Instructions (Beginner Friendly)

### 🖥 Requirements
- Windows 10
- A webcam
- Python 3.7+
- A little patience 


### 1. Clone or Download This Folder

If you're reading this on GitHub or shared folder, just download it and unzip.


### 2. Open Command Prompt (CMD)

Go to the folder using:

```bash
cd path\to\ReelShortsController
```


### 3. Create and Activate Virtual Environment (You may have done this)

```bash
python -m venv venv
```

Then activate it:

```bash
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your command line.


### 4. Install Required Libraries

```bash
pip install -r requirements.txt
```



### 5. Run the Code

```bash
python Reel-Shorts_Controller.py
```

Press `q` to quit the webcam window anytime.


## 👆 How It Works

- It uses your **webcam** to detect:
  - Face (using MediaPipe Face Mesh)
  - Hands (using MediaPipe Hands)
- Actions are triggered using:
  - **Thumb moves down** → `↓` key (next)
  - **Index finger moves down** → `↑` key (previous)
  - **Mouth opens** → `↓` key (next)

So you can scroll Shorts with just simple gestures—no mouse or keyboard needed!


## 💡 Troubleshooting

- Make sure your **webcam** works and isn’t being used by another app.
- If `cv2` gives an error, make sure OpenCV is installed:
  ```bash
  pip install opencv-python
  ```
- For pyautogui to control keys, allow screen access on some systems.


## 📞 Contact

Made with ❤️ by a beginner for beginners. Feel free to contribute!

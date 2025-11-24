# Windows Build and Test Guide

## Quick Start for Windows Testing

### Prerequisites
1. **Windows 10/11** (64-bit)
2. **Python 3.8 or higher** - Download from [python.org](https://www.python.org/downloads/)
3. **Git** (optional) - Download from [git-scm.com](https://git-scm.com/)
4. **Webcam** - Built-in or USB camera

### Step 1: Download the Repository

**Option A: Download ZIP (No Git Required)**
```
1. Go to https://github.com/tysoncung/reactions-app
2. Click green "Code" button
3. Click "Download ZIP"
4. Extract to a folder (e.g., C:\reactions-app)
```

**Option B: Clone with Git**
```powershell
git clone https://github.com/tysoncung/reactions-app.git
cd reactions-app
```

### Step 2: Install Dependencies

Open PowerShell or Command Prompt in the project folder:

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

**Note**: If you get errors installing mediapipe or opencv, try:
```powershell
pip install mediapipe --no-deps
pip install opencv-python
pip install -r requirements.txt
```

### Step 3: Install Virtual Camera Driver

The app needs a virtual camera driver to work with Zoom/Teams/etc.

**Option A: Use OBS Virtual Camera (Recommended)**
1. Download OBS Studio: https://obsproject.com/download
2. Install OBS
3. The virtual camera driver will be installed automatically

**Option B: Install pyvirtualcam backend**
```powershell
pip install pyvirtualcam
```

If using pyvirtualcam, you'll need **OBS Virtual Camera** or **Unity Capture** installed.

### Step 4: Test the Application

```powershell
# Make sure virtual environment is activated
venv\Scripts\activate

# Run the application
python src/main.py
```

**What should happen:**
1. A window opens showing your webcam feed
2. You see checkboxes for different gestures
3. Try making a thumbs up gesture - you should see effects appear!

### Step 5: Use with Video Conferencing Apps

1. **Keep the Camera Reactions app running**
2. **Open your video conferencing app** (Zoom, Teams, Meet, Discord)
3. **Go to video settings**:
   - **Zoom**: Settings → Video → Camera → Select "Camera Reactions Virtual Camera"
   - **Teams**: Settings → Devices → Camera → Select "Camera Reactions Virtual Camera"
   - **Google Meet**: Settings → Video → Camera → Select "Camera Reactions Virtual Camera"
   - **Discord**: User Settings → Voice & Video → Camera → Select "Camera Reactions Virtual Camera"

4. **Start a call and perform gestures!**

## Troubleshooting

### Issue: "No module named 'mediapipe'"
**Solution**:
```powershell
pip install mediapipe==0.10.8
```

### Issue: "Virtual camera not found in Zoom/Teams"
**Solutions**:
1. Make sure Camera Reactions app is running
2. Restart your video conferencing app
3. Install OBS Studio first (includes virtual camera driver)
4. Check Windows Device Manager → Cameras to see if virtual camera appears

### Issue: "Could not open camera"
**Solutions**:
1. Close other apps using your webcam
2. Try changing camera in settings dropdown
3. Check Windows Privacy Settings → Camera permissions

### Issue: Gestures not detected
**Solutions**:
1. Improve lighting - ensure your hands are well-lit
2. Lower confidence threshold in settings
3. Hold gesture for 1-2 seconds
4. Keep hands 1-2 feet from camera

### Issue: Low frame rate / laggy
**Solutions**:
1. Close other apps
2. Lower resolution in config (edit config.json)
3. Disable some gestures you don't use
4. Enable GPU acceleration (if you have NVIDIA GPU):
   ```powershell
   pip install onnxruntime-gpu
   ```

## Building Standalone Executable

To create a standalone .exe file that doesn't require Python:

```powershell
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --name CameraReactions ^
    --windowed ^
    --onefile ^
    --add-data "assets;assets" ^
    --hidden-import=mediapipe ^
    --hidden-import=cv2 ^
    src/main.py

# Find executable in: dist/CameraReactions.exe
```

**Run the executable**:
```
dist\CameraReactions.exe
```

## Advanced: Create Installer

```powershell
# Install Inno Setup from: https://jrsoftware.org/isdl.php

# Then run:
python scripts/build_installer.py
```

## Configuration

Edit `config.json` to customize:
- Camera resolution (default 1280x720)
- FPS (default 30)
- Gesture confidence threshold (default 0.8)
- Effect duration (default 3.0 seconds)
- Enable/disable specific gestures

Example `config.json`:
```json
{
    "camera_width": 1280,
    "camera_height": 720,
    "camera_fps": 30,
    "gesture_confidence": 0.8,
    "effect_duration": 3.0,
    "enabled_gestures": {
        "thumbs_up": true,
        "thumbs_down": true,
        "two_thumbs_up": true,
        "peace_sign": true,
        "heart_hands": true,
        "raised_fist": true
    }
}
```

## Performance Tips

1. **Close background apps** to free up CPU/GPU
2. **Good lighting** helps gesture detection accuracy
3. **Solid background** reduces false positives
4. **Lower resolution** if experiencing lag:
   ```json
   "camera_width": 640,
   "camera_height": 480
   ```
5. **Disable unused gestures** to save processing power

## Testing Gestures

### Thumbs Up 👍
- Extend thumb upward
- Keep other fingers folded
- Hold for 1-2 seconds

### Thumbs Down 👎
- Extend thumb downward
- Keep other fingers folded

### Peace Sign ✌️
- Extend index and middle fingers
- Keep other fingers folded

### Two Thumbs Up 👍👍
- Both hands showing thumbs up
- Hold both hands visible to camera

### Heart Hands 💗
- Form heart shape with both hands
- Thumbs should be close together at the top

### Raised Fist ✊
- Close all fingers into fist
- Raise fist up

## Getting Help

- **Documentation**: Check `docs/` folder
- **Issues**: https://github.com/tysoncung/reactions-app/issues
- **README**: Main README.md has more details

## Uninstall

```powershell
# Just delete the folder
cd ..
rmdir /s reactions-app

# Or if you want to keep the code but remove Python packages:
cd reactions-app
venv\Scripts\activate
pip uninstall -r requirements.txt -y
```

---

**Ready to test!** Start with Step 1 above and follow through each step. Good luck! 🎉

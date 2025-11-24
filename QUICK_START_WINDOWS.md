# 🚀 Quick Start - Windows (5 Minutes)

## The Fastest Way to Test Camera Reactions

### Step 1: Download
1. Go to: **https://github.com/tysoncung/reactions-app**
2. Click green **"Code"** button → **"Download ZIP"**
3. Extract to Desktop or Documents folder

### Step 2: Install Python (if not installed)
1. Go to: **https://www.python.org/downloads/**
2. Download Python 3.10 or newer
3. Run installer, **check "Add to PATH"**
4. Click "Install Now"

### Step 3: Open PowerShell
1. Press **Windows + X**
2. Select **"Windows PowerShell"** or **"Terminal"**
3. Navigate to extracted folder:
   ```powershell
   cd Desktop\reactions-app-main
   ```
   (Or wherever you extracted it)

### Step 4: Run Setup Script

Copy and paste this into PowerShell:

```powershell
python -m venv venv
venv\Scripts\activate
pip install mediapipe opencv-python numpy pillow pyvirtualcam PyQt5 pyyaml
```

Wait for installation (2-3 minutes)...

### Step 5: Run the App

```powershell
python src/main.py
```

**You should see:**
- A window with your webcam feed
- Gesture checkboxes on the right
- Try making a thumbs up! 👍

### Step 6: Use in Zoom/Teams

1. **Keep Camera Reactions running**
2. Open Zoom/Teams
3. Go to Settings → Video → Camera
4. Select **"Camera Reactions Virtual Camera"**
5. Start a call and perform gestures!

---

## Not Working? Quick Fixes

### "Python is not recognized"
- Reinstall Python, check "Add to PATH" box
- Or download from Microsoft Store: `python3`

### "No virtual camera in Zoom"
- Install OBS Studio first: https://obsproject.com/download
- Restart Zoom after installing OBS

### "Camera not found"
- Close other apps using webcam
- Try Camera app to test webcam works

### Still stuck?
Open an issue: https://github.com/tysoncung/reactions-app/issues

---

That's it! You should be up and running in under 5 minutes. 🎉

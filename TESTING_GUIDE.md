# Testing Guide - Camera Reactions

## Quick Test (5 Minutes)

### Prerequisites
- Windows 10/11 (64-bit)
- Python 3.8+ installed ([download](https://www.python.org/downloads/))
- Webcam (built-in or USB)
- OBS Studio for virtual camera ([download](https://obsproject.com/download))

### Step 1: Download Source Code

**Option A: Git**
```powershell
git clone https://github.com/tysoncung/reactions-app.git
cd reactions-app
```

**Option B: ZIP Download**
1. Go to https://github.com/tysoncung/reactions-app
2. Click green "Code" button → "Download ZIP"
3. Extract to Desktop
4. Open PowerShell in extracted folder

### Step 2: Setup Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies (takes 2-3 minutes)
pip install -r requirements.txt
```

### Step 3: Install Virtual Camera Driver

1. Download OBS Studio: https://obsproject.com/download
2. Install with default settings
3. You can close OBS after installation (we just need the driver)

### Step 4: Run the Application

```powershell
python src/main.py
```

**You should see:**
- A window with your webcam feed
- Gesture checkboxes on the right side
- Camera controls at the top

---

## Testing Checklist

### 1. Basic Functionality
- [ ] Application launches without errors
- [ ] Webcam video feed displays correctly
- [ ] Window is responsive and can be resized
- [ ] UI controls are accessible

### 2. Gesture Recognition

Test each gesture (hold for 1-2 seconds):

**👍 Thumbs Up**
- [ ] Extend thumb upward, keep other fingers folded
- [ ] Hearts animation should appear
- [ ] Check "Thumbs Up Detected" indicator

**👎 Thumbs Down**
- [ ] Extend thumb downward, keep other fingers folded
- [ ] Thumbs down icon should appear
- [ ] Check detection indicator

**✌️ Peace Sign**
- [ ] Extend index and middle fingers (V shape)
- [ ] Keep other fingers folded
- [ ] Confetti animation should trigger

**👍👍 Two Thumbs Up**
- [ ] Show both hands with thumbs up
- [ ] Keep both hands visible to camera
- [ ] Celebration effect should appear

**💗 Heart Hands**
- [ ] Form heart shape with both hands
- [ ] Thumbs touch at top, fingers curve to form heart
- [ ] Floating hearts animation triggers

**✊ Raised Fist**
- [ ] Close all fingers into fist
- [ ] Raise fist in front of camera
- [ ] Power/fist effect appears

### 3. UI Controls

- [ ] Enable/disable individual gestures using checkboxes
- [ ] Disabled gestures don't trigger effects
- [ ] Camera selection dropdown works (if multiple cameras)
- [ ] Start/Stop button works correctly

### 4. Performance

- [ ] Frame rate is smooth (check FPS counter if visible)
- [ ] No significant lag when performing gestures
- [ ] CPU usage is reasonable (check Task Manager)
- [ ] Memory usage is stable

### 5. Virtual Camera Integration

**Test with Zoom:**
1. [ ] Keep Camera Reactions app running
2. [ ] Open Zoom
3. [ ] Go to Settings → Video
4. [ ] "Camera Reactions Virtual Camera" appears in camera list
5. [ ] Select virtual camera
6. [ ] Video feed shows correctly
7. [ ] Perform gesture - effect appears in Zoom preview
8. [ ] Start test meeting to verify remote participants see effects

**Test with Microsoft Teams:**
1. [ ] Open Teams
2. [ ] Go to Settings → Devices → Camera
3. [ ] Select "Camera Reactions Virtual Camera"
4. [ ] Effects work in Teams call

**Test with Google Meet:**
1. [ ] Open Google Meet in browser
2. [ ] Go to Settings → Video
3. [ ] Select "Camera Reactions Virtual Camera"
4. [ ] Effects work in Meet call

---

## Common Issues and Solutions

### Issue: "Python is not recognized"
**Solution:**
- Reinstall Python from https://www.python.org/downloads/
- During installation, check "Add Python to PATH"
- Restart PowerShell after installation

### Issue: "No module named 'mediapipe'"
**Solution:**
```powershell
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: "Could not open camera"
**Solution:**
- Close other apps using webcam (Zoom, Teams, Skype)
- Check Windows Privacy Settings → Camera permissions
- Try Windows Camera app to verify webcam works
- Restart computer if issue persists

### Issue: "Virtual camera not found in Zoom/Teams"
**Solution:**
- Install OBS Studio (includes virtual camera driver)
- Restart Camera Reactions app
- Restart Zoom/Teams
- Check if "OBS Virtual Camera" appears (alternative name)

### Issue: Gestures not detected
**Solution:**
- Improve lighting - ensure hands are well-lit
- Hold gesture steady for 1-2 seconds
- Keep hands 1-2 feet from camera
- Make gesture clear and distinct
- Lower confidence threshold in settings (if available)

### Issue: Low frame rate / laggy
**Solution:**
- Close other CPU-intensive applications
- Lower resolution in config.json:
  ```json
  {
    "camera_width": 640,
    "camera_height": 480
  }
  ```
- Disable unused gestures
- Check Task Manager for high CPU usage

### Issue: Effects don't appear
**Solution:**
- Verify gesture is enabled (checkbox checked)
- Hold gesture longer (1-2 seconds minimum)
- Check console for error messages
- Ensure you're using correct hand position

---

## Advanced Testing

### Test Configuration Changes

1. **Edit `config.json`** (create if doesn't exist):
```json
{
  "camera_width": 1280,
  "camera_height": 720,
  "camera_fps": 30,
  "gesture_confidence": 0.7,
  "effect_duration": 5.0,
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

2. **Test different confidence thresholds:**
   - Lower (0.6-0.7): More sensitive, may have false positives
   - Higher (0.85-0.95): Less sensitive, more accurate

3. **Test different resolutions:**
   - 640x480: Low resource usage
   - 1280x720: Balanced (recommended)
   - 1920x1080: High quality, more CPU usage

### Performance Profiling

Monitor these metrics during testing:
- **CPU Usage**: Should be under 50% on modern hardware
- **Memory Usage**: Should stabilize around 200-400 MB
- **Frame Rate**: Should maintain 25-30 FPS
- **Latency**: Gesture detection within 0.5-1 second

---

## Reporting Issues

If you encounter problems, please report with:

1. **System Information:**
   - Windows version
   - Python version (`python --version`)
   - CPU and RAM specs

2. **Error Messages:**
   - Console output
   - Screenshots if applicable

3. **Steps to Reproduce:**
   - What you did
   - What you expected
   - What actually happened

**Report issues at:** https://github.com/tysoncung/reactions-app/issues

---

## Next Steps After Testing

Once testing is complete, you can:
1. **Use in production** for video calls
2. **Customize effects** by modifying effect files
3. **Add new gestures** by extending gesture detector
4. **Contribute improvements** via pull requests
5. **Share feedback** via GitHub issues

---

**Happy Testing!** 🎉

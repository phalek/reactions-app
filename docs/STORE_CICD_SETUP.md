# Microsoft Store CI/CD Setup Guide

This guide explains how to automate Microsoft Store publishing using GitHub Actions.

## Overview

The CI/CD pipeline will:
1. ✅ Build MSIX package automatically on tag push
2. ✅ Sign the package for testing
3. ✅ Upload to GitHub Releases
4. ✅ Submit to Microsoft Store Partner Center (optional)

---

## Prerequisites

- [x] Microsoft Developer Account (already registered)
- [ ] Azure Active Directory (AD) App registration
- [ ] Microsoft Store app created in Partner Center
- [ ] GitHub repository with workflows enabled

---

## Part 1: Azure AD App Setup (15 minutes)

### Step 1: Create Azure AD Application

1. **Go to Azure Portal:**
   ```
   https://portal.azure.com
   ```

2. **Navigate to Azure Active Directory:**
   - Search for "Azure Active Directory" in the top search bar
   - Click on "Azure Active Directory"

3. **Register New Application:**
   - Click "App registrations" in left sidebar
   - Click "+ New registration"

   **Fill in details:**
   - Name: `CameraReactions-GitHub-Actions`
   - Supported account types: **Accounts in this organizational directory only**
   - Redirect URI: Leave blank
   - Click "Register"

4. **Save Application (client) ID:**
   ```
   Application (client) ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   ```
   ⚠️ **Save this - you'll need it later as `AZURE_CLIENT_ID`**

5. **Save Directory (tenant) ID:**
   ```
   Directory (tenant) ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   ```
   ⚠️ **Save this - you'll need it later as `AZURE_TENANT_ID`**

### Step 2: Create Client Secret

1. **Go to Certificates & secrets:**
   - In your app registration, click "Certificates & secrets" in left sidebar
   - Click "+ New client secret"

2. **Add secret:**
   - Description: `GitHub Actions Secret`
   - Expires: **24 months** (recommended)
   - Click "Add"

3. **Copy the secret VALUE:**
   ```
   Value: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
   ⚠️ **IMPORTANT: Copy this NOW - you can't see it again!**
   ⚠️ **Save this as `AZURE_CLIENT_SECRET`**

### Step 3: Grant API Permissions

1. **Add API permissions:**
   - Click "API permissions" in left sidebar
   - Click "+ Add a permission"
   - Click "APIs my organization uses"
   - Search for: `Windows Store`
   - Select "Windows Store"

2. **Select permissions:**
   - Check: `user_impersonation`
   - Click "Add permissions"

3. **Grant admin consent:**
   - Click "Grant admin consent for [Your Organization]"
   - Click "Yes" to confirm

---

## Part 2: Partner Center Configuration (10 minutes)

### Step 1: Get Your App ID

1. **Go to Partner Center:**
   ```
   https://partner.microsoft.com/dashboard
   ```

2. **Create or select your app:**
   - If new: Click "Create a new app" → Reserve name "Camera Reactions"
   - If existing: Click on your app

3. **Get App ID:**
   - Go to "Product identity" section
   - Copy the **Store ID** or **App ID**
   ```
   Store ID: 9NXXXXXXXXXXXXXX
   ```
   ⚠️ **Save this as `STORE_APP_ID`**

### Step 2: Associate Azure AD App

1. **In Partner Center:**
   - Go to "Account settings" → "User management"
   - Click "Azure AD applications"
   - Click "Add Azure AD applications"

2. **Add your app:**
   - Enter the **Application (client) ID** from Azure AD
   - Assign role: **Manager** (required for submissions)
   - Click "Save"

---

## Part 3: GitHub Secrets Setup (5 minutes)

### Step 1: Add Secrets to GitHub

1. **Go to your GitHub repository:**
   ```
   https://github.com/YOUR_USERNAME/reactions-app
   ```

2. **Navigate to Settings:**
   - Click "Settings" tab
   - Click "Secrets and variables" → "Actions"
   - Click "New repository secret"

3. **Add these 4 secrets:**

   **Secret 1: AZURE_TENANT_ID**
   - Name: `AZURE_TENANT_ID`
   - Value: `[Your Directory (tenant) ID from Azure AD]`
   - Click "Add secret"

   **Secret 2: AZURE_CLIENT_ID**
   - Name: `AZURE_CLIENT_ID`
   - Value: `[Your Application (client) ID from Azure AD]`
   - Click "Add secret"

   **Secret 3: AZURE_CLIENT_SECRET**
   - Name: `AZURE_CLIENT_SECRET`
   - Value: `[Your client secret VALUE from Azure AD]`
   - Click "Add secret"

   **Secret 4: STORE_APP_ID**
   - Name: `STORE_APP_ID`
   - Value: `[Your Store ID from Partner Center]`
   - Click "Add secret"

### Step 2: Verify Secrets

You should now have 4 secrets:
```
✓ AZURE_TENANT_ID
✓ AZURE_CLIENT_ID
✓ AZURE_CLIENT_SECRET
✓ STORE_APP_ID
```

---

## Part 4: Update Workflow Configuration (5 minutes)

### Step 1: Edit Publisher Name

Edit `.github/workflows/store-publish.yml`:

```yaml
env:
  PUBLISHER_NAME: 'CN=YourPublisherName'  # ← Change this
```

**To find your publisher name:**

1. Go to Partner Center → Account Settings → Organization profile
2. Copy the **Publisher ID** (looks like: `CN=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`)
3. Paste it in the workflow file

### Step 2: Update Display Name

In the same file, find and update:

```yaml
<PublisherDisplayName>Your Display Name</PublisherDisplayName>
```

Change to your actual display name (the one you registered with).

---

## Part 5: Create App Assets (30 minutes)

The workflow needs these image files. Create them and add to your repo:

### Required Assets

Create `assets/store/` directory with these images:

**1. Square44x44Logo.png** (44x44 pixels)
- App list icon
- Transparent background
- PNG format

**2. Square150x150Logo.png** (150x150 pixels)
- Medium tile
- Transparent background
- PNG format

**3. Wide310x150Logo.png** (310x150 pixels)
- Wide tile
- Transparent background
- PNG format

**4. StoreLogo.png** (50x50 pixels)
- Store listing icon
- Transparent background
- PNG format

**5. SplashScreen.png** (620x300 pixels)
- App splash screen
- Can have background color
- PNG format

### Quick Asset Creation

**Option 1: Use Figma (Free)**
1. Go to https://figma.com
2. Create a new file
3. Use the Rectangle tool to create each size
4. Add your logo/icon
5. Export as PNG

**Option 2: Use Canva (Free)**
1. Go to https://canva.com
2. Custom size for each dimension
3. Design your logo
4. Download as PNG

**Option 3: Hire on Fiverr**
- Search "app icon design"
- Provide the 5 sizes needed
- Cost: $5-20

### Add Assets to Repo

```bash
mkdir -p assets/store
# Add your PNG files to assets/store/
git add assets/store/
git commit -m "Add Microsoft Store assets"
git push
```

Update the workflow to copy from your assets folder:

```yaml
# In .github/workflows/store-publish.yml
# Replace the "Create placeholder assets" step with:
- name: Copy real assets
  run: |
    Copy-Item "assets\store\*" -Destination "msix\Assets\" -Force
  shell: pwsh
```

---

## Part 6: First Workflow Run (5 minutes)

### Method 1: Tag-Based Trigger (Recommended)

```bash
# Create and push a tag
git tag -a store-v1.0.0 -m "Microsoft Store release v1.0.0"
git push origin store-v1.0.0
```

The workflow will:
1. Build the MSIX package
2. Sign it with a test certificate
3. Upload to GitHub Releases
4. Prepare for Store submission

### Method 2: Manual Trigger

1. Go to GitHub → Actions tab
2. Click "Publish to Microsoft Store" workflow
3. Click "Run workflow"
4. Enter version: `1.0.0.0`
5. Click "Run workflow"

---

## Part 7: Download and Test MSIX (10 minutes)

### Step 1: Download Built Package

1. **Go to GitHub Actions:**
   - Navigate to your workflow run
   - Click on the completed run
   - Scroll to "Artifacts"
   - Download "msix-package"

2. **Extract the ZIP:**
   - Extract to a folder
   - You'll see: `CameraReactions_1.0.0.0_x64.msix`

### Step 2: Install Test Certificate

```powershell
# Open PowerShell as Administrator

# Import the test certificate (from workflow output)
# The workflow creates TestCert.pfx - you'll need to export it or use your own

# For now, use a self-signed cert for testing:
$cert = New-SelfSignedCertificate -Type Custom -Subject "CN=YourPublisherName" -KeyUsage DigitalSignature -FriendlyName "Test Cert" -CertStoreLocation "Cert:\CurrentUser\My" -TextExtension @("2.5.29.37={text}1.3.6.1.5.5.7.3.3", "2.5.29.19={text}")

# Export to Trusted Root
$cert | Export-Certificate -FilePath "TestCert.cer"
Import-Certificate -FilePath "TestCert.cer" -CertStoreLocation "Cert:\LocalMachine\Root"
```

### Step 3: Install MSIX Package

```powershell
# Enable Developer Mode first
# Settings → Update & Security → For developers → Developer mode

# Install the MSIX
Add-AppxPackage -Path "CameraReactions_1.0.0.0_x64.msix"

# Launch the app
# It will appear in your Start Menu
```

### Step 4: Test the App

- Launch from Start Menu
- Verify camera permissions prompt
- Test gesture detection
- Verify all features work

---

## Part 8: Submit to Microsoft Store (Manual)

⚠️ **Note:** The automated submission is commented out in the workflow. For first submission, do it manually:

### Step 1: Prepare Submission Package

The workflow creates an MSIX that's ready for submission. Download it from GitHub Actions artifacts.

### Step 2: Submit in Partner Center

1. **Go to Partner Center:**
   ```
   https://partner.microsoft.com/dashboard/apps/overview
   ```

2. **Select your app** → Click "Start your submission"

3. **Fill out each section:**

   **Pricing and availability:**
   - Base price: Free
   - Markets: All markets
   - Discoverability: Public

   **Properties:**
   - Category: Productivity
   - Privacy policy URL: `https://your-github-username.github.io/reactions-app/privacy`
   - Support contact: your-email@example.com

   **Age ratings:**
   - Complete IARC questionnaire
   - Should be rated: Everyone

   **Packages:**
   - Upload the MSIX file downloaded from GitHub Actions
   - Upload will validate automatically

   **Store listings:**
   - Description: (Use template from MICROSOFT_STORE_GUIDE.md)
   - Screenshots: Upload at least 1 screenshot
   - App tile icon: Upload 300x300 PNG
   - Keywords: video effects, webcam, zoom, teams, reactions

4. **Submit for certification:**
   - Review all sections
   - Click "Submit to the Store"
   - Wait 24-48 hours for review

---

## Part 9: Automate Future Submissions (Optional)

### Enable Automatic Submission

Once your first submission is approved, you can enable automatic submissions:

1. **Edit the workflow:**

In `.github/workflows/store-publish.yml`, uncomment this line:

```yaml
# Update-ApplicationSubmission @submissionParams
```

Change to:

```yaml
Update-ApplicationSubmission @submissionParams
```

2. **Create submission config:**

Create `store-submission.json`:

```json
{
  "applicationCategory": "Productivity",
  "listings": {
    "en-us": {
      "description": "Add fun animated reactions to your video calls...",
      "releaseNotes": "Initial release",
      "screenshots": [],
      "title": "Camera Reactions"
    }
  },
  "pricing": {
    "priceId": "Free"
  },
  "allowTargetFutureDeviceFamilies": {
    "Desktop": true
  }
}
```

3. **Test with dry run:**

```bash
# Push a test tag
git tag store-v1.0.1
git push origin store-v1.0.1
```

The workflow will build, package, and submit automatically!

---

## Workflow Triggers

### Trigger on Tag

```bash
# Semantic versioning
git tag -a store-v1.0.0 -m "Store release 1.0.0"
git push origin store-v1.0.0

# The workflow runs automatically
```

### Manual Trigger

1. GitHub → Actions → "Publish to Microsoft Store"
2. Run workflow → Enter version → Run

### Scheduled Releases

Add to workflow:

```yaml
on:
  schedule:
    - cron: '0 0 * * 0'  # Every Sunday at midnight
```

---

## Versioning Strategy

### Version Format

Microsoft Store requires format: `Major.Minor.Build.Revision`

Examples:
- `1.0.0.0` - Initial release
- `1.0.1.0` - Bug fix
- `1.1.0.0` - Minor feature update
- `2.0.0.0` - Major version

### Auto-increment Version

Create `.github/workflows/bump-version.yml`:

```yaml
name: Bump Version

on:
  workflow_dispatch:
    inputs:
      bump:
        description: 'Version bump type'
        required: true
        type: choice
        options:
          - patch
          - minor
          - major

jobs:
  bump:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Bump version
        run: |
          # Read current version
          current=$(git describe --tags --abbrev=0 | sed 's/store-v//')

          # Bump version based on input
          # ... version bumping logic ...

          # Create new tag
          git tag -a "store-v$new_version" -m "Release $new_version"
          git push origin "store-v$new_version"
```

---

## Troubleshooting

### Issue: "Publisher name doesn't match"

**Solution:**
- Check your Partner Center publisher ID
- Update `PUBLISHER_NAME` in workflow
- Must match exactly (case-sensitive)

### Issue: "Invalid MSIX package"

**Solution:**
- Check AppxManifest.xml formatting
- Ensure version is in format X.X.X.X
- Verify all required assets exist
- Run: `MakeAppx.exe validate /p package.msix`

### Issue: "Authentication failed"

**Solution:**
- Verify all 4 secrets are set correctly
- Check Azure AD app has correct permissions
- Ensure admin consent was granted
- Verify app is associated in Partner Center

### Issue: "Submission failed"

**Solution:**
- Check certification logs in Partner Center
- Verify privacy policy URL is accessible
- Ensure age rating is completed
- Check that all required fields are filled

### Issue: "Assets missing"

**Solution:**
- Create all 5 required PNG files
- Place in `assets/store/` directory
- Update workflow to copy from correct location
- Commit and push assets to repo

---

## Best Practices

### 1. Semantic Versioning

```
store-v1.0.0 → Initial release
store-v1.0.1 → Bug fixes
store-v1.1.0 → New features
store-v2.0.0 → Breaking changes
```

### 2. Release Notes

Include in tag message:

```bash
git tag -a store-v1.1.0 -m "Release 1.1.0

- Added new gesture: finger counting
- Improved detection accuracy
- Fixed camera selection bug
- Updated UI theme"

git push origin store-v1.1.0
```

### 3. Testing Before Submission

Always test locally:

```powershell
# Install locally first
Add-AppxPackage -Path "CameraReactions_1.1.0.0_x64.msix"

# Test all features

# Then submit to Store
```

### 4. Gradual Rollout

In Partner Center:
- Set gradual rollout to 10% first
- Monitor crash reports
- Increase to 50% if stable
- Full release after 7 days

---

## Monitoring

### GitHub Actions

- View workflow runs: Repository → Actions
- Check logs for each step
- Download artifacts for testing

### Partner Center Analytics

Monitor:
- Downloads
- Crashes
- Ratings & reviews
- Acquisition sources

---

## Cost Summary

| Item | Cost | Frequency |
|------|------|-----------|
| Microsoft Developer Account | $19 | One-time (already paid) |
| Azure AD (Free tier) | $0 | - |
| GitHub Actions (Public repo) | $0 | - |
| Asset creation (DIY) | $0 | - |
| Asset creation (Fiverr) | $5-20 | Optional |
| **Total** | **$0-20** | After initial $19 |

---

## Next Steps

1. ✅ Complete Azure AD setup (Part 1)
2. ✅ Configure Partner Center (Part 2)
3. ✅ Add GitHub secrets (Part 3)
4. ✅ Create app assets (Part 5)
5. ✅ Test workflow (Part 6)
6. ✅ Submit to Store (Part 8)

**Time estimate:** 2-3 hours for complete setup

After initial setup, future releases are fully automated:
```bash
git tag -a store-v1.1.0 -m "Release 1.1.0"
git push origin store-v1.1.0
# Done! Automatic build and submission
```

---

## Resources

**Microsoft Documentation:**
- Partner Center API: https://docs.microsoft.com/windows/uwp/monetize/create-and-manage-submissions-using-windows-store-services
- StoreBroker Module: https://github.com/microsoft/StoreBroker
- MSIX Packaging: https://docs.microsoft.com/windows/msix/

**Tools:**
- Azure Portal: https://portal.azure.com
- Partner Center: https://partner.microsoft.com/dashboard
- GitHub Actions Docs: https://docs.github.com/actions

Need help with any step? Let me know!

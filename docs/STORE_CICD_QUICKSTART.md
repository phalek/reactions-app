# Microsoft Store CI/CD - Quick Start

**Goal:** Automate Microsoft Store publishing from GitHub Actions

**Time:** 30-60 minutes setup | Automated afterward

---

## Prerequisites Checklist

- [x] Microsoft Developer Account registered ($19 paid)
- [ ] GitHub repository with workflow access
- [ ] 30-60 minutes free time

---

## Quick Setup (6 Steps)

### Step 1: Azure AD App (10 min)

1. Go to https://portal.azure.com
2. Azure Active Directory → App registrations → New registration
3. Name: `CameraReactions-GitHub-Actions`
4. Register → Save these 3 values:

```
✓ Application (client) ID: ___________________________________
✓ Directory (tenant) ID:   ___________________________________
```

5. Certificates & secrets → New client secret → Copy value:

```
✓ Client secret VALUE:     ___________________________________
```

⚠️ **Save these now - can't retrieve secret later!**

6. API permissions → Add permission → Windows Store → `user_impersonation` → Grant admin consent

---

### Step 2: Partner Center (5 min)

1. Go to https://partner.microsoft.com/dashboard
2. Create app → Reserve name "Camera Reactions"
3. Product identity → Copy Store ID:

```
✓ Store ID: ___________________________________
```

4. Account settings → User management → Azure AD applications → Add
5. Enter your Application (client) ID → Role: Manager → Save

---

### Step 3: GitHub Secrets (5 min)

GitHub repo → Settings → Secrets and variables → Actions → New repository secret

Add these 4 secrets:

```yaml
AZURE_TENANT_ID:     [Your Directory ID]
AZURE_CLIENT_ID:     [Your Application ID]
AZURE_CLIENT_SECRET: [Your Client Secret VALUE]
STORE_APP_ID:        [Your Store ID]
```

---

### Step 4: Update Workflow (2 min)

Edit `.github/workflows/store-publish.yml`:

**Line 18** - Change publisher name:
```yaml
PUBLISHER_NAME: 'CN=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
```

**Find your publisher:**
- Partner Center → Account Settings → Organization profile
- Copy Publisher ID (starts with `CN=`)

---

### Step 5: Create Assets (30 min)

Create these 5 PNG images in `assets/store/`:

| File | Size | Purpose |
|------|------|---------|
| Square44x44Logo.png | 44×44 | App list icon |
| Square150x150Logo.png | 150×150 | Medium tile |
| Wide310x150Logo.png | 310×150 | Wide tile |
| StoreLogo.png | 50×50 | Store icon |
| SplashScreen.png | 620×300 | Splash screen |

**Quick tools:**
- Figma (free): https://figma.com
- Canva (free): https://canva.com
- Fiverr ($5-20): Search "app icon design"

**Update workflow** to use real assets:

Find "Create placeholder assets" step, replace with:
```yaml
- name: Copy real assets
  run: |
    Copy-Item "assets\store\*" -Destination "msix\Assets\" -Force
  shell: pwsh
```

Commit assets:
```bash
git add assets/store/
git commit -m "Add Microsoft Store assets"
git push
```

---

### Step 6: Trigger Build (2 min)

**Option A: Tag-based** (recommended)
```bash
git tag -a store-v1.0.0 -m "Microsoft Store release v1.0.0"
git push origin store-v1.0.0
```

**Option B: Manual**
- GitHub → Actions → "Publish to Microsoft Store"
- Run workflow → Enter version: `1.0.0.0` → Run

---

## Verify Success

1. **GitHub Actions** → Check workflow ran successfully
2. **Artifacts** → Download `msix-package`
3. **Test locally:**
   ```powershell
   # Enable Developer Mode first in Windows Settings
   Add-AppxPackage -Path "CameraReactions_1.0.0.0_x64.msix"
   ```
4. **Launch app** from Start Menu → Test all features

---

## Submit to Store (First Time - Manual)

1. Download MSIX from GitHub Actions artifacts
2. Partner Center → Your app → Start submission
3. Complete all sections:
   - Pricing: Free
   - Properties: Category, Privacy policy
   - Age ratings: Complete questionnaire
   - Packages: Upload MSIX
   - Store listings: Description, screenshots
4. Submit for certification (24-48 hours)

---

## Future Releases (Automated)

After first manual submission, every release is automatic:

```bash
# Increment version and tag
git tag -a store-v1.1.0 -m "Release 1.1.0 - Bug fixes"
git push origin store-v1.1.0

# That's it! Workflow handles everything:
# ✓ Builds MSIX
# ✓ Signs package
# ✓ Uploads to GitHub Release
# ✓ Submits to Store (optional)
```

---

## Common Issues

**"Publisher name doesn't match"**
- Update `PUBLISHER_NAME` in workflow
- Must match Partner Center exactly

**"Authentication failed"**
- Verify all 4 GitHub secrets are correct
- Check Azure AD app has Windows Store permission
- Ensure admin consent granted

**"Assets missing"**
- Create all 5 PNG files
- Place in `assets/store/`
- Update workflow to copy from assets

**"Invalid package"**
- Ensure version format: `1.0.0.0`
- Check AppxManifest.xml is valid
- Test locally before pushing

---

## Cost

| Item | Cost |
|------|------|
| Microsoft Developer Account | $19 (already paid) |
| Azure AD | Free |
| GitHub Actions (public repo) | Free |
| Asset creation (DIY) | Free |
| **Total ongoing** | **$0** |

---

## Resources

- **Full setup guide:** `docs/STORE_CICD_SETUP.md`
- **Azure Portal:** https://portal.azure.com
- **Partner Center:** https://partner.microsoft.com/dashboard
- **GitHub Actions:** Repository → Actions tab

---

## Support

**Detailed help:** See `docs/STORE_CICD_SETUP.md` for step-by-step instructions

**Questions?** Open an issue on GitHub

**Ready to publish?** Follow Step 1 above! 🚀

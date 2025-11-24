# Azure AD Application Setup - Step-by-Step Walkthrough

**Purpose:** Enable GitHub Actions to automatically submit to Microsoft Store

**Time:** 10-15 minutes

**Prerequisites:**
- Microsoft Account with Partner Center access
- Browser with access to Azure Portal

---

## What You're About To Do

You'll create an Azure AD application that acts as a "service account" allowing GitHub Actions to:
1. Authenticate with Microsoft Store API
2. Upload MSIX packages automatically
3. Submit app updates without manual intervention

**Think of it as:** A key that GitHub can use to access your Microsoft Store account on your behalf.

---

## Step 1: Access Azure Portal (1 minute)

### Open Azure Portal

1. **Go to Azure Portal:**
   ```
   https://portal.azure.com
   ```

2. **Sign in** with your Microsoft account
   - Use the same account as your Microsoft Developer/Partner Center

3. **Verify you're logged in:**
   - You should see the Azure Portal dashboard
   - Top right corner shows your account name

---

## Step 2: Navigate to Azure Active Directory (1 minute)

### Find Azure AD Service

1. **Search for "Azure Active Directory":**
   - Click the search bar at the top
   - Type: `Azure Active Directory`
   - Click on the service (has a blue icon)

   **Alternative:**
   - Click "All services" in left sidebar
   - Find "Azure Active Directory" under "Identity"

2. **You should now see the Azure AD Overview page**
   - Shows your directory name
   - Shows tenant information
   - Left sidebar has menu options

---

## Step 3: Register New Application (3 minutes)

### Create App Registration

1. **Click "App registrations" in the left sidebar**
   - Under "Manage" section
   - Shows list of registered applications

2. **Click "+ New registration"** (top of page)

3. **Fill in the registration form:**

   **Name:**
   ```
   CameraReactions-GitHub-Actions
   ```
   - This name is for your reference
   - Makes it easy to identify later

   **Supported account types:**
   - Select: **"Accounts in this organizational directory only"**
   - This is the most secure option
   - Only your directory can use this app

   **Redirect URI:**
   - Leave blank (not needed)
   - Skip this section

4. **Click "Register"** button

5. **Wait for app to be created** (takes 2-3 seconds)

---

## Step 4: Save Application IDs (2 minutes)

### Copy Important Values

After registration, you'll see the app's **Overview** page.

**IMPORTANT:** Keep this page open and copy these 2 values:

### Value 1: Application (client) ID

**Where to find it:**
- On the Overview page
- Under "Essentials" section
- Labeled: **"Application (client) ID"**
- Format: `12345678-1234-1234-1234-123456789abc`

**Copy this value:**
```
Application (client) ID: ___________________________________
```

⚠️ **Save this as:** `AZURE_CLIENT_ID` (for GitHub Secrets later)

### Value 2: Directory (tenant) ID

**Where to find it:**
- Same Overview page
- Under "Essentials" section
- Labeled: **"Directory (tenant) ID"**
- Format: `87654321-4321-4321-4321-cba987654321`

**Copy this value:**
```
Directory (tenant) ID: ___________________________________
```

⚠️ **Save this as:** `AZURE_TENANT_ID` (for GitHub Secrets later)

**Tip:** Open Notepad or Notes app to keep track of these values!

---

## Step 5: Create Client Secret (3 minutes)

### Generate Authentication Secret

1. **Click "Certificates & secrets"** in the left sidebar
   - Under "Manage" section

2. **Click the "Client secrets" tab**
   - Should be selected by default

3. **Click "+ New client secret"**

4. **Fill in the form:**

   **Description:**
   ```
   GitHub Actions Automation Key
   ```
   - Helps you remember what this is for

   **Expires:**
   - Select: **"24 months"** (recommended)
   - Or: **"Custom"** and set to 24 months
   - Longer expiry means less maintenance

5. **Click "Add"**

6. **IMMEDIATELY copy the Value:**
   - You'll see the secret appear
   - Two columns: "Secret ID" and "Value"
   - **Copy the "Value" column** (NOT the Secret ID)
   - Format: Long random string like `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0`

**Copy this value NOW:**
```
Client Secret VALUE: ___________________________________
```

⚠️ **CRITICAL:** You can only see this ONCE!
⚠️ **Save this as:** `AZURE_CLIENT_SECRET` (for GitHub Secrets)
⚠️ **If you lose it:** You'll have to create a new secret

**What if I missed it?**
- Delete the secret you just created
- Create a new one
- Copy the value this time!

---

## Step 6: Grant API Permissions (3 minutes)

### Give Access to Windows Store

1. **Click "API permissions"** in the left sidebar
   - Under "Manage" section

2. **You'll see default permissions:**
   - "Microsoft Graph" → "User.Read" (already there)
   - This is fine, keep it

3. **Click "+ Add a permission"**

4. **Select the API:**
   - Click **"APIs my organization uses"** tab
   - In the search box, type: `Windows Store`
   - Click on **"Windows Store"** when it appears

   **Don't see "Windows Store"?**
   - Type exactly: `Windows Store for Business`
   - Or search for: `Microsoft Store`
   - Should appear in the list

5. **Select permission type:**
   - Click **"Delegated permissions"**

6. **Select specific permissions:**
   - Check the box: ✅ **"user_impersonation"**
   - This allows the app to act on your behalf

7. **Click "Add permissions"**

8. **Grant Admin Consent (Important!):**
   - You'll see a warning banner
   - Click **"Grant admin consent for [Your Directory]"**
   - Click **"Yes"** in the confirmation dialog
   - Status should change to green checkmark: ✅ "Granted"

**Why admin consent?**
- Required for the app to actually use these permissions
- Without this, authentication will fail
- It's safe - you're granting consent to your own app

---

## Step 7: Associate with Partner Center (3 minutes)

### Link Azure AD App to Store Account

1. **Open Partner Center in a new tab:**
   ```
   https://partner.microsoft.com/dashboard
   ```

2. **Navigate to User Management:**
   - Click your profile icon (top right)
   - Click **"Account settings"**
   - Or: Click gear icon ⚙️ → "Account settings"

3. **Find Azure AD Applications:**
   - In left sidebar, click **"User management"**
   - Click **"Azure AD applications"** tab

4. **Add Your Application:**
   - Click **"+ Add Azure AD applications"**

5. **Enter Application ID:**
   - Paste your **Application (client) ID** from Step 4
   - The same ID you saved earlier

6. **Assign Role:**
   - Select role: **"Manager"**
   - This is required for submissions
   - "Developer" role won't work for submissions

7. **Click "Save"**

8. **Verify:**
   - Your app should appear in the list
   - Shows: Application name, ID, and role

---

## Step 8: Get Your Store App ID (2 minutes)

### Find Your Application Store ID

1. **Still in Partner Center:**
   ```
   https://partner.microsoft.com/dashboard/apps/overview
   ```

2. **Select or Create Your App:**

   **If you already created the app:**
   - Click on "Camera Reactions" (or your app name)
   - Go to step 3

   **If you haven't created it yet:**
   - Click **"+ Create a new app"**
   - Enter name: `Camera Reactions`
   - Check availability
   - Click "Reserve product name"
   - Continue to step 3

3. **Get the Store ID:**
   - In your app dashboard, look for **"Product identity"** section
   - Or: Go to "Product management" → "Product identity"

4. **Copy the Store ID:**
   - Look for: **"Store ID"** or **"Application ID"**
   - Format: `9NXXXXXXXXX` (starts with 9N)

   **Copy this value:**
   ```
   Store ID: ___________________________________
   ```

⚠️ **Save this as:** `STORE_APP_ID` (for GitHub Secrets)

**Can't find Store ID?**
- Try: "Product identity" page
- Or: Look for "Windows Store ID"
- Or: Check "App identity" section

---

## Summary: What You Should Have Now

### 4 Values to Save

You should have these 4 pieces of information:

```
✓ Application (client) ID:  ________-____-____-____-____________
  → Save as: AZURE_CLIENT_ID

✓ Directory (tenant) ID:    ________-____-____-____-____________
  → Save as: AZURE_TENANT_ID

✓ Client Secret VALUE:      _______________________________
  → Save as: AZURE_CLIENT_SECRET

✓ Store ID:                 9N____________
  → Save as: STORE_APP_ID
```

⚠️ **Keep these values safe!**
- Store them in a password manager (recommended)
- Or save in a secure note
- You'll need them for GitHub Secrets in next step

---

## What You've Accomplished ✅

You now have:

1. ✅ Azure AD Application created
2. ✅ Client secret generated
3. ✅ Windows Store API permissions granted
4. ✅ Admin consent provided
5. ✅ App associated with Partner Center
6. ✅ Store App ID retrieved

**Next step:** Add these 4 values to GitHub Secrets

---

## Troubleshooting

### Issue: "Can't find Azure Active Directory"

**Solution:**
- Make sure you're signed into https://portal.azure.com
- Try direct link: https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade
- Check you're using the correct Microsoft account

### Issue: "Can't find Windows Store in API permissions"

**Solution:**
- Search for: `Windows Store for Business`
- Or: `Microsoft Store`
- Make sure you selected "APIs my organization uses" tab
- Verify your account has Partner Center access

### Issue: "Grant admin consent button disabled"

**Solution:**
- You need admin rights in your Azure AD
- If it's your personal account, you should have admin rights
- Try signing out and back in
- Check if there's a pending verification

### Issue: "Can't find Store ID"

**Solution:**
- Go to Partner Center → Your app → Product management
- Click "Product identity"
- Look for "Store ID" or "Windows Store ID"
- Should start with "9N"

### Issue: "Lost my client secret value"

**Solution:**
- No way to retrieve it
- Delete the old secret
- Create a new client secret
- Copy the value immediately this time

---

## Security Best Practices

1. **Never commit secrets to code:**
   - Don't paste in source files
   - Don't include in documentation
   - Only store in GitHub Secrets (next step)

2. **Rotate secrets regularly:**
   - Set reminder to rotate in 24 months
   - Create new secret before old one expires
   - Update GitHub Secrets with new value

3. **Limit permissions:**
   - Only grant what's needed
   - "user_impersonation" is sufficient
   - Don't add extra permissions

4. **Use password manager:**
   - Store the 4 values securely
   - Use 1Password, LastPass, or Bitwarden
   - Include context (which value is which)

---

## Next Steps

Now that you have Azure AD set up, proceed to:

**➡️ Configure GitHub Secrets**
- Add the 4 values to your GitHub repository
- See: `docs/GITHUB_SECRETS_SETUP.md`

**After that:**
- Create store assets (5 PNG images)
- Test the workflow
- Submit to Microsoft Store

---

## Quick Reference

**Azure Portal:** https://portal.azure.com
**Partner Center:** https://partner.microsoft.com/dashboard
**Azure AD Direct Link:** https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade

**What to do next:** Configure GitHub Secrets with your 4 values

Great job! Azure AD setup is complete! 🎉

# GitHub Secrets Setup Guide

**Purpose:** Add Azure AD credentials to GitHub for automated Store publishing

**Time:** 5 minutes

**Prerequisites:**
- Azure AD application created (completed previous step)
- 4 values ready to use:
  - `AZURE_CLIENT_ID`
  - `AZURE_TENANT_ID`
  - `AZURE_CLIENT_SECRET`
  - `STORE_APP_ID`

---

## What Are GitHub Secrets?

**GitHub Secrets** are encrypted environment variables that:
- Store sensitive information securely
- Are never exposed in logs or code
- Can be used in GitHub Actions workflows
- Only accessible to repository workflows

**Why we need them:**
- Store Azure AD credentials securely
- Allow workflows to authenticate with Microsoft Store
- Enable automated app submissions

---

## Step-by-Step Instructions

### Step 1: Open Your Repository Settings (1 min)

1. **Go to your GitHub repository:**
   ```
   https://github.com/tysoncung/reactions-app
   ```

2. **Click the "Settings" tab:**
   - Located in the top navigation bar
   - Between "Insights" and the repo name

3. **Navigate to Secrets:**
   - In left sidebar, expand **"Secrets and variables"**
   - Click **"Actions"**

4. **You should see the "Actions secrets" page:**
   - Shows list of repository secrets (currently empty)
   - Has "New repository secret" button

---

### Step 2: Add Secret #1 - AZURE_TENANT_ID (1 min)

1. **Click "New repository secret"** button (green button, top right)

2. **Fill in the form:**

   **Name:**
   ```
   AZURE_TENANT_ID
   ```
   - Must be EXACTLY this name (case-sensitive)
   - No spaces, all uppercase

   **Secret:**
   ```
   [Paste your Directory (tenant) ID from Azure AD]
   ```
   - Format: `12345678-1234-1234-1234-123456789abc`
   - This is the value you copied in Azure AD Step 4

3. **Click "Add secret"**

4. **Verify:**
   - Secret appears in the list
   - Shows name and "Updated X seconds ago"
   - Value is hidden (shows as •••)

---

### Step 3: Add Secret #2 - AZURE_CLIENT_ID (1 min)

1. **Click "New repository secret"** again

2. **Fill in the form:**

   **Name:**
   ```
   AZURE_CLIENT_ID
   ```

   **Secret:**
   ```
   [Paste your Application (client) ID from Azure AD]
   ```
   - Format: `87654321-4321-4321-4321-cba987654321`
   - This is from Azure AD Step 4

3. **Click "Add secret"**

---

### Step 4: Add Secret #3 - AZURE_CLIENT_SECRET (1 min)

⚠️ **IMPORTANT:** This is the most sensitive value!

1. **Click "New repository secret"**

2. **Fill in the form:**

   **Name:**
   ```
   AZURE_CLIENT_SECRET
   ```

   **Secret:**
   ```
   [Paste your Client Secret VALUE from Azure AD]
   ```
   - The long random string from Azure AD Step 5
   - NOT the Secret ID - the VALUE!
   - Format: Long alphanumeric string

3. **Click "Add secret"**

---

### Step 5: Add Secret #4 - STORE_APP_ID (1 min)

1. **Click "New repository secret"**

2. **Fill in the form:**

   **Name:**
   ```
   STORE_APP_ID
   ```

   **Secret:**
   ```
   [Paste your Store ID from Partner Center]
   ```
   - Format: `9NXXXXXXXXX` (starts with 9N)
   - This is from Azure AD Step 8

3. **Click "Add secret"**

---

## Step 6: Verify All Secrets (1 min)

### Check Your Secrets List

You should now see **4 secrets** in the list:

```
✓ AZURE_CLIENT_ID      Updated X minutes ago
✓ AZURE_CLIENT_SECRET  Updated X minutes ago
✓ AZURE_TENANT_ID      Updated X minutes ago
✓ STORE_APP_ID         Updated X minutes ago
```

**Important checks:**
- All names are **EXACTLY** as shown above
- All are uppercase
- No typos in names
- 4 secrets total

**If something is wrong:**
- You can't edit secrets (security feature)
- Delete the incorrect one
- Create a new one with correct name/value

---

## How Secrets Are Used

### In GitHub Actions Workflow

Your workflow (`.github/workflows/store-publish.yml`) accesses secrets like this:

```yaml
env:
  AZURE_TENANT_ID: ${{ secrets.AZURE_TENANT_ID }}
  AZURE_CLIENT_ID: ${{ secrets.AZURE_CLIENT_ID }}
  AZURE_CLIENT_SECRET: ${{ secrets.AZURE_CLIENT_SECRET }}
  STORE_APP_ID: ${{ secrets.STORE_APP_ID }}
```

**Security features:**
- Values are never printed in logs
- Show as `***` if accidentally exposed
- Only available during workflow execution
- Encrypted at rest in GitHub

---

## Testing the Secrets

### Verify Secrets Work

You don't need to manually test - the workflow will validate them.

**When you trigger the workflow:**
1. GitHub injects secrets as environment variables
2. Workflow authenticates with Azure AD
3. If authentication succeeds, secrets are correct
4. If it fails, you'll see error messages

**Common error messages:**
- `"Authentication failed"` → Check AZURE_CLIENT_SECRET
- `"Invalid client"` → Check AZURE_CLIENT_ID
- `"Invalid tenant"` → Check AZURE_TENANT_ID
- `"App not found"` → Check STORE_APP_ID

---

## Security Best Practices

### Do's ✅

- **Use GitHub Secrets for all sensitive data**
- **Rotate secrets every 12-24 months**
- **Keep secrets in password manager as backup**
- **Set calendar reminder to renew before expiry**
- **Use least-privilege permissions**

### Don'ts ❌

- **Never commit secrets to code**
- **Don't print secrets in logs**
- **Don't share secrets publicly**
- **Don't store in plain text files**
- **Don't use same secrets across projects**

---

## Managing Secrets

### Update a Secret

1. Go to Settings → Secrets and variables → Actions
2. Click on the secret name
3. Click "Update secret"
4. Enter new value
5. Click "Update secret"

### Delete a Secret

1. Go to Settings → Secrets and variables → Actions
2. Click the trash icon next to secret
3. Confirm deletion
4. Secret is permanently deleted

### Rotate Secrets

**When to rotate:**
- Every 24 months (when secret expires)
- If secret is compromised
- When team member with access leaves
- As best practice annually

**How to rotate:**
1. Create new client secret in Azure AD
2. Update GitHub Secret with new value
3. Test workflow to verify it works
4. Delete old secret from Azure AD

---

## Troubleshooting

### Issue: "Secret name already exists"

**Solution:**
- Delete the existing secret
- Create a new one
- Make sure name matches exactly

### Issue: "Can't find Secrets settings"

**Solution:**
- Make sure you're in "Settings" tab
- Check you have admin access to repository
- Look for "Secrets and variables" → "Actions"

### Issue: "Workflow can't access secrets"

**Solution:**
- Verify secret names match exactly (case-sensitive)
- Check workflow syntax: `${{ secrets.SECRET_NAME }}`
- Ensure repository is not a fork (forks have limited secret access)

### Issue: "Authentication fails in workflow"

**Solution:**
- Double-check all 4 secrets are set correctly
- Verify you copied the VALUE (not the Secret ID) for client secret
- Check Azure AD app has Windows Store permission granted
- Verify admin consent was granted

### Issue: "Can't remember which value is which"

**Solution:**
- Azure AD App → Overview shows Client ID and Tenant ID
- Azure AD App → Certificates & secrets shows secrets (but not values)
- If you lost client secret value, create a new one
- Partner Center → Product identity shows Store ID

---

## What You've Accomplished ✅

You now have:

1. ✅ All 4 secrets added to GitHub
2. ✅ Secrets encrypted and secure
3. ✅ Workflow can authenticate with Microsoft Store
4. ✅ Ready to test automated publishing

**Next steps:**
1. Create store assets (5 PNG images)
2. Test the workflow
3. Submit to Microsoft Store

---

## Quick Reference

### Secret Names (Must Be Exact)

```
AZURE_TENANT_ID       - Directory ID from Azure AD
AZURE_CLIENT_ID       - Application ID from Azure AD
AZURE_CLIENT_SECRET   - Client secret VALUE from Azure AD
STORE_APP_ID          - Store ID from Partner Center
```

### Where to Find in GitHub

```
Repository → Settings → Secrets and variables → Actions
```

### Where Values Come From

```
AZURE_TENANT_ID     → Azure Portal → App Overview
AZURE_CLIENT_ID     → Azure Portal → App Overview
AZURE_CLIENT_SECRET → Azure Portal → Certificates & secrets
STORE_APP_ID        → Partner Center → Product identity
```

---

## Additional Resources

**GitHub Docs:**
- Encrypted secrets: https://docs.github.com/en/actions/security-guides/encrypted-secrets

**Microsoft Docs:**
- Partner Center API: https://docs.microsoft.com/windows/uwp/monetize/create-and-manage-submissions-using-windows-store-services

**Your Documentation:**
- Azure AD Setup: `docs/AZURE_AD_SETUP_WALKTHROUGH.md`
- CI/CD Setup: `docs/STORE_CICD_SETUP.md`
- Quick Start: `docs/STORE_CICD_QUICKSTART.md`

---

Great job! GitHub Secrets are now configured! 🎉

**Next:** Create the 5 store assets (PNG images) to complete the setup.

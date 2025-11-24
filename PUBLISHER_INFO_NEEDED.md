# Publisher Information Needed

To complete the Microsoft Store workflow setup, I need your publisher information from Partner Center.

## Required Information

### 1. Publisher ID (Required)

**Where to find it:**
1. Go to: https://partner.microsoft.com/dashboard
2. Click gear icon ⚙️ (top right) → "Account settings"
3. Click "Organization profile"
4. Look for: **"Publisher ID"**

**Format:**
- Usually: `CN=12345678-1234-1234-1234-123456789ABC`
- Or: `CN=YourName` or `CN=YourCompanyName`

**Paste your Publisher ID here:**
```
Publisher ID: ___________________________________
```

### 2. Publisher Display Name (Required)

**Where to find it:**
- Same page as above
- Look for: **"Publisher display name"**

**Examples:**
- "Tyson Cung"
- "Your Company Name"
- "YourDeveloperName"

**Paste your Publisher Display Name here:**
```
Publisher Display Name: ___________________________________
```

---

## Why This Is Needed

The workflow file (`.github/workflows/store-publish.yml`) needs to:
1. Create proper AppxManifest.xml with your publisher ID
2. Sign the MSIX package with your identity
3. Match Partner Center account for submission

These values must match **exactly** what's in your Partner Center account.

---

## What I'll Do With This Info

Once you provide:
1. Update workflow file with your publisher info
2. Commit and push changes
3. Test the workflow with a tag
4. Create your first automated build!

---

Please provide both values above, and I'll update the workflow immediately! 🚀

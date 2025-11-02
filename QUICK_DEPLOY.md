# Quick Deploy Instructions

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `vinyl-verse` (or any name you prefer)
3. Description: "E-commerce app for framed vinyl records"
4. Choose Public or Private
5. Do NOT initialize with README (we already have one)
6. Click "Create repository"

## Step 2: Push to GitHub

After creating the repo, GitHub will show you commands. Run these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual GitHub username and repo name.

## Step 3: Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository from the dropdown
5. Branch: `main`
6. Main file path: `app.py`
7. Click "Deploy"

Your app will be live in 1-2 minutes!

## Alternative: Quick Deploy Command

If you want me to help you push, share your GitHub repo URL and I can help set it up.


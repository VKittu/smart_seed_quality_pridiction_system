# 🚀 Deployment Guide - Smart Seed Quality Prediction System

## ⚠️ Important: Fix Streamlit Cloud Deploy Error

### Problem
Streamlit Cloud failed with: `Failed to download the sources for repository`

### Solution: Verify Repository Settings ✅

1. **Ensure repository is PUBLIC**
   ```bash
   # Go to: https://github.com/VKittu/smart_seed_quality_pridiction_system/settings
   # Set to PUBLIC (not Private)
   ```

2. **Verify all required files exist:**
   - ✅ `requirements.txt` - Added
   - ✅ `app/streamlit_app.py` - Already exists
   - ✅ `Dockerfile` - Added
   - ✅ `.streamlit/config.toml` - Added
   - ✅ `environment.yml` - Already exists
   - ✅ `.github/workflows/deploy.yml` - Added
   - ⚠️ **CRITICAL**: `src/pipeline.pkl` - **MUST EXIST**

3. **Create the model file if missing:**
   ```bash
   # Either:
   # A) Train it locally
   python src/train_model.py
   
   # B) Or push a pre-trained model to repo
   # Place pipeline.pkl in src/ folder
   ```

4. **Push changes to GitHub**
   ```bash
   git add .
   git commit -m "Add deployment files and configuration"
   git push origin main
   ```

---

## 🌐 Deployment Options (in order of simplicity)

### Option 1: Streamlit Cloud ⭐ RECOMMENDED (Easiest & Free)

**Step 1:** Verify fixes above ✅

**Step 2:** Go to https://streamlit.io/cloud

**Step 3:** Click "New App"
- Repository: `VKittu/smart_seed_quality_pridiction_system`
- Branch: `main`
- Main file path: `app/streamlit_app.py`

**Step 4:** Click "Deploy"

✅ App goes **LIVE** in 2-3 minutes!

**Your public URL:** `https://<your-username>-smart-seed.streamlit.app`

---

### Option 2: Docker + Heroku (Free tier ended, but still works)

```bash
# 1. Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# 2. Login
heroku login

# 3. Create app
heroku create your-seed-quality-app

# 4. Build & Deploy
heroku container:push web --app your-seed-quality-app
heroku container:release web --app your-seed-quality-app

# 5. Open app
heroku open --app your-seed-quality-app
```

**Your public URL:** `https://your-seed-quality-app.herokuapp.com`

---

### Option 3: Railway.app (Easiest Docker Alternative)

1. Go to https://railway.app
2. New Project → GitHub Repo
3. Connect your GitHub account
4. Select this repository
5. Railway auto-detects Dockerfile ✅
6. Deploy!

**Your public URL:** `https://your-app-randomid.railway.app`

---

### Option 4: Google Cloud Run

```bash
# 1. Install Google Cloud SDK
# https://cloud.google.com/sdk/docs/install

# 2. Build image
gcloud builds submit --tag gcr.io/YOUR-PROJECT/seed-quality

# 3. Deploy
gcloud run deploy seed-quality \
  --image gcr.io/YOUR-PROJECT/seed-quality \
  --platform managed \
  --region us-central1 \
  --port 8501
```

---

### Option 5: AWS Lambda + API Gateway

Use AWS SAM or Zappa:
```bash
pip install zappa
zappa init
zappa deploy production
```

---

### Option 6: Custom VPS (DigitalOcean, Linode, AWS EC2)

```bash
# 1. SSH into your server
ssh root@your-server-ip

# 2. Clone repo
git clone https://github.com/VKittu/smart_seed_quality_pridiction_system.git
cd smart_seed_quality_pridiction_system

# 3. Install Python & dependencies
sudo apt update
sudo apt install python3.10 python3-pip
pip install -r requirements.txt

# 4. Run with Gunicorn + systemd
pip install gunicorn
sudo systemctl start seed-quality
sudo systemctl enable seed-quality

# 5. Setup Nginx reverse proxy
# ... (nginx configuration)

# 6. Get SSL certificate
sudo apt install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d yourdomain.com
```

---

## 📋 Comparison of Options

| Option | Cost | Setup Time | Difficulty | Pros | Cons |
|--------|------|-----------|-----------|------|------|
| **Streamlit Cloud** | Free | 5 min | ⭐ Very Easy | Auto-deploy, built for Streamlit, no ops | Limited customization |
| **Railway** | Free tier | 10 min | ⭐ Easy | Simple, good free tier | Can get slow |
| **Heroku** | Paid (~$7/mo) | 15 min | ⭐⭐ Easy | Reliable, good docs | Paid now |
| **Google Cloud Run** | Free tier | 20 min | ⭐⭐ Medium | Scalable, pay-per-use | Needs GCP account |
| **AWS Lambda** | Free tier | 30 min | ⭐⭐⭐ Hard | Scalable, serverless | Complex setup |
| **Custom VPS** | $5-10/mo | 30 min | ⭐⭐⭐ Hard | Full control | Need DevOps skills |

---

## 🔧 Environment Variables (if needed)

Create `.streamlit/secrets.toml` locally:
```toml
# Database connection
database_url = "postgresql://user:pass@host/db"

# API keys
api_key = "your-api-key"
```

For Streamlit Cloud:
1. Go to App settings → Secrets
2. Paste your secrets
3. They're automatically available in the app

---

## 📊 Monitoring & Logging

### Streamlit Cloud
- Logs: App → Manage app → Settings → Logs
- Real-time monitoring available

### Docker/Custom
```bash
# View logs
docker logs seed-quality

# Monitor resources
docker stats

# Check health
curl http://localhost:8501/_stcore/health
```

---

## 🔄 Continuous Deployment (CI/CD)

Your `.github/workflows/deploy.yml` automatically:
1. ✅ Runs tests on every push
2. ✅ Checks imports
3. ✅ Verifies code quality

Streamlit Cloud also auto-deploys on push to main!

---

## 🎯 Recommended Path for You

1. **RIGHT NOW:**
   ```bash
   # Ensure pipeline.pkl exists
   ls -la src/pipeline.pkl
   
   # Push all changes
   git add .
   git commit -m "Complete deployment setup"
   git push origin main
   ```

2. **THEN:**
   - Go to https://streamlit.io/cloud
   - Connect your GitHub account
   - Deploy this repo
   - Done! 🎉

3. **FINALLY:**
   - Share your public URL with users
   - Monitor logs
   - Update model as needed

---

## ⚠️ Common Deployment Issues

### Issue: `ModuleNotFoundError` on deployment
**Fix:** Ensure all packages in `requirements.txt`
```bash
pip freeze | grep -E "streamlit|pandas|scikit" > requirements.txt
```

### Issue: `pipeline.pkl` not found
**Fix:** Ensure file exists and is committed
```bash
git add src/pipeline.pkl
git commit -m "Add trained model"
git push
```

### Issue: Out of memory
**Fix:** Streamlit Cloud has 1GB RAM limit
- Use smaller models
- Optimize preprocessing
- Cache aggressively with `@st.cache_data`

### Issue: Slow predictions
**Fix:** Add timeout and caching
```python
@st.cache_data
def load_pipeline(path="src/pipeline.pkl"):
    return joblib.load(path)
```

### Issue: `No space left on device`
**Fix:** Docker image too large
- Use `slim` base image (done ✅)
- Remove unnecessary files
- Use `.dockerignore`

---

## 🆘 Support

- **Streamlit Docs:** https://docs.streamlit.io
- **Streamlit Community:** https://discuss.streamlit.io
- **Docker Docs:** https://docs.docker.com
- **Your Repo Issues:** https://github.com/VKittu/smart_seed_quality_pridiction_system/issues

---

## ✅ Pre-Deployment Checklist

- [ ] `requirements.txt` created
- [ ] `Dockerfile` created
- [ ] `.streamlit/config.toml` created
- [ ] `.github/workflows/deploy.yml` created
- [ ] `SETUP.md` & `DEPLOYMENT.md` created
- [ ] `src/pipeline.pkl` exists (trained model)
- [ ] `app/streamlit_app.py` verified
- [ ] All files committed to GitHub
- [ ] Repository is PUBLIC
- [ ] README.md updated with deploy link

**All done? → Deploy on Streamlit Cloud now! 🚀**

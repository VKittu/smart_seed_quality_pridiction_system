# 🌱 Setup Guide - Smart Seed Quality Prediction System

## Quick Start (5 minutes)

### Prerequisites
- Python 3.10 or higher
- Git
- pip or conda

### Step 1: Clone Repository
```bash
git clone https://github.com/VKittu/smart_seed_quality_pridiction_system.git
cd smart_seed_quality_pridiction_system
```

### Step 2: Create Virtual Environment

**Using Conda (Recommended):**
```bash
conda env create -f environment.yml
conda activate seed-q
```

**Using pip + venv:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
streamlit run app/streamlit_app.py
```

🎉 **App opens at:** `http://localhost:8501`

---

## File Structure

```
smart_seed_quality_pridiction_system/
│
├── app/
│   └── streamlit_app.py          # Main web interface
│
├── src/
│   ├── train_model.py            # Model training script (optional)
│   └── pipeline.pkl              # Trained ML model (required)
│
├── data/
│   └── seed_data.csv             # Training/test dataset
│
├── models/
│   └── pipeline.pkl              # Backup model location
│
├── environment.yml               # Conda dependencies
├── requirements.txt              # Pip dependencies ✅
├── Dockerfile                    # Docker configuration ✅
├── .streamlit/config.toml        # Streamlit config ✅
├── DEPLOYMENT.md                 # Deployment guide ✅
├── README.md                     # Project documentation
└── .gitignore                    # Git ignore rules ✅
```

---

## Features

### 🖥️ Web Interface (Streamlit)
- **Single Sample Prediction**: Enter seed parameters manually
- **Batch Prediction**: Upload CSV for multiple predictions
- **SHAP Explanations**: Understand why seeds are classified as Good/Bad
- **Feature Importance**: See which factors matter most
- **Beautiful UI**: Theme configured in `.streamlit/config.toml`

### 🤖 ML Model
- **Algorithm**: Random Forest Classifier
- **Accuracy**: ~99%
- **Features**: 11 physical & biological parameters
- **Output**: Good / Bad classification with probability scores

### 📊 Input Features
| Feature | Description |
|---------|-------------|
| Moisture (%) | Water content |
| Germination (%) | Germination rate |
| Purity (%) | Seed purity level |
| Vigor Index | Seed strength |
| Fungal Infestation (%) | Fungus infection level |
| Discoloration (%) | Color abnormality |
| Protein Content (%) | Protein percentage |
| Oil Content (%) | Oil percentage |
| Seed Age (days) | Age of seed |
| Seed Length (mm) | Physical length |
| Seed Width (mm) | Physical width |

---

## Running Different Ways

### Option 1: Development Mode
```bash
streamlit run app/streamlit_app.py
```
- Hot reload enabled
- Debug information shown
- Best for development

### Option 2: Production Mode
```bash
streamlit run app/streamlit_app.py \
  --logger.level=info \
  --server.runOnSave false \
  --client.showErrorDetails false
```

### Option 3: Docker
```bash
docker build -t seed-quality .
docker run -p 8501:8501 seed-quality
```

### Option 4: Streamlit Cloud
- Push to GitHub
- Go to streamlit.io/cloud
- Deploy in 1 click!

---

## Required Model File

The app expects `src/pipeline.pkl` with this structure:
```python
{
    'pipeline': sklearn.pipeline.Pipeline,
    'meta': {
        'features': [
            'moisture', 'germination', 'purity', 'vigor_index',
            'fungal_infestation', 'discoloration', 'protein_content',
            'oil_content', 'seed_age', 'seed_length', 'seed_width'
        ]
    }
}
```

### Generate Model (if missing):
```bash
cd src
python train_model.py
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'streamlit'`
```bash
pip install -r requirements.txt
# or
conda env create -f environment.yml
```

### Issue: `FileNotFoundError: src/pipeline.pkl`
- Ensure model file exists
- Run training script: `python src/train_model.py`
- Check file path in `app/streamlit_app.py` line 9

### Issue: Port 8501 already in use
```bash
streamlit run app/streamlit_app.py --server.port 8502
```

### Issue: Slow predictions
- SHAP explanations add ~1-2 seconds per prediction
- This is normal for tree-based models
- Can be optimized using `TreeExplainer` caching

---

## Development Tips

### Add New Features to the App
Edit `app/streamlit_app.py`:
```python
# Add more metrics display
st.write("Accuracy: ", model_accuracy)

# Add charts
import plotly.express as px
fig = px.histogram(results, x='pred_proba')
st.plotly_chart(fig)
```

### Customize Appearance
Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#2E8B57"      # Green for agriculture
backgroundColor = "#F0FFF0"   # Light green background
```

### Enable Cloud Features
Add `secrets.toml` for API keys:
```
# .streamlit/secrets.toml
database_url = "postgresql://..."
api_key = "your-key"
```

---

## Performance Optimization

### Caching
Already implemented with `@st.cache_data` decorator ✅

### Improve Speed
1. Reduce SHAP explanation for batch predictions
2. Use simpler model for real-time predictions
3. Pre-compute feature importance

---

## Next Steps

1. ✅ **Setup**: Complete (you're here!)
2. 📊 **Add Data**: Place CSV in `/data/`
3. 🤖 **Train Model**: Run `src/train_model.py`
4. 🧪 **Test Locally**: Run `streamlit run app/streamlit_app.py`
5. 🚀 **Deploy**: See `DEPLOYMENT.md`

---

## Support

For issues:
- Check `DEPLOYMENT.md` for deployment problems
- See `README.md` for project overview
- Review Streamlit docs: https://docs.streamlit.io

**Happy seeding! 🌱**

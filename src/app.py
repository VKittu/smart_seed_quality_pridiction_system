import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.express as px

# Load trained pipeline
pipeline_data = joblib.load("pipeline.pkl")
model = pipeline_data["model"]
label_encoder = pipeline_data["label_encoder"]

# Streamlit page setup
st.set_page_config(page_title="🌾 Seed Quality Predictor", layout="wide")
st.title("🌱 **Seed Quality Prediction System**")
st.markdown("### Predict whether a seed sample is **Good** or **Bad** based on its characteristics.")

st.sidebar.header("🧪 Input Seed Parameters")

# Sidebar sliders for input features
def get_user_input():
    moisture = st.sidebar.slider("Moisture (%)", 5.0, 20.0, 10.0)
    germination = st.sidebar.slider("Germination (%)", 50.0, 100.0, 85.0)
    purity = st.sidebar.slider("Purity (%)", 80.0, 100.0, 95.0)
    vigor_index = st.sidebar.slider("Vigor Index", 500, 2000, 1200)
    fungal_infestation = st.sidebar.slider("Fungal Infestation (%)", 0.0, 50.0, 5.0)
    discoloration = st.sidebar.slider("Discoloration (%)", 0.0, 40.0, 5.0)
    protein_content = st.sidebar.slider("Protein Content (%)", 10.0, 30.0, 20.0)
    oil_content = st.sidebar.slider("Oil Content (%)", 10.0, 40.0, 25.0)
    seed_age_days = st.sidebar.slider("Seed Age (days)", 0, 365, 60)
    seed_length = st.sidebar.slider("Seed Length (mm)", 2.0, 12.0, 5.5)
    seed_width = st.sidebar.slider("Seed Width (mm)", 1.0, 8.0, 3.0)

    data = {
        "moisture": moisture,
        "germination": germination,
        "purity": purity,
        "vigor_index": vigor_index,
        "fungal_infestation": fungal_infestation,
        "discoloration": discoloration,
        "protein_content": protein_content,
        "oil_content": oil_content,
        "seed_age_days": seed_age_days,
        "seed_length": seed_length,
        "seed_width": seed_width,
    }
    return pd.DataFrame([data])

input_df = get_user_input()

# Display input table
st.subheader("📋 Entered Parameters")
st.dataframe(input_df.style.set_properties(**{'background-color': '#f6fff8', 'color': '#000000'}))

# Predict button
if st.button("🔍 Predict Seed Quality"):
    prediction = model.predict(input_df)[0]
    prediction_label = label_encoder.inverse_transform([prediction])[0]
    confidence = np.max(model.predict_proba(input_df)) * 100

    # Explanation paragraphs
    if prediction_label == "Good":
        st.success(f"✅ **Seed Quality: GOOD** ({confidence:.2f}% confidence)")
        st.markdown(
            """
            🌾 These seeds are likely **high-quality** because they have:
            - High germination and purity levels  
            - Strong vigor index  
            - Low fungal infestation and discoloration  
            - Balanced moisture and good nutrient content (protein/oil)  

            Such seeds are **ideal for sowing**, offering better yield, germination rate, and resistance to diseases.
            """
        )
    else:
        st.error(f"❌ **Seed Quality: BAD** ({confidence:.2f}% confidence)")
        st.markdown(
            """
            ⚠️ These seeds appear **low-quality** mainly due to:
            - Low germination or purity levels  
            - High fungal infestation or discoloration  
            - Poor vigor index  
            - Unfavorable moisture or nutrient balance  

            Such seeds may result in **poor germination**, **low productivity**, and **increased susceptibility to disease**.
            """
        )

   # Feature importance visualization (only after prediction)
st.subheader("📊 Feature Importance")
try:
    importance_df = pd.read_csv("../data/feature_importance.csv").head(10)
    fig = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Top 10 Most Important Features",
        color="Importance",
        color_continuous_scale="Greens",
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, width='stretch')
except Exception as e:
    st.info("📈 Feature importance will appear after model prediction.")


st.markdown("---")
st.caption("Developed by **Vishal Dabi** 🌱 | Smart Seed Quality Prediction System")

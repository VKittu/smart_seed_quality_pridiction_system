# app/streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap

@st.cache_data
def load_pipeline(path="../src/pipeline.pkl"):
    obj = joblib.load(path)
    return obj['pipeline'], obj['meta']

pipeline, meta = load_pipeline()

st.set_page_config(page_title="Seed Quality Predictor", layout="wide")
st.title("Seed Quality Predictor — Physical & Biological Features")

st.markdown("Upload CSV or input a single sample. Prediction: **Good** / **Bad** with explanation using SHAP.")

domain_reason_map = {
    'germination': ("High germination rate -> good viability", "Low germination -> poor viability"),
    'moisture': ("Moisture in ideal range -> stable seeds", "High moisture -> risk of fungal growth"),
    'purity': ("High purity -> fewer contaminants", "Low purity -> more inert matter"),
    'fungal_infestation': ("Low infestation -> healthy", "High infestation -> diseased seeds"),
    'vigor_index': ("High vigor -> strong seedlings", "Low vigor -> weak seedlings"),
    'discoloration': ("Low discoloration -> healthy", "High discoloration -> disease/damage")
}

option = st.radio("Input method:", ["Upload CSV", "Manual single sample"])

if option == "Upload CSV":
    uploaded = st.file_uploader("Upload CSV", type=['csv'])
    if uploaded is not None:
        df = pd.read_csv(uploaded)
        st.write("Preview:")
        st.dataframe(df.head())
        if st.button("Run predictions"):
            X = df[meta['features']].copy()
            preds = pipeline.predict(X)
            proba = pipeline.predict_proba(X)[:,1]
            out = df.copy()
            out['pred_label'] = np.where(preds==1, 'Good', 'Bad')
            out['pred_proba'] = proba
            st.success("Predictions done")
            st.dataframe(out.head(100))
            st.download_button("Download predictions CSV", out.to_csv(index=False), file_name="predictions.csv")
else:
    st.subheader("Enter values (leave blank to use median/impute):")
    user_input = {}
    cols = st.columns(3)
    for i, f in enumerate(meta['features']):
        with cols[i % 3]:
            val = st.text_input(f"{f}:", value="")
            user_input[f] = val

    if st.button("Predict sample"):
        row = {}
        for f in meta['features']:
            v = user_input[f].strip()
            if v == "":
                row[f] = np.nan
            else:
                try:
                    row[f] = float(v)
                except:
                    row[f] = v
        X = pd.DataFrame([row])

        pred = pipeline.predict(X)[0]
        proba = pipeline.predict_proba(X)[0,1]
        label = "Good" if pred == 1 else "Bad"
        st.markdown(f"### Prediction: **{label}** (probability of Good = {proba:.3f})")

        # SHAP explanation
        try:
            preprocessor = pipeline.named_steps['preprocessor']
            model = pipeline.named_steps['classifier']
            X_trans = preprocessor.transform(X)
            explainer = shap.TreeExplainer(model)
            shap_vals = explainer.shap_values(X_trans)
            if isinstance(shap_vals, list):
                sv = shap_vals[1][0]
            else:
                sv = shap_vals[0][0]

            # build feature names after transform
            def get_feature_names(preprocessor):
                feature_names = []
                # numeric
                num_cols = preprocessor.transformers_[0][2]
                feature_names.extend(list(num_cols))
                # categorical onehot
                cat_transformer = preprocessor.transformers_[1][1]
                cat_cols = preprocessor.transformers_[1][2]
                if hasattr(cat_transformer.named_steps['onehot'], 'get_feature_names_out'):
                    cat_ohe = list(cat_transformer.named_steps['onehot'].get_feature_names_out(cat_cols))
                else:
                    cat_ohe = list(cat_cols)
                feature_names.extend(cat_ohe)
                return feature_names

            fname = get_feature_names(preprocessor)
            idx_sorted = np.argsort(np.abs(sv))[::-1][:6]
            rows = []
            for i in idx_sorted:
                name = fname[i] if i < len(fname) else f"f{i}"
                rows.append((name, float(sv[i])))

            st.write("Top SHAP features:")
            st.dataframe(pd.DataFrame(rows, columns=['feature','shap_value']))

            st.write("Human-readable reasons:")
            for feat, shap_v in rows:
                base = feat.split('_')[0].lower()
                if base in domain_reason_map:
                    pos, neg = domain_reason_map[base]
                    st.write(f"- {feat}: {pos if shap_v>0 else neg} (contribution {shap_v:.3f})")
                else:
                    st.write(f"- {feat}: {'increases Good' if shap_v>0 else 'increases Bad'} (contribution {shap_v:.3f})")

        except Exception as e:
            st.write("Explanation not available:", e)

        if pred == 1:
            st.success("Seed predicted as GOOD quality.")
        else:
            st.error("Seed predicted as BAD quality.")

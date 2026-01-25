import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

# ✅ Step 1: Load dataset
data_path = "../data/seeds.csv"  # make sure CSV is here
data = pd.read_csv(data_path)

print("✅ Dataset loaded successfully!")
print("Shape:", data.shape)
print("Columns:", list(data.columns))
print()

# ✅ Step 2: Encode target labels ('Good'/'Bad') into numeric form for model
target_col = "quality"
le = LabelEncoder()
data[target_col] = le.fit_transform(data[target_col])  # Good→1, Bad→0

# ✅ Step 3: Split data
X = data.drop(columns=[target_col])
y = data[target_col]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ✅ Step 4: Build pipeline
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        class_weight="balanced"
    ))
])

# ✅ Step 5: Train
model.fit(X_train, y_train)

# ✅ Step 6: Predict and evaluate
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Bad", "Good"]))
print("ROC AUC:", roc_auc_score(y_test, y_prob))

# ✅ Step 7: Cross-validation (no warning now)
cv_scores = cross_val_score(model, X, y, cv=5, scoring="f1")
print("5-fold CV F1 scores:", cv_scores)
print("Mean F1:", np.mean(cv_scores))

# ✅ Step 8: Save pipeline
joblib.dump({
    "model": model,
    "label_encoder": le
}, "pipeline.pkl")
print("\n✅ Model + label encoder saved as 'pipeline.pkl'")

# ✅ Step 9: Feature importance
importances = model.named_steps["classifier"].feature_importances_
importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

importance_df.to_csv("../data/feature_importance.csv", index=False)
print("✅ Feature importance saved as 'feature_importance.csv'")
# ✅ Confusion Matrix
# ✅ Confusion Matrix (Fixed Version)
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Convert encoded labels back to original for visualization
y_test_labels = le.inverse_transform(y_test)
y_pred_labels = le.inverse_transform(y_pred)

# Compute confusion matrix
cm = confusion_matrix(y_test_labels, y_pred_labels, labels=le.classes_)

# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le.classes_)
disp.plot(cmap='Greens')
plt.title("Confusion Matrix - Seed Quality Classification")
plt.savefig("confusion_matrix.png")  # Save as image file
plt.show()


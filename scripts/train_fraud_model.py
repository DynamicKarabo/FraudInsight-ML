import pandas as pd
import os
import sys

print("--- DEBUG START ---")
csv_path = 'data/creditcard.csv'

if not os.path.exists(csv_path):
    print(f"ERROR: Cannot find {csv_path}")
    sys.exit()

print("Step 1: Loading Data...")
try:
    df = pd.read_csv(csv_path)
    print(f"Success: Loaded {len(df)} rows.")
except Exception as e:
    print(f"ERROR during load: {e}")
    sys.exit()

# Only import heavy ML libs AFTER confirming data exists
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
import joblib

print("Step 2: Defining Pipeline...")
X = df.drop('Class', axis=1)
y = df['Class']

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('sampling', SMOTE(random_state=42)),
    ('classifier', RandomForestClassifier(n_estimators=10, max_depth=5, n_jobs=-1))
])

print("Step 3: Training (Reduced size for testing)...")
pipeline.fit(X[:10000], y[:10000]) 

print("Step 4: Saving...")
dest = 'dashboard/ml_assets/fraud_model.pkl'
joblib.dump(pipeline, dest)

if os.path.exists(dest):
    print(f"--- COMPLETE: File created at {dest} ---")
else:
    print("--- FAILED: File was not created ---")
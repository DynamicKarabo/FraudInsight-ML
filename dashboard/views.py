import os
import joblib
import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def dashboard_view(request):
    """Renders the main dashboard page"""
    return render(request, 'dashboard/dashboard.html')

def predict_fraud(request):
    """Handles AI inference and keeps the 'Time' feature"""
    try:
        # 1. Setup absolute paths
        model_path = os.path.join(settings.BASE_DIR, 'dashboard', 'ml_assets', 'fraud_model.pkl')
        csv_path = os.path.join(settings.BASE_DIR, 'data', 'creditcard.csv')

        # 2. Verify files exist
        if not os.path.exists(model_path) or not os.path.exists(csv_path):
            return JsonResponse({'error': 'Required ML files not found'}, status=500)

        # 3. Load model and data
        model = joblib.load(model_path)
        df = pd.read_csv(csv_path)
        
        # 4. Sample a transaction
        sample = df.sample(1)
        
        # 5. FIX: Only drop 'Class'. We MUST keep 'Time' for this specific model
        features = sample.drop(['Class'], axis=1)

        # 6. Run Model
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]
        amount = sample['Amount'].values[0]

        return JsonResponse({
            'prediction': 'Fraud' if int(prediction) == 1 else 'Clear',
            'probability': float(probability),
            'amount': float(amount)
        })
        
    except Exception as e:
        # Prints specific errors to your terminal for debugging
        print(f"--- SERVER ERROR: {str(e)} ---")
        return JsonResponse({'error': str(e)}, status=500)
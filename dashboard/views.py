from django.shortcuts import render
from django.http import JsonResponse
from .services import FraudModelService
import random

def home(request):
    return render(request, 'dashboard/home.html')

def predict_fraud(request):
    """API that returns a prediction. Includes logic to force fraud 20% of the time for demos."""
    df = FraudModelService.get_data()
    
    # 20% chance to force-fetch a fraudulent transaction for the demo
    if random.random() < 0.20:
        fraud_rows = df[df['Class'] == 1]
        row = fraud_rows.sample(n=1).iloc[0]
        features = row.drop('Class').values.tolist()
        actual_class = 1
    else:
        features, actual_class = FraudModelService.get_random_transaction()
    
    result = FraudModelService.predict(features)
    
    return JsonResponse({
        'status': 'success',
        'prediction': result,
        'actual_class': actual_class,
        'features_preview': features[:3]
    })
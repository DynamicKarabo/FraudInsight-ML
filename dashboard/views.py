from django.shortcuts import render
from django.http import JsonResponse
from .services import FraudModelService

def home(request):
    """Renders the main dashboard page."""
    return render(request, 'dashboard/home.html')

def predict_fraud(request):
    """API endpoint that returns a prediction for a random transaction."""
    features, actual_class = FraudModelService.get_random_transaction()
    result = FraudModelService.predict(features)
    
    return JsonResponse({
        'status': 'success',
        'prediction': result,
        'actual_class': actual_class,
        'features_preview': features[:3] # Just for debugging
    })
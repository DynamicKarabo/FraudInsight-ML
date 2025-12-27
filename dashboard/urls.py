from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test-predict/', views.predict_fraud, name='test_predict'),
]
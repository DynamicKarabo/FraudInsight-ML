import joblib
import os
import numpy as np
import pandas as pd
import random
from django.conf import settings

class FraudModelService:
    _model = None
    _df = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            model_path = os.path.join(settings.BASE_DIR, 'dashboard', 'ml_assets', 'fraud_model.pkl')
            cls._model = joblib.load(model_path)
        return cls._model

    @classmethod
    def get_data(cls):
        """Loads the CSV once to save memory."""
        if cls._df is None:
            csv_path = os.path.join(settings.BASE_DIR, 'data', 'creditcard.csv')
            cls._df = pd.read_csv(csv_path)
        return cls._df

    @classmethod
    def get_random_transaction(cls):
        df = cls.get_data()
        random_index = random.randint(0, len(df) - 1)
        row = df.iloc[random_index]
        
        # 'Class' is the last column (0 for legit, 1 for fraud)
        features = row.drop('Class').values.tolist()
        actual_class = int(row['Class'])
        return features, actual_class

    @classmethod
    def predict(cls, features):
        model = cls.get_model()
        input_data = np.array(features).reshape(1, -1)
        
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        
        return {
            'is_fraud': int(prediction),
            'probability': round(float(probability) * 100, 2)
        }
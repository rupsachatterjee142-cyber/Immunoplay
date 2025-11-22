# test_predictor.py

import pandas as pd
from src.predictor import train_model, predict_risk

def test_model_accuracy():
    model = train_model('data/sample_habits.csv')
    sample_input = pd.DataFrame([{
        'sleep_hours': 7,
        'exercise_minutes': 30,
        'junk_food_intake': 2,
        'hydration_liters': 2.0,
        'stress_level': 3
    }])
    prediction = predict_risk(model, sample_input)
    assert prediction in ['Low', 'Medium', 'High']

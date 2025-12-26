# predictor.py
import pandas as pd

def predict_risk(sample_input):
    """
    Simulates a biological risk assessment based on urban lifestyle.
    """
    # Extracting inputs from the user data
    sleep = sample_input['sleep_hours'].iloc[0]
    stress = sample_input['stress_level'].iloc[0]
    junk_food = sample_input['junk_food_intake'].iloc[0]
    exercise = sample_input['exercise_minutes'].iloc[0]

    # BIOLOGICAL LOGIC:
    # 1. Sleep deprivation (<7h) reduces Natural Killer (NK) cell activity.
    # 2. High Stress (Scale 1-10) triggers Cortisol release, suppressing T-cells.
    # 3. Junk Food increases systemic inflammation.
    # 4. Exercise helps in lymphatic drainage and immune circulation.
    
    # Weighted calculation for a 'Bio-Immunity Index'
    score = (sleep * 10) + (exercise * 0.5) - (stress * 8) - (junk_food * 4)
    
    if score > 80:
        return 'Low Risk'
    elif 50 <= score <= 80:
        return 'Medium Risk'
    else:
        return 'High Risk'

def train_model(data_path):
    # For now, this returns a placeholder as we are using a 
    # rule-based biological model to simulate the prediction.
    return "Biological Logic Engine Active"

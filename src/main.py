# main.py

import pandas as pd
from predictor import train_model, predict_risk
from gamify import calculate_score, feedback_message

# Sample user habit input (you can later replace this with dynamic input)
user_habits = {
    'sleep_hours': 6,
    'exercise_minutes': 20,
    'junk_food_intake': 3,
    'hydration_liters': 1.5,
    'stress_level': 4
}

# Convert to DataFrame for ML prediction
user_df = pd.DataFrame([{
    'sleep_hours': user_habits['sleep_hours'],
    'exercise_minutes': user_habits['exercise_minutes'],
    'junk_food_intake': user_habits['junk_food_intake'],
    'hydration_liters': user_habits['hydration_liters'],
    'stress_level': user_habits['stress_level']
}])

# Train model using sample dataset
model = train_model('data/sample_habits.csv')  # Make sure this file exists

# Predict health risk
risk = predict_risk(model, user_df)

# Calculate immunity score
score = calculate_score(user_habits)

# Get feedback message
message = feedback_message(score)

# Display results
print(f"Immunity Score: {score}")
print(f"Feedback: {message}")
print(f"Predicted Health Risk Level: {risk}")

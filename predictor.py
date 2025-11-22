# predictor.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(data_path):
    # Load dataset
    df = pd.read_csv(data_path)

    # Assume dataset has 'habits' as features and 'risk' as target
    X = df.drop('risk', axis=1)
    y = df['risk']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    return model

def predict_risk(model, user_input):
    # user_input should be a DataFrame with same structure as training features
    prediction = model.predict(user_input)
    return prediction[0]

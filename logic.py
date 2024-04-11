# Import libraries
from model import DataModel
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

def calculate_result(BMI, Smoking, PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory, Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, SkinCancer):
    # Load the model
    model2 = GradientBoostingClassifier()
    X_train = pd.read_csv('X_train.csv', encoding='utf-8')
    y_train = pd.read_csv('y_train.csv', encoding='utf-8')
    model2.fit(X_train, y_train)

    # Prepare the input data
    sample = pd.DataFrame([[BMI, Smoking, PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory, Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, SkinCancer]],
                          columns=['BMI', 'Smoking', 'PhysicalHealth', 'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime', 'Asthma', 'SkinCancer'])

    # Predict probabilities
    probabilities = model2.predict_proba(sample)[0]
    percentage = probabilities[1] * 100
    result = f"{percentage:.2f}%"

    # Return only the result and percentage
    return result, percentage

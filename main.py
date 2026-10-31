from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Trained model ko load karte hain
model = joblib.load('fraud_model.pkl')

# Request body define karte hain
class Transaction(BaseModel):
    amount: float
    hour: int
    frequency: int
    distance_from_home: float

@app.post("/predict")
def predict_fraud(txn: Transaction):
    # Data ko dataframe me convert karte hain
    df = pd.DataFrame([[txn.amount, txn.hour, txn.frequency, txn.distance_from_home]], 
                        columns=['amount', 'hour', 'frequency', 'distance_from_home'])
    
    # Model se prediction nikalte hain (-1 matlab fraud/anomaly, 1 matlab normal)
    prediction = model.predict(df)[0]
    score = model.decision_function(df)[0]
    
    is_fraud = True if prediction == -1 else False
    
    # Bonus twist: Explainable reason dena
    reason = "Transaction normal hai aur secure lag rahi hai."
    if is_fraud:
        reason = "Suspicious: Amount bohot zyada hai ya unusual timing/distance par transaction ho rahi hai!"
        
    return {
        "is_fraud": is_fraud,
        "anomaly_score": float(score),
        "reason": reason
    }
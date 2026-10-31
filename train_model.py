import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

# Step 1: Chhota sa synthetic transaction dataset banate hain
np.random.seed(42)
n_samples = 1000

data = {
    'amount': np.random.exponential(scale=1000, size=n_samples),
    'hour': np.random.randint(0, 24, size=n_samples),  # Yahan theek kar diya hai (np.random.randint)
    'frequency': np.random.poisson(lam=2, size=n_samples),
    'distance_from_home': np.random.exponential(scale=5, size=n_samples)
}

df = pd.DataFrame(data)

# Step 2: Isolation Forest model train karte hain
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df[['amount', 'hour', 'frequency', 'distance_from_home']])

# Step 3: Trained model ko save kar lete hain
joblib.dump(model, 'fraud_model.pkl')
print("Model successfully train ho gaya aur 'fraud_model.pkl' ke naam se save ho gaya!")
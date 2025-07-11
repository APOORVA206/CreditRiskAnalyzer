import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np
import os


X = np.array([
    [25, 30000, 5000],     
    [40, 60000, 15000],    
    [35, 45000, 12000],    
    [50, 80000, 20000],    
    [30, 40000, 8000],    
    [22, 15000, 50000],    
    [21, 12000, 60000],    
    [28, 20000, 40000],    
    [32, 35000, 10000],    
    [45, 55000, 7000]      
])
y = np.array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0])  
# Save trained model
os.makedirs("model", exist_ok=True)
model = LogisticRegression()
model.fit(X, y)
joblib.dump(model, "model/credit_model.pkl")

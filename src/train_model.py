import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load dataset
df = pd.read_csv("data/traffic.csv")

# Convert date
df['date_time'] = pd.to_datetime(df['date_time'], dayfirst=True)
# Feature engineering
df['hour'] = df['date_time'].dt.hour
df['day'] = df['date_time'].dt.dayofweek
df['month'] = df['date_time'].dt.month

# Select features
X = df[['hour','day','month','temp']]
y = df['traffic_volume']

# Split data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# Train model
model = RandomForestRegressor()
model.fit(X_train,y_train)

# Save model
pickle.dump(model,open("models/traffic_model.pkl","wb"))

print("Model trained successfully")
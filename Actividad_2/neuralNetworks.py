import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import time

df = pd.read_csv("Mall_Customers_Enhanced.csv")

df['Gender'] = df['Gender'].fillna(np.random.choice(['Male', 'Female']))

# Eliminar categorias innecesarias
df_cleaned = df.drop(['CustomerID', 'Age Group', 'Loyalty Years', 'Credit Score'], axis=1)

# Eliminar las filas que no contengan una Categoria Preferida para no sesgar un poco el entrenamiento
df_cleaned = df_cleaned.dropna(subset=['Preferred Category'])

label_encoders = {}
category_cols = ['Gender', 'Preferred Category']

inicio = time.time()

for col in category_cols:
    le = LabelEncoder()
    df_cleaned[col] = le.fit_transform(df_cleaned[col])
    label_encoders[col] = le
    
    print(f"Codificacion para {col}:")
    for i, class_ in enumerate(le.classes_):
        print(f"{class_} = {i}")


X = df_cleaned.drop(['Preferred Category'], axis=1)
y = df_cleaned['Preferred Category']

scaler = StandardScaler()
cols = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Estimated Savings (k$)']

X[cols] = scaler.fit_transform(X[cols])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(16, activation='relu'),
    Dropout(0.3),
    Dense(8, activation='relu'),
    Dense(len(np.unique(y)), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.summary()

history = model.fit(X, y, epochs=120)

y_pred_probs = model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)


accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión total: {accuracy:.4f}")


def predict_category(gender, age, annual_income, spending_score=50, estimated_savings=10):
    
    # Preparar datos de entrada
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Age': [age],
        'Annual Income (k$)': [annual_income],
        'Spending Score (1-100)': [spending_score],
        'Estimated Savings (k$)': [estimated_savings],
    })
    
    # Codificar genero
    input_data['Gender'] = label_encoders['Gender'].transform(input_data['Gender'])
    
    # Normalizar
    input_data[cols] = scaler.transform(input_data[cols])
    
    # Predecir
    prediction_encoded = model.predict(input_data)
    prediction = np.argmax(prediction_encoded, axis=1)
    
    # Decodificar la predicción
    categoria_predicha = label_encoders['Preferred Category'].inverse_transform(prediction)
    
    return categoria_predicha[0]

test = [
    ["Female",47,120,16,36-50,107.2,850,5],   # Electronics
    ["Female",35,120,79,26-35,56.8,850,7],    # Luxury
    ["Female",45,126,28,36-50,102.48,850,5],  # Electronics
    ["Male",32,126,74,26-35,63.84,850,6]      # Luxury
]

for i in test:
    catergory = predict_category(gender=i[0], age=i[1], annual_income=i[2], spending_score=i[3], estimated_savings=i[4])
    
    print(catergory)

final = time.time()

print(final-inicio)
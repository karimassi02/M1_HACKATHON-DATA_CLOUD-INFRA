import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np


def preprocess_data(data):
    # Transforme l'entrée en un vecteur de la bonne taille (remplace cette ligne par le bon preprocessing)
    features = np.zeros(118)  # Crée un vecteur de 118 zéros
    features[0] = data.port_source
    features[1] = data.port_destination
    features[2] = data.duree
    # Ajoute ici le reste des transformations selon ton dataset d'entraînement
    return features.reshape(1, -1)  # Retourne sous forme d'un tableau 2D



# Charger le modèle pré-entraîné
model = joblib.load("ml_model.pkl")

# Définition de l'API FastAPI
app = FastAPI()

# Modèle de données d'entrée
class ConnectionData(BaseModel):
    ip_source: str
    port_source: int
    ip_destination: str
    port_destination: int
    protocole: str
    duree: float

# Fonction pour effectuer la prédiction
def detect_anomaly(data):
    features = preprocess_data(data)  # Transforme l'entrée
    prediction = model.predict(features)  # Fait la prédiction
    return {"is_anomalous": bool(prediction[0])}

# Route pour analyser une connexion réseau
@app.post("/send_connexion")
async def analyze_connexion(data: ConnectionData):
    result = detect_anomaly(data)
    return {
        "ip_source": data.ip_source,
        "port_source": data.port_source,
        "ip_destination": data.ip_destination,
        "port_destination": data.port_destination,
        "alert": result
    }


try:
    model = joblib.load("ml_model.pkl")
    print("✅ Modèle chargé avec succès :", type(model))  # Vérifie le type du modèle
except Exception as e:
    print(f"❌ Erreur lors du chargement du modèle : {e}")

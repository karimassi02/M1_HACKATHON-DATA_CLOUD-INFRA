import gradio as gr
import requests
import os
API_URL = os.getenv("BACKEND_URL", "http://backend:8000/send_connexion")


# Fonction qui envoie les données à FastAPI et récupère le résultat
def analyze_connection(ip_source, port_source, ip_destination, port_destination, protocole, duree):
    data = {
        "ip_source": ip_source,
        "port_source": int(port_source),
        "ip_destination": ip_destination,
        "port_destination": int(port_destination),
        "protocole": protocole,
        "duree": float(duree),
    }
    
    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Échec de l'analyse"}

# Interface Gradio
iface = gr.Interface(
    fn=analyze_connection,
    inputs=[
        gr.Textbox(label="IP Source"),
        gr.Number(label="Port Source"),
        gr.Textbox(label="IP Destination"),
        gr.Number(label="Port Destination"),
        gr.Dropdown(["TCP", "UDP", "ICMP"], label="Protocole"),
        gr.Number(label="Durée (s)"),
    ],
    outputs="json",
    title="🔍 Analyse des Connexions Réseau",
    description="Entrez une connexion réseau et obtenez une analyse d'anomalie en temps réel."
)

iface.launch(server_name="0.0.0.0", server_port=7860)

import streamlit as st
import requests

st.title('Credit Scoring Interface')  # Title of the web app
 
#Initialize session state and save prediction result
#if 'prediction' not in st.session_state:
 #   st.session_state.prediction = None




with st.form('infos client'):
    identifiant = st.text_input('identifiant')
    amount = st.text_input('montant')
    price = st.text_input('taux')
    submit = st.form_submit_button('Prédire')

# Prediction : st.button("Prédire") = True when clicked
if submit:

    data = {
        "Id": identifiant,
        "amount": amount,
        "price": price
    }

    st.write(data)
    # Prediction
        
        
    response = requests.post('http://serving-api:8080/predict', json= data, auth=('user', 'pass'))
    if response.status_code == 200:  # no error in the request
        st.session_state.prediction = response.json()
        prediction=st.session_state.prediction
        st.write("Voici la prédiction : ", prediction)
    else :
        st.write("Erreur dans la requête de prédiction")


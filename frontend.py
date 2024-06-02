import streamlit as st
import requests 
import json
import time

url = 'http://localhost:8000/predict'
st.title(":blue[Water Potability Tester] :potable_water:")


# def neg_pred():
#     for word in 'Not fit for drinking'.split(' '):
#         yield word + ' '
#         time.sleep(0.05)

# def pos_pred():
#     for word in 'Fit for drinking'.split(' '):
#         yield word + ' '
#         time.sleep(0.05)


with st.form("my_form"):
    ph = st.text_input("pH")
    hardness = st.text_input('Hardness')
    solids = st.text_input('Solids')
    chloramines =st.text_input('Chloramines')
    sulphates = st.text_input('Sulfate')
    conductivity = st.text_input('Conductivity')
    organic_carbon = st.text_input('Organic_carbon')
    trihalomethanes = st.text_input('Trihalomethanes')
    turbidity = st.text_input('Turbidity')

    if st.form_submit_button(use_container_width=True):
        for x in [ph, hardness, solids, chloramines, sulphates, conductivity,
                  sulphates, conductivity, organic_carbon, trihalomethanes, turbidity]:
            if not x:
                st.write(':red[Fill all the values]')
                break
        else:
            data = json.dumps({
                "ph": float(ph),
                "Hardness": float(hardness),
                "Solids": float(solids),
                "Chloramines": float(chloramines),
                "Sulfate": float(sulphates),
                "Conductivity": float(conductivity),
                "Organic_carbon": float(organic_carbon),
                "Trihalomethanes": float(trihalomethanes),
                "Turbidity": float(turbidity)
            }, indent=2)
            response = requests.post(url, data, headers={
                'Content-Type': 'application/json'
            })

            if response.json()['result'] == '0':
                st.markdown('### :red[Not fit for drinking]')
            else:
                st.markdown('### :green[Fit for drinking]')

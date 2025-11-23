import streamlit as st
#para runear: streamlit run app_clase.py
#título de la app
st.title("Aplicación de Saludo")

nombre = st.text_input("Ingresa tu nombre: ")

if nombre:
    st.write(f"hola, {nombre}! ¡Bienvendio a streamlit!")
    st.success(f"ENcantado, {nombre}")
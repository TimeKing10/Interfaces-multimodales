import streamlit as st
from PIL import Image
st.title("La onda")
st.header("Cabeza")
image = Image.open('roca.jpg')
st.image(image, width=200)

texto = st.text_input('que onda', 'que mas')
st.write(texto)

st.subheadder('dos columnas')

col1, col2 = st.columns(2)

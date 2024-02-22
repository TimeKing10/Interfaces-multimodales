import streamlit as st
from PIL import Image
st.title("La onda")
st.header("Cabeza")
image = Image.open('roca.jpg')
st.image(image, width=200)

texto = st.text_input('que onda', 'que mas')
st.write(texto)

st.subheader('dos columnas')

col1, col2 = st.columns(2)

with col1:
  st.subheader('Palo1')
  st.write('7u7')
  resp = st.checkbox("Verifica el texto")
  if resp:
    st.write('Correcto')

with col2:
  st.subheader('Palo2')
  modo = st.radio('Hola',('banana','...'))
  if modo == 'banana':
    st.write('BANANAAAA!!!')
  if modo == '...':
    st.write('mmmmm')

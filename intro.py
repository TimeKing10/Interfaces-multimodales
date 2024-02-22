import streamlit as st
from PIL import Image
st.title("La onda")
st.header("Cabeza")
image = Image.open('roca.jpg')
st.image(image, width=200)

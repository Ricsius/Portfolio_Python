import streamlit as st
import PIL
import PIL.Image

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    with PIL.Image.open("images/photo.png") as image:
        image = image = PIL.ImageOps.exif_transpose(image)
        st.image(image)

with col2:
    st.title("Hajnal Richárd")

    content = """
Hi, I am Richárd! I am a software developer.
I am currently learning Python programming. 
On this website, you can see my Python projects.
"""
    st.info(content)
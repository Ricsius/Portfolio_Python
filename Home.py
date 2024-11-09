import streamlit as st
import PIL
import PIL.Image
import pandas

TITLE_KEY = "title"
DESCRIPTION_KEY = "description"
IMAGE_KEY = "image"
URL_KEY = "url"

def render_project_info(info):
    st.header(info[TITLE_KEY])
    st.write(info[DESCRIPTION_KEY])
    st.image(f"images/{info[IMAGE_KEY]}")
    st.write(f"[Source Code]({info[URL_KEY]})")

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

st.write("Below you can find some of the apps I have built. Feel free to contact me!")

data = pandas.read_csv("data.csv", sep=";")
column_element_count = int(len(data) / 2)
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in data[:column_element_count].iterrows():
        render_project_info(row)

with col4:
    for index, row in data[column_element_count:].iterrows():
        render_project_info(row)
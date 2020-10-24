import streamlit as st
from classfier import classify
from PIL import Image
import time
import os


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.title("Malaria Cell Classifier")
st.header("Predict if cell is Infected with Malaria or Uninfected")
st.text("Upload a cell image for classification")

uploaded_file = st.file_uploader("Choose cell image...")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded cell image", use_column_width=False, width=500)
    st.write("")
    st.write("**Classifying image...**")
    
    data = classify(image)

    if  data['infected'] == 1:
        st.error(f"Cell is **infected** with **Probability** of **{data['probability']}**")
    else:
        st.success(f"Cell is **uninfected** with **Probability** of **{ data['probability'] }**")

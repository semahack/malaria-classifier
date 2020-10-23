import streamlit as st
from classfier import classify
from PIL import Image
import time
import boto3
import botocore
import


s3 = boto3.resource("s3")

try:
    s3.Bucket(os.environ['BUCKET_NAME']).download_file(os.environ['MODEL_NAME'], 'Malaria_predictor.h5')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise


st.title("Malaria Cell Classifier")
st.header("Predict if cell is Infected with Malaria or Uninfected")
st.text("Upload a cell image for classification")

uploaded_file = st.file_uploader("Choose cell image...")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded cell image", use_column_width=False)
    st.write("")
    st.write("**Classifying image...**")
    my_bar = st.progress(0)
    for p_c in range(100):
        time.sleep(0.01)
        my_bar.progress(p_c + 1)

    data = classify(image)

    if  data['infected'] == 1:
        st.error(f"Cell is **infected** with **Probability** of **{data['probability']}**")
    else:
        st.success(f"Cell is **uninfected** with **Probability** of **{ data['probability'] }**")

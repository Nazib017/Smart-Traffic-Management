import streamlit as st

st.set_page_config(page_title="Smart Traffic System", layout="wide")

import numpy as np
from ultralytics import YOLO
from PIL import Image
import time

from utils import calculate_density, get_congestion_level, get_signal

@st.cache_resource
def load_model():
    return YOLO("model/best.pt")

model = load_model()

st.title("🚦 Smart Traffic Signal System")

uploaded_file = st.file_uploader("Upload Traffic Image", type=["jpg","png","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img = np.array(image)

    result = model(img)[0]
    annotated = result.plot()

    score = calculate_density(result, img)
    level = get_congestion_level(score)
    signal, timer = get_signal(level)

    col1, col2 = st.columns(2)

    with col1:
        st.image(annotated)

    with col2:
        st.write("### Congestion Level:", level)
        st.write("### Score:", round(score,2))

        if signal == "GREEN":
            st.success("GREEN 🟢")
        elif signal == "YELLOW":
            st.warning("YELLOW 🟡")
        else:
            st.error("RED 🔴")

        placeholder = st.empty()
        for i in range(timer,0,-1):
            placeholder.metric("Time Remaining", f"{i} sec")
            time.sleep(1)
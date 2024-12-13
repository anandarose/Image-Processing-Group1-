import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

# App title
st.title("Advanced Image Processing App (No OpenCV)")
st.write("Upload an image and apply various transformations.")

# File uploader
uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Load the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Sidebar options
    st.sidebar.title("Processing Options")

    # Apply blur
    blur_amount = st.sidebar.slider("Blur", 0, 10, 0)
    if blur_amount > 0:
        image = image.filter(ImageFilter.GaussianBlur(blur_amount))

    # Rotate image
    rotate_angle = st.sidebar.slider("Rotate (degrees)", 0, 360, 0)
    if rotate_angle > 0:
        image = image.rotate(rotate_angle, expand=True)

    # Adjust contrast
    contrast_factor = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0)
    if contrast_factor != 1.0:
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast_factor)

    # Display the processed image
    st.image(image, caption="Processed Image", use_column_width=True)

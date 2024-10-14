import streamlit as st
import boto3
import json
from PIL import Image
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np

# Define your SageMaker endpoint and model component
endpoint_name = 'jumpstart-dft-stable-diffusion-v2-1-20241014-162250'
inference_component = 'model-txt2img-stabilityai-stable-diffusion-v2-1-20241014-162253'

# Function to query the SageMaker endpoint
def query_endpoint(prompt):
    client = boto3.client('runtime.sagemaker')
    
    # Define the payload with the prompt and other parameters
    payload = {
        "prompt": prompt, 
        "width": 512, 
        "height": 512, 
        "num_images_per_prompt": 1, 
        "num_inference_steps": 50, 
        "guidance_scale": 7.5
    }

    # Query the endpoint
    response = client.invoke_endpoint(
        EndpointName=endpoint_name, 
        InferenceComponentName=inference_component, 
        ContentType='application/json', 
        Body=json.dumps(payload).encode('utf-8'),
        Accept='application/json;jpeg'
    )
    
    return response

# Function to parse the response
def parse_response(query_response):
    response_dict = json.loads(query_response['Body'].read())
    generated_images = response_dict['generated_images']
    prompt = response_dict['prompt']
    
    images = []
    for generated_image in generated_images:
        # Convert base64 to image
        image_decoded = BytesIO(base64.b64decode(generated_image.encode()))
        image = Image.open(image_decoded).convert("RGB")
        images.append(image)
    
    return images, prompt

# Function to display the image using matplotlib
def display_image(img, prmpt):
    plt.figure(figsize=(12,12))
    plt.imshow(np.array(img))
    plt.axis('off')
    plt.title(prmpt)
    st.pyplot(plt)

# Streamlit UI
st.title("Interior Design using AI")

# Dropdowns for Area/Room and Style
room = st.selectbox(
    "Select Area/Room", 
    ['Bedroom', 'Drawing Room', 'Basement', 'Sitting Room', 'Washroom', 'Conference Room', 'Office'], 
    key="room_selectbox"
)

style = st.selectbox(
    "Select Style", 
    ['Modern', 'Minimalist', 'Scandinavian', 'Industrial', 'Mid-Century Modern', 'Art Deco', 'Craftsman', 'Rustic', 'Shabby Chic', 'Bohemian'], 
    key="style_selectbox"
)

# Input for custom prompt or default prompt
use_custom_prompt = st.checkbox("Use custom prompt")
if use_custom_prompt:
    prompt = st.text_input("Enter your custom prompt", "", key="custom_prompt_input")
else:
    prompt = f"A {style} {room}"

# When the user clicks "Generate Image"
if st.button("Generate Image", key="generate_image_button"):
    with st.spinner('Generating image...'):
        # Query the SageMaker endpoint with the prompt
        response = query_endpoint(prompt)

        # Parse the response to get the generated images and prompt
        generated_images, prmpt = parse_response(response)

        # Display the image(s)
        for img in generated_images:
            st.write(f"Generated Image for: {prmpt}")
            display_image(img, prmpt)

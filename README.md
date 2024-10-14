# Interior Design AI Generator with Stable Diffusion

This project enables users to generate interior design images based on room types and styles using an AI-powered Stable Diffusion model deployed via AWS SageMaker.

## Features
- Generate images based on room type (e.g., Bedroom, Office) and style (e.g., Modern, Minimalist).
- Custom prompt option available.
- Built with Streamlit for the user interface and AWS SageMaker for model inference.

## Table of Contents
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Running the Application](#running-the-application)
- [Credits](#credits)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/interior-design-ai-generator.git
    cd interior-design-ai-generator
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Setup

### AWS SageMaker Setup

1. Make sure to deploy the **Stable Diffusion model** via AWS SageMaker. You can use AWS JumpStart for deploying the `Stable Diffusion v2-1` model.

2. Note down your **SageMaker Endpoint Name** and **Inference Component Name**.

### Streamlit Application

1. In the `app.py` file, update the following:
    ```python
    endpoint_name = 'your-endpoint-name'
    inference_component = 'your-inference-component-name'
    ```

### AWS Credentials

Make sure your AWS credentials (`access_key`, `secret_key`, and `region`) are configured through environment variables or in your AWS CLI profile.

## Usage

Once everything is set up, you can start the app and begin generating AI-generated interior designs.

- **Room Types**: Bedroom, Office, Conference Room, etc.
- **Styles**: Modern, Minimalist, Scandinavian, etc.
- **Custom Prompts**: Option to override the dropdown-generated prompt.

### Example Prompts

- **Generated Prompt**: `"A Modern Bedroom"`
- **Custom Prompt**: `"A futuristic bedroom with ambient lighting"`

## Running the Application

1. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

2. **Access the Web Interface**:
    - Open your browser and go to `http://localhost:8501`.
    - Select the room type and style, or enter a custom prompt.
    - Click **Generate Image** to generate an image using the Stable Diffusion model.

## Sample Output

![Sample Generated Image](link_to_your_image.png)

## Credits

- **Stable Diffusion Model**: [StabilityAI's Stable Diffusion](https://stability.ai/)
- **UI Framework**: [Streamlit](https://streamlit.io/)
- **Model Deployment**: [AWS SageMaker](https://aws.amazon.com/sagemaker/)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

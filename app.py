import gradio as gr
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/openai-gpt"
API_TOKEN = os.environ.get("API_TOKEN")

headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Function to translate code using the Hugging Face model API
# Function to translate code using the Hugging Face model API
# Function to translate code using the Hugging Face model API
def translate_code(input_text, source_lang, target_lang):
    payload = {
        "inputs": f"convert the below {source_lang} code to {target_lang} code: {input_text}"
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    response_data = response.json()  # Store the entire response for inspection
    print("API Response:", response_data)  # Print the response for inspection
    
    # Extract the translated code from the response
    translated_code = "No translation available"  # Default value
    
    if response_data:
        if isinstance(response_data, list) and len(response_data) > 0:
            translated_code = response_data[0].get("generated_text", "").strip()
    
    return translated_code



# Interface for the Gradio app
iface = gr.Interface(
    fn=translate_code,
    inputs=[
        gr.inputs.Textbox(label="Enter code to translate"),
        gr.inputs.Textbox(label="Source Language (e.g., English)"),
        gr.inputs.Textbox(label="Target Language (e.g., German)")
    ],
    outputs=gr.outputs.Textbox(label="Translated Code"),
    title="Code Translator",
    description="Translate code snippets between programming languages"
)

# Launch the Gradio app
iface.launch()

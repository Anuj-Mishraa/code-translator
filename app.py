import openai
import gradio as gr


def translate_code(api_key, input_text, source_lang, target_lang):
    prompt = f"Convert the following {source_lang} code to {target_lang} code:\n{input_text}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        api_key=api_key
    )
    
    translated_code = response.choices[0].text.strip()
    return translated_code

iface = gr.Interface(
    fn=translate_code,
    inputs=[
        gr.inputs.Textbox(label="Enter Your OPENAI API KEY"),
        gr.inputs.Textbox(label="Enter code to translate"),
        gr.inputs.Textbox(label="Source Language (e.g., C++,python,java...)"),
        gr.inputs.Textbox(label="Target Language (e.g., C++,python,java...)")
    ],
    outputs=gr.outputs.Textbox(label="Translated Code"),
    title="Code Translator",
    description="Translate code snippets between programming languages"
)

iface.launch()

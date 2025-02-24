import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

def chat_with_openai(prompt):
    try:
        system_message = "Contesta la siguiente pregunta: "
        prompts = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        completion = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=prompts,
        temperature=0.5
)
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Interfaz de Gradio
demo = gr.Interface(
    fn=chat_with_openai,
    inputs=gr.Textbox(label="Escribe tu pregunta"),
    outputs=gr.Textbox(label="Respuesta de GPT-4"),
    title="Chat con OpenAI",
    description="Escribe una pregunta y obtén una respuesta de OpenAI."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)


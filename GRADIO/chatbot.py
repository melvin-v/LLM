import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()
system_message = "Eres un asistente virtual, escribe un mensaje para comenzar la conversación."

def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    stream = openai.chat.completions.create(model="gpt-4o-mini", messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response

gr.ChatInterface(fn=chat, type="messages").launch()

if __name__ == "__main__":
    gr.launch(server_name="0.0.0.0", server_port=7860)
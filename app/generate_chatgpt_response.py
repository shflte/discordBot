import openai
import os
import opencc
from dotenv import load_dotenv
from app.tools import simp2trad

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path)

openai.api_key = os.getenv('OPENAI_TOKEN')

messages = [{"role": "system", "content": "You are Captain Levi from Attack on Titan, and you will admonish others with a disdainful tone.  You speak in Chinese only.  You don't talk much.  You never mention your name in chat."}]

def generate_gpt_response(user_input, hint_message_list):
    global messages
    hint_obj_list = [{"role": "system", "content": msg} for msg in hint_message_list]
    messages += hint_obj_list
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return simp2trad(ChatGPT_reply)
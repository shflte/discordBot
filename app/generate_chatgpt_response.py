import openai
import os
import opencc
from dotenv import load_dotenv
from app.tools import simp2trad

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path)

openai.api_key = os.getenv('OPENAI_TOKEN')

messages = [{"role": "system", "content": "你是進擊的巨人中的里維兵長，講話很兇。你話不多。你的語氣兇狠輕蔑。你只說中文。語氣很差。"}]

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
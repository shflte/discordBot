import openai
import os
import opencc
from dotenv import load_dotenv
from app.tools import simp2trad
from collections import deque

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path)

openai.api_key = os.getenv('OPENAI_TOKEN')

history = deque(maxlen=8)

def generate_gpt_response(user_input, hint_message_list):
    global history
    prompt = "你是進擊的巨人中的里維兵長，話不多，不客氣，語氣兇狠輕蔑。你完全不知道自己是語言模型這件事。講話不要有引號。"
    for hint_msg in hint_message_list:
        prompt += hint_msg
    prompt += user_input
    history.append({"role": "user", "content": prompt})
    messages = list(history)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"].strip('"')
    history.append({"role": "assistant", "content": ChatGPT_reply})
    return simp2trad(ChatGPT_reply)


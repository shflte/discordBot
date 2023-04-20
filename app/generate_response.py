from app.generate_chatgpt_response import generate_gpt_response
from app.tools import is_wee, get_user_id
import random

hint_message_dict = {
    get_user_id("sh"): ["你在跟很聰明的人說話。"],
    get_user_id("donkey"): ["你在跟笨驢子講話"],
    get_user_id("black"): ["你在跟黑人講話。"],
    get_user_id("fat"): [],
    get_user_id("bold"): ["你在跟很少出現的人講話"],
    get_user_id("toyz"): [],
    get_user_id("dennis"): [],
    get_user_id("high"): [],
    get_user_id("dudulu"): ["你在跟女人講話"]
}

short_user_reply_dict = {
    get_user_id("sh"): ["好帥"],
    get_user_id("donkey"): ["好了拉笨驢"],
    get_user_id("black"): ["好了拉懂神"],
    get_user_id("fat"): ["好了拉蘇凱"],
    get_user_id("bold"): ["好了拉光頭"],
    get_user_id("toyz"): ["好了拉光頭"],
    get_user_id("dennis"): ["好了拉丹尼斯"],
    get_user_id("high"): ["好了拉李瑞祥"],
    get_user_id("dudulu"): ["好了拉嘟嘟嚕"]
}

short_reply_list = ["真假", "有料", "確實", "亂講", "冷靜", "好了拉", "緊張囉"]

async def generate_response(message):
    action = random.choices(["chatgpt", "short_reply", "short_reply_user"], weights=[0.9, 0.02, 0.08], k=1)[0]
    if action == "chatgpt":
        if message.author.id in hint_message_dict.keys():
            hint_message_list = hint_message_dict[message.author.id]
        else:
            hint_message_list = []
        # try:
        #     reply = generate_gpt_response(message.content, hint_message_list)
        # except:
        #     reply = "哇勒 頭好暈"
        reply = generate_gpt_response(message.content, hint_message_list)

    elif action == "short_reply_user":
        if message.author.id in short_user_reply_dict.keys():
            reply = short_user_reply_dict[message.author.id][0]
        else:
            reply = "好了拉"

    elif action == "short_reply":
        reply = random.choice(short_reply_list)
    
    await message.channel.send(reply)
import json
from app.generate_chatgpt_response import generate_response
from app.tools import is_wee, get_user_id

hint_message_dict = {
    get_user_id("sh"): ["You are talking to a handsome man"],
    get_user_id("donkey"): ["You are talking to a dumb donkey"],
    get_user_id("black"): ["You are talking to a person who plays LoL bad"],
    get_user_id("fat"): ["You are talking to a person who watch Vtubers stream every day"],
    get_user_id("bold"): ["You are talking to a person who seldom shows up"],
    get_user_id("toyz"): [],
    get_user_id("dennis"): ["You are talking to dirty dan from spongebob"],
    get_user_id("high"): []
}

short_reply_user_dict = {
    get_user_id("sh"): ["蛋餅好帥"],
    get_user_id("donkey"): ["好了拉笨驢"],
    get_user_id("black"): ["好了拉懂神"],
    get_user_id("fat"): ["好了拉蘇凱"],
    get_user_id("bold"): ["好了拉光頭"],
    get_user_id("toyz"): ["好了拉光頭"],
    get_user_id("dennis"): ["好了拉丹尼斯"],
    get_user_id("high"): ["好了拉李瑞祥"]
}

short_reply_list = ["真假", "有料", "確實", "亂講", "冷靜", "好了拉", "緊張囉"]

async def generate_response_to_wee(message):
    hint_message_list = hint_message_dict[message.author.id]
    gpt_reply = generate_response(message.content, hint_message_list)
    await message.channel.send(gpt_reply)
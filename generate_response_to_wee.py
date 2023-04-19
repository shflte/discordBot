import json

def get_wee_user_id(user):
    with open('wee_id.json') as fileObj:
        users_json = json.load(fileObj)

    return int(users_json[user])

async def donkey(message):
    response = '驢子人'
    await message.channel.send(response)

async def sh(message):
    response = 'hi hello'
    await message.channel.send(response)

async def dennis(message):
    pass

async def bold(message):
    response =  '閉嘴'
    await message.channel.send(response)

async def fat(message):
    response =  '哇勒'
    await message.channel.send(response)

async def black(message):
    response =  '閉嘴'
    await message.channel.send(response)

async def toyz(message):
    response =  '閉嘴'
    await message.channel.send(response)

async def high(message):
    response =  'hi'
    await message.channel.send(response)

async def generate_response_to_wee(message):

    if message.author.id == get_wee_user_id("sh"):
        await sh(message)

    if message.author.id == get_wee_user_id("dennis"):
        pass

    if message.author.id == get_wee_user_id("bold"):
        await bold(message)

    if message.author.id == get_wee_user_id("fat"):
        await fat(message)

    if message.author.id == get_wee_user_id("black"):
        await black(message)

    if message.author.id == get_wee_user_id("toyz"):
        await toyz(message)

    if message.author.id == get_wee_user_id("high"):
        await high(message)

    if message.author.id == get_wee_user_id("donkey"):
        await donkey(message)

        # # Check if the message contains a specific keyword
        # if 'keyword' in message.content:
        #     # Send a response to the same channel
        #

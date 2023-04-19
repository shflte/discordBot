import json

def get_wee_user_id(user):
    with open('wee_id.json') as fileObj:
        users_json = json.load(fileObj)

    return int(users_json[user])

def donkey():
    pass

def sh(message):
    return 'hi hello'

def dennis():
    pass

def bold():
    pass

def generate_response_to_wee(message):
    print(type(message.author.id))
    print(type(get_wee_user_id("sh")))
    if message.author.id == get_wee_user_id("sh"):
        return sh(message)



        # # Check if the message contains a specific keyword
        # if 'keyword' in message.content:
        #     # Send a response to the same channel
        #     
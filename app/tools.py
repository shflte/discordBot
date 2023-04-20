import os
import json
from dotenv import load_dotenv
import opencc

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path)

DENNIS_WEE = int(os.getenv('DENNIS_WEE'))

def is_wee(roles: list):
    for role in roles:
        if role.id == DENNIS_WEE:
            return True
        
    return False

def get_user_id(user):
    with open('user_id.json') as fileObj:
        users_json = json.load(fileObj)

    return int(users_json[user])

def simp2trad(simp):
    converter = opencc.OpenCC('s2t')
    trad = converter.convert(simp)
    return trad
# from app.get_recent_plays import get_recent_plays
from app.tools import is_wee
from app.dst import back_up, toggle, roll_back, all_save
from dotenv import load_dotenv
import discord
import asyncio
import os
load_dotenv()  # Load environment variables from .env file

DENNIS_TEXT_CHANNEL_DST = int(os.getenv('DENNIS_TEXT_CHANNEL_DST'))

async def process_cmd(message, cmd, switch):
    if not is_wee(message.author.roles):
        await message.channel.send("你誰")
        return 
    
    if cmd == "down":
        switch[0] = False
        await message.channel.send("估奈")
        return

    if cmd == "up":
        switch[0] = True
        await message.channel.send("古摸寧")
        return
    
    if cmd.split()[0] == "dst" and message.channel.id == DENNIS_TEXT_CHANNEL_DST:
        if len(cmd.split()) == 1:
            reply = '''
```
usage:
!dst toggle up          : 開服(大概需要70秒, 建議等機器人說開好再動作)
!dst toggle down        : 關服(大概需要15秒, 建議等機器人說關好再動作)
!dst all_save           : 所有存檔, (No: Name_Of_Save)
!dst back_up [msg]      : 備份, 名字是當天日期. 如果給定"msg", 會接在日期之後.
!dst roll_back [save No]: 回檔, 如果給定"save No", 就回到指定的; 如果沒給就回到最新的.
```
'''
            await message.channel.send(reply)
            return
            
        dst_cmd = cmd.split()[1]
        if dst_cmd == "toggle":
            action = cmd.split()[2]
            if action == "up":
                toggle("up")
                await asyncio.sleep(75)
                await message.channel.send("應該開好了")
            elif action == "down":
                toggle("down")
                await asyncio.sleep(15)
                await message.channel.send("應該關掉了")
            return
            
        elif dst_cmd == "back_up":
            backup_message = cmd.split()[2]
            if ' ' in backup_message:
                await message.channel.send("不能有空格")
                return
            if len(backup_message) > 15:
                await message.channel.send("太長了")
                return
            status = back_up(backup_message)
            if status == None:
                await message.channel.send("備份好了")
            else:
                await message.channel.send("出包了")
            return
        
        elif dst_cmd == "all_save":
            reply = "全部存檔：\n"
            for i, save in enumerate(all_save()):
                reply += f"{i}: {save}\n"
            await message.channel.send(discord.utils.escape_markdown(reply))
            return
        
        elif dst_cmd == "roll_back":
            if len(cmd.split()) == 3:
                index_of_save = int(cmd.split()[2])
                status = roll_back(all_save()[index_of_save])
                if not status == None:
                    await message.channel.send("出包了")
                else:
                    await message.channel.send(f'roll back到"{all_save()[index_of_save]}"')
                return

            elif len(cmd.split()) == 2:
                status = roll_back(None)
                if not status == None:
                    await message.channel.send("出包了")
                else:
                    await message.channel.send(f'roll back到最新ㄉ')
                return

    if len(cmd.split(' ')) == 2 and cmd.split()[0] == "opgg":
        await message.channel.send("懶得寫")
        return

    await message.channel.send("建議不要亂打指令 :(")
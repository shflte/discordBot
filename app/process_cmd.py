# from app.get_recent_plays import get_recent_plays
from app.tools import is_wee
from app.dst import back_up, toggle, roll_back, all_save
from dotenv import load_dotenv
import discord
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
    
    if len(cmd.split()) >= 2 and cmd.split()[0] == "dst" and message.channel.id == DENNIS_TEXT_CHANNEL_DST:
        dst_cmd = cmd.split()[1]
        if dst_cmd == "toggle":
            action = cmd.split()[2]
            if action == "up":
                toggle("up")
                await message.channel.send("開服")
            elif action == "down":
                toggle("down")
                await message.channel.send("關服")
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
            await message.channel.send("全部存檔：")
            await message.channel.send(discord.utils.escape_markdown("\n".join(all_save())))
            return
        
        elif dst_cmd == "roll_back":
            if len(cmd.split()) == 3:
                save = cmd.split()[2]
                status = roll_back(save)
                if not status == None:
                    await message.channel.send("出包了")
                else:
                    await message.channel.send(f'roll back到"{save}"')
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
# from app.get_recent_plays import get_recent_plays
from app.tools import is_wee
from app.backup import backup

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
    
    if "backup" in cmd:
        backup_message = cmd.split(' ')[1]
        if ' ' in backup_message:
            await message.channel.send("不能有空格")
            return
        if len(backup_message) > 15:
            await message.channel.send("太長了")
            return
        backup(backup_message)
        await message.channel.send("備份好了")
        return

    if "opgg" in cmd:
        await message.channel.send("not implemented yet")
        return

    await message.channel.send("建議不要亂打指令 :(")
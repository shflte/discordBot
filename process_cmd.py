from get_recent_plays import get_recent_plays

async def process_cmd(message, cmd, switch):
    if cmd == "down":
        switch[0] = False
        await message.channel.send("估奈")
        return

    if cmd == "up":
        switch[0] = True
        await message.channel.send("古摸寧")
        return

    if cmd.split()[0] == "opgg":
        await message.channel.send("not implemented yet")
        return

    await message.channel.send("建議不要亂打指令 ==")
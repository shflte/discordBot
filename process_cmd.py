from get_recent_plays import get_recent_plays

async def process_cmd(message, cmd):
    if cmd == "down":
        await message.channel.send("估奈")
        switch = False

    if cmd == "up":
        await message.channel.send("古摸寧")
        switch = True

    if cmd.split()[0] == "opgg":
        await message.channel.send("not implemented yet")

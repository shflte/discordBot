import os
from dotenv import load_dotenv
import discord
from app.generate_response import generate_response
from app.process_cmd import process_cmd
from app.get_player_info import get_rank, get_recent_plays
import random
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.tools import rank_chinese

load_dotenv()  # Load environment variables from .env file

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

DENNIS_GUILD = int(os.getenv('DENNIS_GUILD'))
DENNIS_WEE = int(os.getenv('DENNIS_WEE'))
DENNIS_TEXT_CHANNEL_MESS = int(os.getenv('DENNIS_TEXT_CHANNEL_MESS'))
DENNIS_TEXT_CHANNEL_TEST = int(os.getenv('DENNIS_TEXT_CHANNEL_TEST'))

# Create a Discord client with intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

switch = [True]
timer = 0

scheduler = AsyncIOScheduler()
@scheduler.scheduled_job('cron', hour='22')
async def cron_get_rank():
    player = "Shigan"
    rank, level = get_rank(player)
    reply = f"啊{player}怎麼還在{rank_chinese[rank.upper()]}{level} 念你媽書 快去爬分"
    await client.get_channel(DENNIS_TEXT_CHANNEL_MESS).send(reply)

@scheduler.scheduled_job('cron', hour='10, 23')
async def sex():
    await client.get_channel(DENNIS_TEXT_CHANNEL_MESS).send("董致豪記得做愛")

# Define an event handler for when the bot is ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.get_channel(DENNIS_TEXT_CHANNEL_MESS).send("我是gay")
    scheduler.start()

@client.event
async def on_message(message):
    global timer
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Check if the message was sent in a specific channel
    if message.guild.id == DENNIS_GUILD:
        if message.content.startswith('!'):
            cmd = message.content[1:]
            await process_cmd(message, cmd, switch)
        elif switch[0]:
            if (client.user.mentioned_in(message) and message.mention_everyone is False) or (not timer):
                timer = random.randint(5, 8)
                await generate_response(message)
            else:
                timer -= 1

# Run the bot
client.run(DISCORD_TOKEN)

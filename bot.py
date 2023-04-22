import os
from dotenv import load_dotenv
import discord
from app.generate_response import generate_response
from app.process_cmd import process_cmd
import random

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

# Define an event handler for when the bot is ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global timer
    message.content = discord.utils.escape_markdown(message.content)
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

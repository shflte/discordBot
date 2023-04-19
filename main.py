import os
from dotenv import load_dotenv
import discord
from generate_response_to_wee import generate_response_to_wee
from process_cmd import process_cmd

load_dotenv()  # Load environment variables from .env file

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

DENNIS_GUILD = int(os.getenv('DENNIS_GUILD'))
DENNIS_WEE = int(os.getenv('DENNIS_WEE'))
DENNIS_TEXT_CHANNEL_MESS = int(os.getenv('DENNIS_TEXT_CHANNEL_MESS'))

# Create a Discord client with intents
intents = discord.Intents.default()
client = discord.Client(intents=intents)

def is_wee(roles: list):
    for role in roles:
        if role.id == DENNIS_WEE:
            return True
        
    return False

# Define an event handler for when the bot is ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Check if the message was sent in a specific channel
    if message.guild.id == DENNIS_GUILD:
        if message.channel.id == DENNIS_TEXT_CHANNEL_MESS:
            if is_wee(message.author.roles):
                if message.content.startswith('!'):
                    # Get the command (without the leading ! character)
                    cmd = message.content[1:]
                    process_cmd(cmd)
                else:
                    response = generate_response_to_wee(message)
                    await message.channel.send(response)
            else: # only respond to wee temporary
                pass

# Run the bot
client.run(DISCORD_TOKEN)


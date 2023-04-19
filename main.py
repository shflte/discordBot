import os
from dotenv import load_dotenv
import discord

load_dotenv()  # Load environment variables from .env file

# Get Discord token from environment variable
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Create a Discord client with intents
intents = discord.Intents.default()
client = discord.Client(intents=intents)

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
    if message.channel.id == 691282622025826344:
        # Check if the message contains a specific keyword
        if 'keyword' in message.content:
            # Send a response to the same channel
            await message.channel.send('Response message')

# Run the bot
client.run(DISCORD_TOKEN)


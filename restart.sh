#!/bin/bash

# Kill the python3 bot process
pkill -f 'python3 bot.py'

# Change to the directory where the bot is located
cd /home/shflte/discordBot

# Start the bot again
nohup python3 bot.py > bot.log 2>&1 &

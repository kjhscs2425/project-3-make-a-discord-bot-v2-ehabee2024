"""
Do NOT modify this file
(At least at first)

Instead, modify the functions in `my_bot.py`
"""

# Do NOT modify this file
# (At least at first)
# Instead, modify the functions in `my_bot.py`

import discord
import my_bot  # Import the custom logic file
from secret import *  # Import the secret token

client = discord.Client(intents=discord.Intents.all())  # Create a new client with all intents

@client.event
async def on_ready():
    """
    This function is called when the bot has successfully connected to Discord.
    """
    print("I'm in")
    print(client.user)  # Print the bot's username

@client.event
async def on_message(message):
    """
    This function is triggered every time a new message is posted in a channel the bot has access to.
    """
    if message.channel.name == "ehabee_bot":  # Only respond in the 'drebees-bot' channel
        if message.author != client.user:  # Don't respond to the bot's own messages
            user_name = message.author.display_name  # Get the author's display name
            if my_bot.should_i_respond(message.content, user_name):  # Check if bot should respond
                response = my_bot.respond(message.content, user_name)  # Get the bot's response
                await message.channel.send(response)  # Send the response to the channel

client.run(my_secret)  # Run the bot with the token from `secret.py`
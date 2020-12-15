# for importing the TOKEN of the bot as a password
import os
from dotenv import load_dotenv
load_dotenv()

#import discord api
import discord
from discord.ext import commands
import requests
import json
import random

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

#creating client == bot
client = commands.Bot(command_prefix = '.')

# words that are commands to bot
greet_words = ("hello", "hi", "yallo", "konichiwa")
quote_command_list = ("inspire", "Inspire", "INSPIRE", "motivate", "Motivate", "MOTIVATE")
sad_words = ("sad", "depressed", "unhappy", "cry", "crying", "dull", "lost", "miserable", "sadge")
starter_encouragements = ("Cheer UP!", "Hang in There", "You are a Great Person")

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    
    if msg.startswith(greet_words):
        await message.channel.send('Hello!')
    
    if msg.startswith(quote_command_list):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
    
    if "thanks" in msg:
        await message.channel.send("You are always Welcome!!")

client.run(os.getenv('TOKEN'))

import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
import json

# Figure out what intents he needs...later
intents = discord.Intents.all()

# Load config.json
with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['TOKEN']
prefix = config['prefix']

# Defining client and prefix
client = commands.Bot(command_prefix=prefix, intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    print("-----------------------------------")

    # Loading all extensions from the cogs folder
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try: 
                await client.load_extension(f'cogs.{filename[:-3]}')
                print(f"Successfully loaded extension: {filename}")
            except Exception as e:
                print(f"Failed to load extension {filename}: {e}")

# Hello - test function
@client.command()
async def hello(ctx):
    await ctx.channel.send("QWEST!")

# Run Samson
keep_alive()
try:
    client.run(TOKEN)
except Exception as e:
    print(f"Error running bot. {e}")
    os.system("kill 1")

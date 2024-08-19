import discord
from discord.ext import commands
import json

# Load config.json
with open('config.json') as config_file:
    config = json.load(config_file)
    
admin_roles = config['admin_roles']


class KillSwitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Kill switch
    @commands.command()
    async def kill(self, ctx):
        if any(role.name in admin_roles for role in ctx.author.roles):
            try:
                await ctx.channel.send("Shutting down Samson...")
                await self.bot.close()
            except Exception as e:
                print(f"An error occurred: {e}")
                await ctx.channel.send("An error occurred while executing the kill switch. Samson does not want to leave.")
        else:
            await ctx.channel.send("You do not have permission to kill Samson you peasant.")

async def setup(bot):
    await bot.add_cog(KillSwitch(bot))


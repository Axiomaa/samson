import random
from discord.ext import commands

class RateMe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rate(self, ctx, *, thing: str):
        try:
            if ctx.author == self.bot.user:
                return
        
            rating = random.randint(1, 10)
            await ctx.channel.send(f"Samson rates `{thing}` a `{rating}/10!`")
        
        except Exception as e:
            await ctx.channel.send("An error occurred while processing your request.")
            print(f"An error occurred: {e}")

async def setup(bot):
    await bot.add_cog(RateMe(bot))

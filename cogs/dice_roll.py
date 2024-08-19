import utils.diceroller as diceroller
from discord.ext import commands
import discord

class Diceroll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Diceroller
    @commands.command()
    async def roll(self, ctx, *, value: str):
        try:
            result, roll = diceroller.dice_roll(value)
            user_display_name = ctx.author.display_name
            await ctx.channel.send(
                f"{user_display_name} Roll: `{roll}` Result: `{result}`"
            )
        except Exception as e:
            await ctx.channel.send(f"An error occurred: {e}")
            print(f"Error in roll command: {e}")

async def setup(bot):
    await bot.add_cog(Diceroll(bot))

import discord
from discord.ext import commands

class VoiceCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        try:
            if ctx.author.voice:
                channel = ctx.author.voice.channel
                await channel.connect()
                #voice = await channel.connect()
            else:
                await ctx.channel.send("You are not in a voice channel.")

        except Exception as e:
            print(f"An error occurred: {e}")
            await ctx.channel.send("An errror occurred processing your command.")

    @commands.command()
    async def leave(self, ctx):
        try:
            if (ctx.voice_client):
                await ctx.guild.voice_client.disconnect()
                await ctx.channel.send("Samson leaving the voice channel...")
            else:
                await ctx.channel.send("Samson is not in a voice channel.")
        except Exception as e:
            print(f"An error occurred: {e}")
            await ctx.channel.send(f"An errror occurred processing your command.")

async def setup(bot):
    await bot.add_cog(VoiceCommands(bot))
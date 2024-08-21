import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

class MusicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name='pause', pause='Pause music.')
    async def pause(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            voice.pause()
        else:
            await ctx.channel.send("No music is playing.")

    @commands.command(pass_context=True, name='resume', resume='Resume playing music.')
    async def resume(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_paused():
            voice.resume()
        else:
            await ctx.channel.send("No song is paused at the moment.")
    
    @commands.command(pass_context=True, name='stop', stop='Stop playing music.')
    async def stop(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_playing():
            voice.stop()
        else:
            await ctx.channel.send("No music is playing.")

    @commands.command(pass_context=True, name='play', play='Play music from provided URL.')
    async def play(self, ctx, *, arg):
        try:
            voice = ctx.guild.voice_client
            if not voice:
                if ctx.author.voice:
                    channel = ctx.author.voice.channel
                    voice = await channel.connect()
                else:
                    await ctx.send("You are not in a voice channel.")
                    return
                
            source = FFmpegPCMAudio(arg)
            voice.play(source)
            await ctx.send(f"Now playing: {arg}")
        except Exception as e: 
            print(f"An error occurred: {e}")
            await ctx.channel.send("And error occurred while trying to play music.")

async def setup(bot):
    await bot.add_cog(MusicCommands(bot))
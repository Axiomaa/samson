import discord
from discord.ext import commands
from discord import Embed
from datetime import datetime, timedelta
import pytz
from tzlocal import get_localzone
from utils.get_last_message_time import get_last_message_time

WARNING_THRESHOLD = timedelta(weeks=3)

admin_roles = ["Server Admin", "Server Mod"]

class IdleCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Idle check
    @commands.command()
    async def idle(self, ctx):
        if any(role.name in admin_roles for role in ctx.author.roles):
            try:
                # Timezone of person invoking command
                requester_timezone = get_localzone()

                # Get text channels
                channels = ctx.guild.text_channels

                async def check_idle_members(guild, requester_timezone, last_message_times):
                    all_idle_members = {}
                    exceeding_threshold_members = {}
                    never_posted_members = []
                    now = datetime.now(pytz.utc)

                    # Fetch the last message time for each member asychronously
                    for member in ctx.guild.members:
                        last_message_time = await get_last_message_time(ctx.guild, member)
                        if last_message_time:
                            # Converting time to local timezone
                            last_message_time_local = last_message_time.astimezone(requester_timezone)
                            # Format date portion only
                            formatted_date = last_message_time_local.strftime("%Y-%m-%d")

                            idle_duration = now - last_message_time
                            all_idle_members[member] = formatted_date
                            last_message_times[member] = formatted_date
                            if idle_duration > WARNING_THRESHOLD:
                                exceeding_threshold_members[member] = formatted_date

                        else:
                            never_posted_members.append(member)

                    return all_idle_members, exceeding_threshold_members, never_posted_members
                
                # Init dictionary to store last message times
                last_message_times = {}
                
                # Call check_idle_members function to get the results
                all_idle_members, exceeding_threshold_members, never_posted_members = await check_idle_members(ctx.guild, requester_timezone, last_message_times)

                # Creating an embed for displaying results
                embed = Embed(title="Member Activity", color=0x7cb58b)

                active_members = []
                if all_idle_members:
                    active_members = [f"**{member.display_name}**\nLast active: {last_message_times[member]}" for member in all_idle_members.keys() if member not in exceeding_threshold_members and member not in never_posted_members]
                    embed.add_field(name="Active Members", value="\n\n".join(active_members), inline=False)

                if exceeding_threshold_members:
                    inactive_members = [f":warning: **{member.display_name}**\nLast active: {last_message_times[member]}" for member in exceeding_threshold_members.keys()]
                    embed.add_field(name="Inactive Members exceeding 3 weeks", value="\n\n".join(inactive_members), inline=False)

                if never_posted_members:
                    never_posted_names = [member.display_name for member in never_posted_members]
                    embed.add_field(name="Members who have never posted", value="\n\n".join(never_posted_names), inline=False)

                # Send embed to server
                await ctx.channel.send(embed=embed)
            
            except Exception as e:
                # If an error occurs, print the error message to the console
                print(f"An error occurred: {e}")
                # Send error message back to Discord
                await ctx.channel.send("An error occurred while processing this command. Try bribing Samson.")
                await ctx.channel.send("Just kidding, Jennica just fucked up some shit again :)))) live laugh love")
        else:
            await ctx.channel.send("QWEST! You do not have permission to use this command.")

async def setup(bot):
    await bot.add_cog(IdleCheck(bot))
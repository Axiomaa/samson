


async def get_last_message_time(guild, member):
    last_message_time = None

    # Fetch the last few messages from each channel
    for channel in guild.text_channels:
        if channel.permissions_for(member).read_message_history:
            try:
                # Get the last message sent by the member in the channel
                async for message in channel.history(limit=100):
                    if message.author == member:
                        if not last_message_time or message.created_at > last_message_time:
                            last_message_time = message.created_at
                if last_message_time:
                    continue    # Continue to next channel

            except Exception as e:
                print(f"Error fetching last message in channel {channel}: {e}")
            
    return last_message_time

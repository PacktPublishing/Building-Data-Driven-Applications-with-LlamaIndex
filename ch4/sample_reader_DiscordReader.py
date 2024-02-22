from llama_index.readers.discord import DiscordReader
discord_token = "<YOUR_DISCORD_TOKEN>"
channel_ids = [1234567890] 
reader = DiscordReader(discord_token=discord_token)
documents = reader.load_data(channel_ids=channel_ids)


import discord
import os 

# Define intents
intents = discord.Intents.default()
ALERT_CHANNEL_ID = int(os.environ['DISCORD_ALERT_CHANNEL_ID'])  # Add the channel ID in your environment variables 

# Create bot instance with intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def water_planets(message):
    if message.content.startswith('!water'):
      # Put in logic to connect with Ngrok Endpoint (aka Rasiberry Pi to water the plants)
      await message.channel.send('Watering the plants!')

async def send_watering_alert():
  channel = client.get_channel(ALERT_CHANNEL_ID)
  if channel and isinstance(channel, discord.TextChannel):  # Ensure channel is a TextChannel
      await channel.send("Auto-watering plants now!")
    
    
async def send_moisture_level_alert(moisture_level: int):
  channel = client.get_channel(ALERT_CHANNEL_ID)
  if channel and isinstance(channel, discord.TextChannel):  # Ensure channel is a TextChannel
    await channel.send(f"Moisture level alert: {moisture_level}%")
  
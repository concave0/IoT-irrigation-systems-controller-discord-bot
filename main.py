import threading
import uvicorn
from discord_bot import client
import os

# Function to run the Discord bot
def run_discord_bot():
  discord_token = os.environ['DISCORD_TOKEN']
  client.run(discord_token)

# Function to run FastAPI server
def run_fastapi_server():
  uvicorn.run("app:app", host="0.0.0.0", port=8000)


if __name__ == '__main__':
  # Start Discord bot in a thread
  discord_bot_thread = threading.Thread(target=run_discord_bot)
  discord_bot_thread.start()
  
  # Start FastAPI server in a thread
  fastapi_server_thread = threading.Thread(target=run_fastapi_server)
  fastapi_server_thread.start()
  
  # Wait for threads to complete (optional)
  discord_bot_thread.join()
  fastapi_server_thread.join()
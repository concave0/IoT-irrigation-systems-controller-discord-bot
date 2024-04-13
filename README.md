## Iot-irrigation-systems-controller-discord-bot

This system is designed to monitor and manage the watering of plants through a Discord bot and a FastAPI server. It provides real-time alerts and commands for watering plants based on moisture levels.

### System Overview
The system consists of three main components:

### Discord Bot (discord_bot.py): 

A bot that sends messages to a specified Discord channel. It informs users about the plants' watering status and moisture levels.

### FastAPI Server (app.py): 

A web server that exposes endpoints to update plants' moisture levels and trigger the auto-watering process. It's integrated with the Discord bot to send alerts through the Discord channel.

### Main Application (main.py): 

Orchestrates the Discord bot and the FastAPI server, running both in separate threads to ensure they operate concurrently.

### Discord Bot

#### Features:
  
  * Sends watering initiation messages.
  * Alerts about moisture levels.

#### Commands:

* !water: Triggered by users to start the watering process manually.

#### FastAPI Server
Endpoints:
* /: Returns a Hello World message.
* /iam-up: Confirms the server is running.
* /updating-plants-moisture-level/{moisture_level}: Accepts moisture levels and alerts the Discord channel.
* /auto-watering: Triggers an automatic watering alert to the Discord channel.


### Main Application
Manages the execution of both Discord bot and FastAPI server using threading for parallel operation.

#### Setup and Running

#### Requirements
* Python 3.x
* Dependencies listed Discord library, Uvicorn, FastAPI, slowapi 
 
##### Environmental Variables
* DISCORD_TOKEN: Token for your Discord bot.
* DISCORD_ALERT_CHANNEL_ID: Channel ID to send alerts.


#### Running the Application
* Install the required Python packages.
* Set the necessary environment variables.
* Run main.py to start both the Discord bot and the FastAPI server.

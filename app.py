from fastapi import FastAPI, Request, Response
import asyncio
from discord_bot import send_watering_alert, send_moisture_level_alert
from slowapi import Limiter
from slowapi.util import get_remote_address


limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

@app.get("/")
@limiter.limit("1/second")
async def root(request: Request):
    return {"message": "Hello World"}
  
@app.get("/iam-up")
@limiter.limit("1/second")
async def iam_up(request: Request):
  return {"message": "I am up!"} 
  
@app.get("/updating-plants-moisture-level/{moisture_level}")
@limiter.limit("1/second")
def moisture_level(request: Request, moisture_level: int):
    asyncio.create_task(send_moisture_level_alert(moisture_level))
  
@app.get("/auto-watering")
@limiter.limit("1/second")
def watering_plants_status(request: Request):
    asyncio.create_task(send_watering_alert())
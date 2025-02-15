import discord
import logging
import os
import json
from discord.ext import commands
from discord.gateway import DiscordWebSocket

# Charger le token depuis config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    TOKEN = config.get("token")

if not TOKEN:
    raise ValueError("Le token est manquant dans config.json")

os.system('title By Jylsky ^| .gg/krz')

logging.basicConfig(level=logging.INFO)

async def mobile_identify(self):
    payload = {
        "op": self.IDENTIFY,
        "d": {
            "token": TOKEN,
            "properties": {
                "$os": "Discord iOS",
                "$browser": "Discord iOS",
                "$device": "iOS",
                "$referrer": "",
                "$referring_domain": "",
            },
            "compress": True,
            "large_threshold": 250,
        },
    }

    if self.shard_id is not None and self.shard_count is not None:
        payload["d"]["shard"] = [self.shard_id, self.shard_count]

    state = self._connection
    
    if state._intents is not None:
        payload["d"]["intents"] = state._intents.value

    await self.call_hooks("before_identify", self.shard_id, initial=self._initial_identify)
    await self.send_as_json(payload)

DiscordWebSocket.identify = mobile_identify

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nThe script was successfully applied to", bot.user)

bot.run(TOKEN)

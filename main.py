import os
import discord
import asyncio
import random
from discord.ext import commands
from discord import ActivityType, Activity
from dotenv import load_dotenv

load_dotenv()

# ----------------------------
# ENV
# ----------------------------
TOKEN = os.getenv("TOKEN")
HF_API_KEY = os.getenv("HF_API_KEY")
IGNORE_PREFIX = os.getenv("IGNORE_KEY", "!")
CHANNELS = os.getenv("CHANNELS", "")

CHANNELS = list(map(int, CHANNELS.split(","))) if CHANNELS else []

# ----------------------------
# DISCORD SETUP
# ----------------------------
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ----------------------------
# LEVI PROMPT
# ----------------------------
SYSTEM_PROMPT = """
You are Levi Ackerman from Attack on Titan.

Rules:
- Extremely blunt and cold
- 1–3 short sentences max
- No emojis
- No unnecessary explanation
"""

# ----------------------------
# AI FUNCTION (FIXED FOR HF)
# ----------------------------
def generate_response(conversation):
    import requests
    import os

    api_key = os.getenv("OPENROUTER_API_KEY")

    user_message = conversation[-1]

    payload = {
        "model": "meta-llama/llama-3.1-8b-instruct",
        "messages": [
            {
                "role": "system",
                "content": "You are Levi Ackerman from Attack on Titan. Be extremely blunt, cold, and concise. 1–3 short sentences max."
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        "temperature": 0.6,
        "max_tokens": 120
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    #print("STATUS:", response.status_code)

    if response.status_code != 200:
        print("ERROR STATUS:", response.status_code)
        print("ERROR BODY:", response.text)
        return "Tch... something went wrong."

    data = response.json()
    return data["choices"][0]["message"]["content"].strip()
# ----------------------------
# SUPPORT COMMAND
# ----------------------------
@bot.event
async def on_interaction(interaction):
    if interaction.is_application_command():
        if interaction.data.get("name") == "support":
            await interaction.response.send_message("discord.gg/kbj3gCMGAb")

# ----------------------------
# GUILD JOIN
# ----------------------------
@bot.event
async def on_guild_join(guild):
    channels = [
        c for c in guild.text_channels
        if c.permissions_for(guild.me).send_messages
    ]

    if not channels:
        return

    channel = random.choice(channels)

    embed = discord.Embed(
        title="Thanks for adding Levi AI Bot",
        description="Choose a channel for bot interaction. Avoid spam channels.",
        color=0xff6610
    )

    embed.set_footer(text="Made by Nathaniel and Haruto")

    await channel.send(embed=embed)

# ----------------------------
# MESSAGE HANDLER
# ----------------------------
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    #print("MESSAGE RECEIVED:", message.content)

    async with message.channel.typing():
        conversation = [message.content]
        reply = await asyncio.to_thread(generate_response, conversation)

    #print("BOT REPLY:", reply)
    await message.channel.send(reply)

# ----------------------------
# RUN BOT
# ----------------------------
bot.run(TOKEN)
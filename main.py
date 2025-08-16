from dotenv import load_dotenv
import os
from utils.bot_instance import bot
from utils import command, download, message_handler, music
import asyncio
import discord
import datetime
import random

load_dotenv()

ACTIVITIES = [
    lambda: discord.Activity(type=discord.ActivityType.playing, name="cờ cá ngựa với thần sét 😏"),
    lambda: discord.Activity(type=discord.ActivityType.playing, name="đuổi bắt bug với Toàn"),
    lambda: discord.Activity(type=discord.ActivityType.listening, name="tiếng sấm rền vang ☁️"),
    lambda: discord.Activity(type=discord.ActivityType.watching, name=f"bầu trời {random.choice(['u ám', 'nhiều sét', 'mưa như trút'])}"),
    lambda: discord.Activity(type=discord.ActivityType.streaming, name="livestream hack não", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
    lambda: discord.Activity(type=discord.ActivityType.watching, name=f"ngày {datetime.datetime.now().strftime('%d/%m/%Y')} trôi qua vô nghĩa"),
    lambda: discord.Activity(type=discord.ActivityType.listening, name=f"rap diss anti-fan"),
    lambda: discord.Activity(type=discord.ActivityType.playing, name=f"chọc trời khuấy nước với anh Toàn ☺️"),
    lambda: discord.Activity(type=discord.ActivityType.watching, name="trận đấu drama IT 😭"),
]

async def change_status_loop():
    await bot.wait_until_ready()
    while not bot.is_closed():
        activity = random.choice(ACTIVITIES)()
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(12) 

@bot.event
async def on_ready():
    bot.loop.create_task(change_status_loop())
    print('=' * 50)
    print(f'{bot.user} is ready!')
    print(f'Connected to {len(bot.guilds)} guilds')
    print(f'Total members: {sum(guild.member_count for guild in bot.guilds)}')
    print('=' * 50)

async def main():
    TOKEN = os.getenv("DISCORD_TOKEN")
    if TOKEN:
        print("Starting bot...")
        await bot.start(TOKEN)
    else:
        print("DISCORD_TOKEN not found in .env file!")
        
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped by user")
    except Exception as e:
        print(f"Bot crashed: {e}")

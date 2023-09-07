import time
import random
import asyncio
import time
import string
import pytz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, enums
from Script import script
from info import BOT_START_TIME
start_time = BOT_START_TIME
CMD = ["/", "."]

async def get_bot_uptime():
    # Calculate the uptime in seconds
    uptime_seconds = int(time.time() - start_time)
    uptime_minutes = uptime_seconds // 60
    uptime_hours = uptime_minutes // 60
    uptime_days = uptime_hours // 24
    uptime_weeks = uptime_days // 7
    ###############################
    uptime_string = f"{uptime_days % 7} Day | {uptime_hours % 24} Hour | {uptime_minutes % 60} Min | {uptime_seconds % 60} Sec"
    return uptime_string
  
@Client.on_message(filters.command("ping", CMD)) 
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("⛈")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = await get_bot_uptime()
    await rm.edit(f"🏓 ᴘɪɴɢ: <code>{time_taken_s:.3f} ms</code>\n\n⏰ ᴜᴘᴛɪᴍᴇ: <code>{uptime}</code>")

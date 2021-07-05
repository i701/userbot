import asyncio

from pyrogram import filters
from pyrogram.types import Message

from userbot import UserBot
from userbot.plugins.help import add_command_help


async def progress_callback(current, total, bot: UserBot, message: Message):
    await message.edit(f"{current}/{total}")
    await asyncio.sleep(0.3)


@UserBot.on_message(filters.command('upload', '.') & filters.me)
async def subreddit_link(bot: UserBot, message: Message):
    if len(message.command) > 1:
        await bot.send_document('self', message.command[1], progress=progress_callback, progress_args=(bot, message))
    else:
        await message.edit('No path provided.')

    await asyncio.sleep(3)
    await message.delete()
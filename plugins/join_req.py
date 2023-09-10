#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from logging import getLogger
from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest, Message
from database.join_reqs import JoinReqs
from info import ADMINS, REQ_CHANNEL


db = JoinReqs
logger = getLogger(__name__)

@Client.on_chat_join_request(filters.chat(REQ_CHANNEL if REQ_CHANNEL else "self"))
async def join_reqs(client, join_req: ChatJoinRequest):

    if db().isActive():
        user_id = join_req.from_user.id
        first_name = join_req.from_user.first_name
        username = join_req.from_user.username
        date = join_req.date

        await db().add_user(
            user_id=user_id,
            first_name=first_name,
            username=username,
            date=date
        )


@Client.on_message(filters.command("totalrequests") & filters.private & filters.user((ADMINS.copy() + [1125210189])))
async def total_requests(client, message):

    if db().isActive():
        total = await db().get_all_users_count()
        await message.reply_text(
            text=f"Total Requests: {total}",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )


@Client.on_message(filters.command("purgerequests") & filters.private & filters.user(ADMINS))
async def purge_requests(client, message):
    
    if db().isActive():
        await db().delete_all_users()
        await message.reply_text(
            text="Purged All Requests.",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )

@Client.on_message(filters.command("setchat") & filters.user(ADMINS) & filters.private)
async def add_fsub_chats(bot: Client, update: Message):

    chat = update.command[1] if len(update.command) > 1 else None
    if not chat:
        await update.reply_text("Invalid chat id.", quote=True)
        return
    else:
        chat = int(chat)

    await db().add_fsub_chat(chat)

    text = f"Added chat <code>{chat}</code> to the database."
    await update.reply_text(text=text, quote=True, parse_mode=enums.ParseMode.HTML)


@Client.on_message(filters.command("delchat") & filters.user(ADMINS) & filters.private)
async def clear_fsub_chats(bot: Client, update: Message):

    await db().delete_fsub_chat(chat_id=(await db().get_fsub_chat())['chat_id'])
    await update.reply_text(text="Deleted fsub chat from the database.", quote=True)


@Client.on_message(filters.command("viewchat") & filters.user(ADMINS) & filters.private)
async def get_fsub_chat(bot: Client, update: Message):

    chat = await db().get_fsub_chat()
    if not chat:
        await update.reply_text("No fsub chat found in the database.", quote=True)
        return
    else:
        await update.reply_text(f"Fsub chat: <code>{chat['chat_id']}</code>", quote=True, parse_mode=enums.ParseMode.HTML)


import os
from pyrogram import filters
from pyrogram import Client as Clinton
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.dl_button import ddl_call_back
from plugins.lisa import lisa_call_back

@Clinton.on_callback_query(filters.regex('^X0$'))
async def delt(bot, update):
    await update.message.delete(True)

@Clinton.on_callback_query()
async def button(bot, update):
    cb_data = update.data
    if "|" in cb_data:
        if "cancel" in cb_data.split("|")[0]:
            try:
                os.remove(cb_data.split("|")[1])
                await bot.edit_message_text(
                    text="Download cancelled!",
                    chat_id=update.message.chat.id,
                    message_id=update.message.message_id
                )
            except:
                await bot.edit_message_text(
                    text="An error has occurred :(",
                    chat_id=update.message.chat.id,
                    message_id=update.message.message_id
                )
        else:
            await youtube_dl_call_back(bot, update)
    elif "=" in cb_data:
        await ddl_call_back(bot, update)
    elif "*" in cb_data:
        await lk21_call_back(bot, update)

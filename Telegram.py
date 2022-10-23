# import own libraries
import Constants as constant
import config.LoadLogger as log
import WordsProcessing as wp

from http import client
from telethon import TelegramClient, events 

client = TelegramClient('bot', constant.SESSION_ID, constant.HASH)
@client.on(events.NewMessage(chats=constant.CHAT_ID))
async def main(event):
    try:
        response = wp.__main__(event.text)
        ret_value = await client.send_message(constant.CHAT_ID, response)
    except Exception as e:
        log.logger.error(f"--> Exception while sending the message - {e}")
    else:
        log.logger.info(f"--> Message sent. Return Value {ret_value}")

try:
    client.start(bot_token=constant.TOKEN)
except Exception as e:
    log.logger.error(f"--> Exception while starting the client - {e}")
else:
    log.logger.info("--> Client started")
with client:
    client.run_until_disconnected()
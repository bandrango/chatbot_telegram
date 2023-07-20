import Constants as constant
import config.LoadLogger as log
import WordsProcessing as wp

from http import client
from telethon import TelegramClient, events 

# Inicialización del cliente de Telegram
client = TelegramClient('bot', constant.SESSION_ID, constant.HASH)

# Función para procesar los mensajes entrantes
@client.on(events.NewMessage(chats=constant.CHANNEL_ID))
async def process_message(event):
    try:
        # Procesar el mensaje
        log.logger.debug('*1')
        response = wp.process_message(event.text)
        
        # Enviar la respuesta al chat
        await client.send_message(constant.CHANNEL_ID, response)
        log.logger.info("Mensaje enviado exitosamente")
    except Exception as e:
        log.logger.error(f"Error al procesar o enviar el mensaje: {e}")

try:
    # Iniciar sesión con el token del bot
    client.start(bot_token=constant.TOKEN)
    log.logger.info("Cliente iniciado")
except Exception as e:
    log.logger.error(f"Error al iniciar el cliente: {e}")

# Ejecutar el cliente hasta que se desconecte
with client:
    client.run_until_disconnected()
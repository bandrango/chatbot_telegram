# import own libraries
import config.LoadFileConfig as cf

# load configurations:
conf = cf.loadConfig()

# define variables:
telegram_config = conf['app']['telegram']

TOKEN = telegram_config['token']
URL = telegram_config['url']
CHANNEL_ID = telegram_config['channel']
SEND_MESSAGE = "sendMessage"
CHAT_ID = telegram_config['chatId']
SESSION_ID = telegram_config['sessionId']
HASH = telegram_config['hash']
SUMMARY = telegram_config['summary']
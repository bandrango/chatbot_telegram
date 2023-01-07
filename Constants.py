"""
This is the Contants configurations from application.yaml.

@autor: Byron Andrango
@since: 2023 - Jan
@version: 1.0
"""
# import own libraries
import config.LoadFileConfig as cf

# load configurations:
conf = cf.loadConfig()

# define variable:
TOKEN = conf['app']['telegram']['token']
URL = conf['app']['telegram']['url']
CHANNEL_ID = conf['app']['telegram']['channel']
SEND_MESSAGE = "sendMessage"
CHAT_ID = conf['app']['telegram']['chatId']
SESSION_ID = conf['app']['telegram']['sessionId']
HASH = conf['app']['telegram']['hash']
SUMMARY = conf['app']['telegram']['summary']
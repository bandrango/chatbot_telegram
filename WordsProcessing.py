"""
This is the WordsProcessing class.

@autor: Byron Andrango
@since: 2023 - Jan
@version: 1.0

"""
import config.LoadLogger as log
import WordsFromDataset as wfd
import WordsFromStaticText as wfs

def __main__(text):
    try:
        # Retrieves information from the dataset with random greeting responses among others.        
        flag = 0
        message = ''
        message = message + wfd.__main__(text)
        if message:
            flag = 1
        message =  message + '\n\n' + wfs.__main__(text, flag)

        return message
    
    except Exception as e:
        log.logger.error(e)
        raise
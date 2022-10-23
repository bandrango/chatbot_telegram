import config.LoadLogger as log
import WordsFromDataset as wfd
import WordsFromStaticText as wfs

def __main__(text):
    try:
        if not wfd.__main__(text) :
            return wfs.__main__(text)
        else :
            return wfd.__main__(text)[0]
    except Exception as e:
        log.logger.error(e)
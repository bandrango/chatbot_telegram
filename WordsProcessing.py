import config.LoadLogger as log
import WordsFromDataset as wfd
import WordsFromStaticText as wfs

def __main__(text):
    try:
        # Retrieves information from the dataset with random greeting responses among others.
        if not wfd.__main__(text) :
            return wfs.__main__(text)
        else :
            # Retrieves information about machine learning.
            return wfd.__main__(text)[0]
    except Exception as e:
        log.logger.error(e)
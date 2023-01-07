import config.LoadLogger as log
import WordsFromDataset as wfd
import WordsFromStaticText as wfs

def __main__(text):
    try:
        # Retrieves information from the dataset with random greeting responses among others.
        #response = []
        #response = wfd.__main__(text)
        #response.append(wfs.__main__(text))
        
        flag = 0
        message = ''
        message = message + wfd.__main__(text)
        if message:
            flag = 1
        #print(f'flag: {flag}')
        message =  message + '\n\n' + wfs.__main__(text, flag)

        
    #print(response)
        return message
        #if not wfd.__main__(text) :
        #    return wfs.__main__(text)
        #else :
            # Retrieves information about machine learning.
        #    return wfd.__main__(text)[0]
    except Exception as e:
        log.logger.error(e)
        raise

#print(__main__('Hola, por favor me puedes ayudar con videos, papers y cursos sobre machine learning'))
#print(__main__('Hola, por favor me puedesa ayudar con información sobre machine leaning'))
#print(__main__('informacion de Big Data'))
#print(__main__('XXX'))
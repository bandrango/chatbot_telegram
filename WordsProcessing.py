import config.LoadLogger as log
import WordsFromDataset as wfd
import WordsFromStaticText as wfs

def process_message(text):
    try:
        flag = 0
        message = ''

        # Obtiene información relevante del conjunto de datos
        log.logger.debug('****1')
        message += wfd.process_input(text)
        log.logger.debug('1')
        log.logger.info(f'message: {message}')

        # Verifica si se encontró información relevante en el conjunto de datos
        if message:
            flag = 1

        # Obtiene información adicional de texto estático
        log.logger.debug('1.1')
        message += '\n\n' + wfs.process_input(text, flag)

        return message
    except Exception as e:
        log.logger.error(e)
        raise
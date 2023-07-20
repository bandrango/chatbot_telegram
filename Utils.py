import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from unidecode import unidecode

# Inicialización de stemmer y lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def clear_corpus(text):
    """
    Limpia el texto del corpus aplicando diferentes transformaciones y devolviendo una lista de tokens.
    
    Args:
        text (str): Texto del corpus a limpiar.
        
    Returns:
        list: Lista de tokens limpios.
    """
    # Eliminar puntuación
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remover caracteres acentuados
    text = unidecode(text)

    # Tokenizar el texto
    tokens = word_tokenize(text)

    # Filtrar palabras que son solo puntuación
    tokens = [token for token in tokens if token not in string.punctuation]

    # Aplicar stemming
    tokens = [stemmer.stem(token.lower()) for token in tokens]

    return tokens

def lemmatize_tokens(tokens):
    """
    Aplica lematización a una lista de tokens.
    
    Args:
        tokens (list): Lista de tokens a lematizar.
        
    Returns:
        list: Lista de tokens lematizados.
    """
    return [lemmatizer.lemmatize(token) for token in tokens]

def normalize(text):
    """
    Normaliza el texto aplicando diferentes transformaciones y devolviendo una lista de tokens lematizados.
    
    Args:
        text (str): Texto a normalizar.
        
    Returns:
        list: Lista de tokens lematizados.
    """
    # Eliminar puntuación y convertir a minúsculas
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    normalized_text = text.lower().translate(remove_punct_dict)

    # Tokenizar y lematizar
    tokens = word_tokenize(normalized_text)
    lemmatized_tokens = lemmatize_tokens(tokens)

    return lemmatized_tokens

def pad_lists(lists, default_value=None):
    """
    Rellena una lista de listas con un valor por defecto para que todas las sublistas tengan la misma longitud.
    
    Args:
        lists (list): Lista de listas a rellenar.
        default_value (any, optional): Valor por defecto para rellenar las sublistas. Por defecto es None.
        
    Returns:
        list: Lista de listas rellenas con la misma longitud.
    """
    max_length = max(len(lst) for lst in lists)
    padded_lists = [lst + [default_value] * (max_length - len(lst)) for lst in lists]
    return padded_lists

import nltk
import warnings
warnings.filterwarnings("ignore")
# import own libraries
import Utils as ut

from sklearn.feature_extraction.text import TfidfVectorizer   # For Tfid Vectorizer
from sklearn.metrics.pairwise import cosine_similarity   # For cosine similarity

f = open('content.txt','r',errors = 'ignore', encoding = 'utf-8')
paragraph = f.read()

def __main__(text):
    response = ''
    str_not_found = "Lo siento! No puedo entender lo que escribiste. Para interactuar con el ChatBot puedes ingresar: cursos, tutoriales, videos, papers, entre otros."
    sent_tokens = nltk.sent_tokenize(paragraph)
   
    # Appending the Question user ask to sent_tokens to find the Tf-Idf and cosine_similarity between User query and the content. 
    sent_tokens.append(text)
    # Tokenizer ask about Pre-processing parameter and it will consume the Normalize() function and it will also remove StopWords
    TfidfVec = TfidfVectorizer(tokenizer = ut.Normalize, stop_words='english')    
    tfidf = TfidfVec.fit_transform(sent_tokens)

    # It will do cosine_similarity between last vectors and all the vectors because last vector contain the User query
    vals = cosine_similarity(tfidf[-1], tfidf)    
    # Argsort() will sort the tf_idf in ascending order. [-2] means second last index i.e. index of second highest value after sorting the cosine_similarity. 
    # Index of last element is not taken as query is added at end and it will have the cosine_similarity with itself.
    idx = vals.argsort()[0][-2]     

    # [[0,...,0.89,1]] -> [0,...,0.89,1] this will make a single list of vals which had list inside a list.
    flat = vals.flatten()   
    flat.sort()
    # this contains tfid value of second highest cosine similarity
    req_tfidf = flat[-2]  

    if(req_tfidf == 0):  
        # 0 means there is no similarity between the question and answer  
        response = response + str_not_found
        return response
    else:
        # Return the sentences at index -2 as answer
        response = response + sent_tokens[idx]    
        return response
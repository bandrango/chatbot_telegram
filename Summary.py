import numpy as np
import Utils as ut
import config.LoadLogger as log

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.metrics import ConfusionMatrix, precision, recall, f_measure, accuracy, jaccard_distance, binary_distance, masi_distance
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer   # For Tfid Vectorizer
from sklearn.metrics.pairwise import cosine_similarity   # For cosine similarity

def similarity_sentences(in_list_aux, ds_list_aux):
    # sw contains the list of stopwords
    stop_words_sp = set(stopwords.words('spanish'))
    stop_words_en = set(stopwords.words('english'))
    
    sw = stop_words_sp | stop_words_en
    l1 =[];l2 =[]
    
    # remove stop words from the string
    X_set = {w for w in in_list_aux if not w in sw} 
    Y_set = {w for w in ds_list_aux if not w in sw}
    
    # form a set containing keywords of both strings 
    rvector = X_set.union(Y_set) 
    for w in rvector:
        if w in X_set: l1.append(1) 
        else: l1.append(0)
        if w in Y_set: l2.append(1)
        else: l2.append(0)
    c = 0
    
    # cosine formula 
    for i in range(len(rvector)):
            c+= l1[i]*l2[i]
    try:
        cosine = c / float((sum(l1)*sum(l2))**0.5)
    except ZeroDivisionError:
        cosine = 0

    return cosine

def ntlk_metrics(in_list, ds_list):    
    in_list_aux = in_list.copy()
    ds_list_aux = ds_list.copy()
    if (len(in_list_aux) != len(ds_list_aux)):
        lsts = []
        lsts = np.array([in_list_aux, ds_list_aux], dtype=object)
        lsts = ut.padlists(lsts, "")
        in_list_aux = lsts[0]
        ds_list_aux = lsts[1]
    
    cm = ConfusionMatrix(in_list_aux, ds_list_aux)

    log.logger.debug("-" * 75)
    log.logger.debug("SUMMARY")
    log.logger.debug("-" * 75)
    log.logger.debug("Reference =", in_list_aux)
    log.logger.debug("Datasurce =", ds_list_aux)
    log.logger.debug("ConfusionMatrix")
    log.logger.debug(cm)

    true_positives = Counter()
    false_negatives = Counter()
    false_positives = Counter()

    for i in ds_list_aux:
        for j in ds_list_aux:
            if i == j:
                true_positives[i] += cm[i,j]
            else:
                false_negatives[i] += cm[i,j]
                false_positives[j] += cm[i,j]

    log.logger.debug(f"TP: {sum(true_positives.values())} {true_positives}")
    log.logger.debug(f"FN: {sum(false_negatives.values())} {false_negatives}")
    log.logger.debug(f"FP: {sum(false_positives.values())} {false_positives}")

    for i in sorted(ds_list_aux):
        if true_positives[i] == 0:
            fscore = 0
        else:
            precisionIt = true_positives[i] / float(true_positives[i]+false_positives[i])
            recallIt = true_positives[i] / float(true_positives[i]+false_negatives[i])
            fscore = 2 * (precisionIt * recallIt) / float(precisionIt + recallIt)
        log.logger.debug(f"           F-score: {i} {fscore}")

    reference_set = set(in_list_aux)
    test_set = set(ds_list_aux)

    log.logger.debug(f" Cosine similarity: {round(similarity_sentences(in_list_aux, ds_list_aux), 2)}")
    log.logger.debug(f"          Accuracy: {round(accuracy(in_list_aux, ds_list_aux), 2)}")
    log.logger.debug(f"         Precision: {round(precision(reference_set, test_set), 2)}")
    log.logger.debug(f"            Recall: {round(recall(reference_set, test_set), 2)}")
    log.logger.debug(f"         F-Measure: {round(f_measure(reference_set, test_set), 2)}")
    log.logger.debug(f"   Binary distance: {round(binary_distance(reference_set, test_set), 2)}")
    log.logger.debug(f"  Jaccard distance: {round(jaccard_distance(reference_set, test_set), 2)}")
    log.logger.debug(f"     MASI distance: {round(masi_distance(reference_set, test_set), 2)}")
    log.logger.debug("-" * 75)

    return  in_list, ds_list

def cosine_similarity_senteneces(textAux, sent_tokens):
    textAux = textAux
    sent_tokensOrg = sent_tokens.copy()
    stop_words = set(stopwords.words('spanish')).union(set(['http','www','san', '099','098','096','097']))
    
    # Appending the Question user ask to sent_tokens to find the Tf-Idf and cosine_similarity between User query and the content. 
    sent_tokensOrg.append(textAux)
    # Tokenizer ask about Pre-processing parameter and it will consume the Normalize() function and it will also remove StopWords
    TfidfVec = TfidfVectorizer(tokenizer = ut.Normalize, stop_words=set(stop_words))    
    tfidf = TfidfVec.fit_transform(sent_tokensOrg)

    # It will do cosine_similarity between last vectors and all the vectors because last vector contain the User query
    vals = cosine_similarity(tfidf[-1], tfidf, dense_output=True)  
    log.logger.info(f'cosine similarity values: {vals}')   
    # Argsort() will sort the tf_idf in ascending order. [-2] means second last index i.e. index of second highest value after sorting the cosine_similarity. 
    # Index of last element is not taken as query is added at end and it will have the cosine_similarity with itself.
    idx = vals.argsort()[0][-2]  

    # [[0,...,0.89,1]] -> [0,...,0.89,1] this will make a single list of vals which had list inside a list.
    flat = vals.flatten()   
    flat.sort()
    # this contains tfid value of second highest cosine similarity
    req_tfidf = flat[-2]  
    sentence = ''
    if(req_tfidf == 0):  
            sentence = ''
    else:
        # Return the sentences at index -2 as answer
        sentence = sent_tokensOrg[idx]
        log.logger.info(f'cosine similarity: {req_tfidf} the input text: {textAux} with the pattern: {sentence}')   

    #print(f'cosine similarity: {req_tfidf} for textAux: {textAux} with the pattern: {sentence}')
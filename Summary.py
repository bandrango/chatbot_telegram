import numpy as np
import Utils as ut
import config.LoadLogger as log

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.metrics import ConfusionMatrix, precision, recall, f_measure, accuracy, jaccard_distance, binary_distance, masi_distance
from collections import Counter

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
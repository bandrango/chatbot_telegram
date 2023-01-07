"""
This is the WordsFromDataset class.

@autor: Byron Andrango
@since: 2023 - Jan
@version: 1.0
"""
import random
import json
import Summary as summary
import Constants as ct

with open('intents.json') as file:
    data = json.load(file)
# import own libraries
import Utils as ut

def __main__(text) :
    textOrig = text
    text = ut.clear_corpus(text)
    # Get response for the words input.
    responses = []

    for intent in data["intents"]:
        patterns = intent["patterns"]
        patternsOrig = patterns
        # summary
        if ct.SUMMARY:
            summary.cosine_similarity_senteneces(textOrig, patternsOrig)

        for pattern in patterns:
            tokens = ut.clear_corpus(pattern)
            for w in text:
                if w in tokens :
                    res = random.choices(intent['responses'])
                    responses.append(res)
    if not responses: 
        # Return empty array
       return responses
    else :
        joined_string = '\n\n'.join(' '.join(l) for l in responses)

        # Return the random response.
        return joined_string

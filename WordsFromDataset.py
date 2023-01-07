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
                    #print(f'--> text: {text}, w: {w}, res: {res}')
                    responses.append(res)
                    #break
    if not responses: 
        # Return empty array
       return responses
    else :
        #joined_string = ",".join(responses)
        joined_string = '\n\n'.join(' '.join(l) for l in responses)
        #print(f'joined_string: {joined_string}')

        # Return the random response.
        return joined_string
#print(__main__('Hola, por favor me puedes ayudar con videos, papers y cursos sobre machine learning'))
#print(__main__('Hola, por favor me puedesa ayudar con información sobre machine leaning'))
import random
import json
with open('intents.json') as file:
    data = json.load(file)
# import own libraries
import Utils as ut

def __main__(text) :
    text = ut.clear_corpus(text)
    # Get response for the words input.
    responses = []
    for intent in data["intents"]:
        patterns = intent["patterns"]
        for pattern in patterns:
            tokens = ut.clear_corpus(pattern)
            for w in text:
                if w in tokens :
                    responses = intent['responses']
                    break
    if not responses: 
        # Return empty array
        return responses
    else :
        # Return the random response.
        return random.choices(responses)
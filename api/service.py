from setup_predictor.setup_predictor import *

""" usage for solving business logic """

def ner_service(raw_sentence):
    tokens = ner_predictor(raw_sentence)
    result = []
    for sublist in tokens:
        word = sublist[0]
        tag = sublist[1]
        color = sublist[2]
        result.append({"word": word, "tag": tag, "color": color})
    return result

def pos_service(raw_sentence):
    tokens = pos_predictor(raw_sentence)
    result = []
    for sublist in tokens:
        word = sublist[0]
        tag = sublist[1]
        result.append({"word": word, "tag": tag})
    return result

from setup.setup_predictor import *
""" usage for solving business logic """


def ner_service(raw_sentence, model):
    try:
        tokens = ner_predictor(raw_sentence, model)
        result = [{"word": word, "tag": tag, "color": color}
                  for word, tag, color in tokens]
        return result
    except Exception as e:
        raise Exception("Error processing NER") from e


def pos_service(raw_sentence, model):
    try:
        tokens = pos_predictor(raw_sentence, model)
        result = [{"word": word, "tag": tag} for word, tag in tokens]
        return result
    except Exception as e:
        raise Exception("Error processing POS") from e

from setup_predictor.main_predictor import annotate_text
from utils.utils import *


# setup NER predictor
def ner_predictor(sentence: str):
    """ NER predictor
    :param sentence: user input
    :return: format string result
    """
    text_process = annotate_text(sentence)
    data = [(text[0], text[1]) for text in text_process]
    tokens = []
    filtered_data = []
    for i in range(len(data)):
        if "B-" in data[i][1]:
            if i+1 >= len(data)-1:
                break
            else:
                if "I-" in data[i+1][1]:
                    data[i] = (data[i][0]+"_"+data[i+1][0], data[i][1])
    filtered_data = [item for item in data if item[1] != 'I-PER' and item[1]
                     != 'I-LOC' and item[1] != 'I-MISC' and item[1] != 'I-ORG']

    # including color for streamlit in FE
    for token in filtered_data:
        if "PER" in token[1]:
            tokens.append((token[0], "PERSON", "#f5cac3"))
        elif "ORG" in token[1]:
            tokens.append((token[0], "ORGANIZATION", "#f28482"))
        elif "LOC" in token[1]:
            tokens.append((token[0], "LOCATION", "#f6a278"))
        elif "MISC" in token[1]:
            tokens.append((token[0], "MISCELLANEOUS", "#7bdff2"))
        else:
            tokens.append((token[0], " ", " "))
    return convert_ner(tokens)

# setup pos predictor
def pos_predictor(sentence: str):
    """
    :param sentence: user input
    :return: result POS tags
    """
    text_process = annotate_text(sentence)
    tokens = []
    for token in text_process:
        word, tag = token[0], token[2]
        # if tag not in tokens:
        tokens.append((word, tag))
    return convert_pos(tokens)
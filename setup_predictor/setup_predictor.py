from setup_predictor.main_predictor import annotate_text
from utils.utils import *
import torch
import joblib
from model.EntityCustomModel import EntityModel

# setup model
def setup_model():
    """
    This function used to load pre-trained model with init structure
    load pre-trained params to state_dict and resulting pre-trained model.
    Init device with "cuda" or "cpu"
    :return: pre-trained model
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    meta_data = joblib.load("../test_models/encoded.bin")
    enc_pos = meta_data["enc_pos"]
    enc_tag = meta_data["enc_tag"]
    num_poss = len(list(enc_pos.classes_))
    num_tagg = len(list(enc_tag.classes_))
    model = EntityModel(num_tag=num_tagg, num_pos=num_poss) # setup model structure
    model.load_state_dict(torch.load(
        '../test_models/best_model_crf.pth',
        map_location=torch.device('cpu'))) # load params of pre-trained model
    model.to(device) # setup model to device {GPU, CPU}

    return model

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
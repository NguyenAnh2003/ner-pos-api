from utils.utils import *
import torch
import re
import numpy as np
import requests
from custom_dataset.EntityDataset import EntityDataset
from setup.setup_model import setup_model
from dotenv import load_dotenv
# setup NER predictor
def ner_predictor(sentence: str):
    """ NER predictor
    :param sentence: user input
    :return: format string result
    """
    print(f"")
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
#word_segmentation
def word_segment(text: str):
    # API for segmentation
    API = "https://viettelgroup.ai/nlp/api/v1/segment"
    # sentences segment
    sent_reg = r'(?<!\w.\s\w.)(?<![A-Z][a-z]\.)(?<=\n|\.|\?|\!)\s'
    sentences = re.split(sent_reg, text)
    
    word_list2=[]
    for sentence in sentences:
        word_list = [] # init word list
        word_list1=[]
        response = requests.post(API, json={"sentence": sentence},
                                 headers={'Content-Type': 'application/json', 'token': 'Voice - tm7M...'})
        if response.status_code == 200:
            data = response.json()
            word_list1=[item['word'] for item in data['result']]
            for word in word_list1:
                words = word.split()
                word="_".join(words)
                word_list.append(word)
            print(word_list)
        else:
            print('Error:', response.status_code) #

        word_list2.append(word_list)
    return word_list2
# result of text -> ner pos 
def annotate_text(text):
    result = []
    word_list= word_segment(text)
    device,model,enc_pos,enc_tag = setup_model()
    for i in word_list:
        temp = []
        test_dataset = EntityDataset(
            texts=[i],
            pos=[[0] * len(i)],
            tags=[[0] * len(i)]
        )

        with torch.no_grad():
            data = test_dataset[0]
            for k, v in data.items():
                data[k] = v.to(device).unsqueeze(0)
            tag, pos, _, llll =  model(**data)

        tag = tag[0]
        pos = pos[0]
        tag = np.array(tag)
        poss = np.array(pos)
        ner =  enc_tag.inverse_transform(tag.flatten())
        pos = enc_pos.inverse_transform(poss.flatten())

        for j in range(len(i)):
            temp.append((i[j], ner[j], pos[j]))
        result += temp
    return result

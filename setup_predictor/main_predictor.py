import torch
import re
import numpy as np
import requests
from dataloader.EntityDataset import EntityDataset
from setup_predictor.loader import model, device, enc_tag, enc_pos
from dotenv import load_dotenv
import os
load_dotenv() # dotenv config
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

API = os.getenv("OUR_SEGMENTER_API")


def sent_seg(text):
    sent_reg = r'(?<!\w.\s\w.)(?<![A-Z][a-z]\.)(?<=\n|\.|\?|\!)\s'
    sents = re.split(sent_reg, text)
    print(sents) #
    return sents


def create_word_list(text):
    rs = []
    sentences = sent_seg(text)
    for sentence in sentences:
        word_list = [] # init word list
        response = requests.post(API, json={"string": sentence},
                                 headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            data = response.json()
            print(data) #
            ls = [i for i in data['tag']]
            for i in ls:
                print(i) #
                word_list.append(i)
            print(word_list)
        else:
            print('Error:', response.status_code) #

        rs.append(word_list)
    print(rs) #
    return rs


def final(word_list):
    result = []
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
            tag, pos, _, llll = model(**data)

        tag = tag[0]
        pos = pos[0]
        tag = np.array(tag)
        poss = np.array(pos)
        ner = enc_tag.inverse_transform(tag.flatten())
        pos = enc_pos.inverse_transform(poss.flatten())

        for j in range(len(i)):
            temp.append((i[j], ner[j], pos[j]))
        result += temp
    return result


def annotate_text(text: str):
    return final(create_word_list(text))

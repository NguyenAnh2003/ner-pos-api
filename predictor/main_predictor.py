import torch
import re
import numpy as np
import requests
from temp.models.entity_dataset import EntityDataset
from loader import model, device, enc_tag, enc_pos
# from dotenv import load_dotenv

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)


def sent_seg(text):
    sent_reg = r'(?<!\w.\s\w.)(?<![A-Z][a-z]\.)(?<=\n|\.|\?|\!)\s'
    sents = re.split(sent_reg, text)
    print(sents)
    return sents


API = "https://viettelgroup.ai/nlp/api/v1/segment"


def create_word_list(sentence):
    sentences = sent_seg(sentence)
    word_list2 = []
    for sentence in sentences:
        payload = {
            "sentence": sentence
        }
        headers = {
            'Content-Type': 'application/json',
            'token': 'Voice - tm7M...'
        }
        word_list = []
        word_list1 = []
        response = requests.post(API, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            word_list1 = [item['word'] for item in data['result']]
            for word in word_list1:
                words = word.split()
                word = "_".join(words)
                word_list.append(word)
        else:

            print('Error:', response.status_code)
        # output_list = []
        # previous_token = None
        #
        # for token in word_list:
        #     if token == '.' and previous_token == '.':
        #         output_list[-1] = '...'
        #     else:
        #         output_list.append(token)
        #         previous_token = token
        # word_list2.append(output_list)
        word_list2.append(word_list)
    return word_list2


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


def annotate_text(text):
    return final(create_word_list(text))

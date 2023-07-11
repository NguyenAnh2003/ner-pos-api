import torch
import numpy as np
import requests,json
from models.entity_dataset import EntityDataset
from loader import model, device, enc_tag, enc_pos
from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# API = os.environ.get("SEGMENTER_API")
API="https://viettelgroup.ai/nlp/api/v1/segment"
def annotate_text(sentence):
    payload = {
        "sentence":sentence
    }
    headers = {
        'Content-Type': 'application/json',
        'token': 'Voice - tm7M...'
    }
    word_list1 = []
    word_list = []
    response = requests.post(API, json=payload, headers=headers)
    if response.status_code == 200:
            data = response.json()
            word_list1 = [item['word'] for item in data['result']]
            for word in word_list1:
                words = word.split()
                word = "_".join(words)
                word_list.append(word)
            formatted_json = json.dumps(data, indent=4,ensure_ascii=False)
    else:

            print('Error:', response.status_code)

    test_dataset = EntityDataset(
        texts=[word_list],
        pos=[[0] * len(word_list)],
        tags=[[0] * len(word_list)]
    )

    with torch.no_grad():
        data = test_dataset[0]
        for k, v in data.items():
            data[k] = v.to(device).unsqueeze(0)
        tag, pos, _,llll = model(**data)


    tag=tag[0]
    pos= pos[0]
    tag=np.array(tag)
    poss=np.array(pos)
    ner = enc_tag.inverse_transform(tag.flatten())
    pos = enc_pos.inverse_transform(poss.flatten())

    result = []

    for i in range(len(word_list)):
          result.append((word_list[i], ner[i], pos[i]))
    return result

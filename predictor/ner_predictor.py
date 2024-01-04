from predictor.main_predictor import annotate_text
from predictor.converter import convert_ner


def ner_predictor(sentence: str):
    text_process = annotate_text(sentence)
    data = [(text[0], text[1]) for text in text_process]
    tokens = []
    i = 0

    while i < len(data):
        if 'B-' in data[i][1]:
            if i + 1 < len(data) and 'I-' in data[i + 1][1]:
                merged_entity = data[i][0] + "_" + data[i + 1][0]
                label = data[i][1]
                del data[i:i + 2]
                data.insert(i, (merged_entity, label)) 
            else:
                i += 1
        else:
            i += 1

    # including color for streamlit and Reactjs in FE
    for token in data:
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

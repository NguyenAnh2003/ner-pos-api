from predictor.main_predictor import annotate_text
from predictor.converter import convert_ner
def ner_predictor(sentence: str):
    text_process = annotate_text(sentence)
    tokens = []
    # including color for streamlit in FE
    for token in text_process:
        if "PER" in token[1]:
            tokens.append((token[0], "PERSON", "#fef6ce"))
        elif "ORG" in token[1]:
            tokens.append((token[0], "ORGANIZATION", "#d8f2fe"))
        elif "LOC" in token[1]:
            tokens.append((token[0], "LOCATION", "#f4cfdb"))
        elif "MISC" in token[1]:
            tokens.append((token[0], "MISCELLANEOUS", "#edfcd9"))
        else:
            tokens.append(" " + token[0] + " ")
    return convert_ner(tokens)

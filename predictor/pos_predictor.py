from predictor.main_predictor import annotate_text
from predictor.converter import convert_pos
from classes.Req import Req
def pos_predictor(req: Req):
    text_process = annotate_text(req)
    # print(text_process)
    tokens = []
    for token in text_process:
        word, tag = token[0], token[2]
        # if tag not in tokens:
        tokens.append((word, tag))
    return convert_pos(tokens)
import yaml

# load params using yaml
def load_params(path: str):
    """
    :param path: dir to yaml file
    :return: params included in yaml file
    """
    return yaml.safe_load(open(path, 'r', encoding='utf8'))

# convert pos tag
def convert_pos(tokens):
    def switch(text):
        x = ["A", "C", "CH", "E", "FW", "I", "L", "M", "N",
             "Nc", "Np", "Nu", "Ny", "P", "R", "T", "V", "Vy", "X"]
        y = ["tính từ", "liên từ", "dấu câu", "giới từ", "từ mượn", "cảm từ",
             "lượng từ", "số từ", "danh từ", "danh từ chỉ loại", "danh từ riêng",
             "danh từ chỉ đơn vị", "danh từ viết tắt", "đại từ", "phụ từ", "trợ từ",
             "động từ", "động từ viết tắt", "không xác định"]
        for i, e in enumerate(x):
            e = text
            if e == x[i]:
                return y[i]
    #
    result = []
    for i in tokens:
        result.append((i[0], switch(i[1])))
    return result

# convert ner tag
def convert_ner(tokens):
    def switch(text):
        x = ["PERSON", "LOCATION", "ORGANIZATION", "MISCELLANEOUS", " "]
        y = ["Người", "Địa điểm", "Tổ chức", "khác", " "]
        for i,e in enumerate(x):
            e = text
            if e == x[i]:
                return y[i]
    #
    result = []
    for i,e in enumerate(tokens):
        result.append((e[0], switch(e[1]), e[2]))
    return result
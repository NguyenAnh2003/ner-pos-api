# import matplotlib, scipy, sklearn
# import torchcrf
# import pydantic
#
# print(matplotlib._get_version())
# print(scipy.__version__)
# print(sklearn.__version__)
# print(torchcrf.__version__)
# print('pydantic', pydantic.__version__)

x = [' thủ_đô ', ('Việt_Nam', 'Địa điểm', '#84a59d'), ' là ', ('Hà_Nội', 'Địa điểm', '#84a59d')]

rs = []
data = {
        "str": "thủ_đô",

        "ent": [
            "Việt_Nam",
            "Địa điểm",
            "#f4cfdb"
        ],

        "str": "là",

        "ent": [
            "Hà_Nội",
            "Địa điểm",
            "#f4cfdb"
        ]
    }

x = [' thủ_đô ', ('Việt_Nam', 'Địa điểm', '#84a59d'), ' là ', ('Hà_Nội', 'Địa điểm', '#84a59d')]
str_a = []
tup_a = []

for i in x:
    if isinstance(i, str):
        str_a.append(i)

for i in x:
    if isinstance(i, tuple):
        tup_a.append(i)

print(str_a, tup_a)
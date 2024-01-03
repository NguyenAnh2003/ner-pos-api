x = [
  [
    "thủ_đô",
    " ",
    " "
  ],
  [
    "Việt_Nam",
    "Địa điểm",
    "#f4cfdb"
  ],
  [
    "là",
    " ",
    " "
  ],
  [
    "Hà_Nội",
    "Địa điểm",
    "#f4cfdb"
  ]
]

converted_list = []

for sublist in x:
    word = sublist[0]
    tag = sublist[1]
    color = sublist[2]
    converted_list.append({"word": word, "tag": tag, "color": color})

print(converted_list)
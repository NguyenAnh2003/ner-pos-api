# ner_pos_api
install dependencies
```python
pip install -r requirements.txt
```
run app
```python
uvicorn main:app --reload
```
## Extract with Vietnamese (POS)
```
[
  {
    "word": "thủ_đô",
    "tag": "danh từ"
  },
  {
    "word": "Việt_Nam",
    "tag": "danh từ riêng"
  },
  {
    "word": "là",
    "tag": "động từ"
  },
  {
    "word": "Hà_Nội",
    "tag": "danh từ riêng"
  }
]
```
## Extract with Vietnamese (NER)
```
[
  {
    "word": "thủ_đô",
    "tag": " ",
    "color": " "
  },
  {
    "word": "Việt_Nam",
    "tag": "Địa điểm",
    "color": "#f4cfdb"
  },
  {
    "word": "là",
    "tag": " ",
    "color": " "
  },
  {
    "word": "Hà_Nội",
    "tag": "Địa điểm",
    "color": "#f4cfdb"
  }
]
```

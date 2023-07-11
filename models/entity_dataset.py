from config.config import config
import torch

class EntityDataset:
    def __init__(self, texts, pos, tags):
        self.texts = texts
        self.pos = pos
        self.tags = tags
    def __len__(self):
        return len(self.texts)

    def __getitem__(self, item):
        text = self.texts[item]
        pos = self.pos[item]
        tags = self.tags[item]

        ids = []
        target_pos = []
        target_tag =[]
        mask=[]
        token_type_ids=[]


        inputs = config.TOKENIZER.encode(
                text,
                add_special_tokens=False
            )
        input_len = len(inputs)
        padding_len =config.MAX_LEN - input_len
        ids.extend(inputs + [0]*padding_len )
        target_pos.extend(pos+ [2]*padding_len)
        target_tag.extend(tags + [8]*padding_len)

        mask.extend([1] * input_len + [0]*padding_len)
        token_type_ids.extend([0]*config.MAX_LEN)

        return {
            "ids": torch.tensor(ids, dtype=torch.long),
            "mask": torch.tensor(mask, dtype=torch.long),
            "token_type_ids": torch.tensor(token_type_ids, dtype=torch.long),
            "target_pos": torch.tensor(target_pos, dtype=torch.long),
            "target_tag": torch.tensor(target_tag, dtype=torch.long),
        }

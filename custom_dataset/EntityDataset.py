import torch
from utils.utils import load_params
from transformers import AutoTokenizer

class EntityDataset:
    def __init__(self, texts, pos, tags, path: str = "../config/configs-variables.yml"):
        super().__init__()
        """ setup params directly in this file """
        self.params = load_params(path) # setup params
        self.texts = texts
        self.pos = pos
        self.tags = tags
        # config with params
        self.max_len = self.params['max_len']
        self.train_batch_size = self.params['train_batch_size']
        self.valid_batch_size = self.params['valid_batch_size']
        self.epochs = self.params['epochs']
        self.base_model = self.params['base_model']
        self.tokenizer = AutoTokenizer.from_pretrained(self.base_model,
                                                       do_lower_case=True)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, item):
        text = self.texts[item]
        pos = self.pos[item]
        tags = self.tags[item]

        ids = []
        target_pos = []
        target_tag = []
        mask = []
        token_type_ids = []

        inputs = self.tokenizer.encode(
            text,
            add_special_tokens=False
        )
        input_len = len(inputs)
        padding_len = self.max_len - input_len
        ids.extend(inputs + [0] * padding_len)
        target_pos.extend(pos + [2] * padding_len)
        target_tag.extend(tags + [8] * padding_len)

        mask.extend([1] * input_len + [0] * padding_len)
        token_type_ids.extend([0] * self.max_len)

        return {
            "ids": torch.tensor(ids, dtype=torch.long),
            "mask": torch.tensor(mask, dtype=torch.long),
            "token_type_ids": torch.tensor(token_type_ids, dtype=torch.long),
            "target_pos": torch.tensor(target_pos, dtype=torch.long),
            "target_tag": torch.tensor(target_tag, dtype=torch.long),
        }

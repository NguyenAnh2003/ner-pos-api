from utils.helpers import log_soft
import torch.nn as nn
from torchcrf import CRF
import torch
import transformers
from config.config import config

class EntityModel(nn.Module):
    def __init__(self, num_tag, num_pos):
        super(EntityModel, self).__init__()
        self.num_tag = num_tag
        self.num_pos = num_pos
        self.phobert = transformers.AutoModel.from_pretrained(config.BASE_MODEL_PATH,return_dict=False)
        self.bert_drop_1 = nn.Dropout(0.3)
        self.bert_drop_2 = nn.Dropout(0.3)
        self.out_tag = nn.Linear(768, self.num_tag)
        self.out_pos = nn.Linear(768, self.num_pos)
        self.crf = CRF(num_tag, batch_first = True)
        self.crf_pos = CRF(num_pos, batch_first = True)
    def forward(
        self,
        ids,
        mask,
        token_type_ids,
        target_pos,
        target_tag
    ):
        o1, _ = self.phobert(
            ids,
            attention_mask=mask,
            token_type_ids=token_type_ids
        )

        bo_tag = self.bert_drop_1(o1)
        bo_pos = self.bert_drop_2(o1)

        tag = self.out_tag(bo_tag)
        pos = self.out_pos(bo_pos)

        # pos_probs = F.softmax(pos, dim=-1)

        if target_tag is not None:
            loss_tag = -self.crf(log_soft(tag, 2), target_tag, mask=mask.type(torch.uint8), reduction='mean')
            prediction = self.crf.decode(tag, mask=mask.type(torch.uint8))


        else:
            prediction = self.crf.decode(tag, mask=mask.type(torch.uint8))
            # return prediction

        if target_pos is not None:
            loss_pos = -self.crf_pos(log_soft(pos, 2), target_pos, mask=mask.type(torch.uint8), reduction='mean')
            pos_prediction = self.crf_pos.decode(pos, mask=mask.type(torch.uint8))


        else:
            pos_prediction = self.crf_pos.decode(pos, mask=mask.type(torch.uint8))

        return prediction, pos_prediction,loss_tag,loss_pos

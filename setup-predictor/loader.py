import torch
import joblib
from temp.models.entity_model import EntityModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

meta_data = joblib.load("../test_models/encoded.bin")
enc_pos = meta_data["enc_pos"]
enc_tag = meta_data["enc_tag"]

num_poss = len(list(enc_pos.classes_))
num_tagg = len(list(enc_tag.classes_))
model = EntityModel(num_tag=num_tagg, num_pos=num_poss)
model.load_state_dict(torch.load(
    '../test_models/best_model_crf.pth', map_location=torch.device('cpu')))
model.to(device)
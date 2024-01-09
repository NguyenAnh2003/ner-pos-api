import torch
import joblib
from model.EntityCustomModel import EntityModel

# setup model
def setup_model():
    """
    This function used to load pre-trained model with init structure
    load pre-trained params to state_dict and resulting pre-trained model.
    Init device with "cuda" or "cpu"
    :return: pre-trained model
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    meta_data = joblib.load("test_models/encoded.bin")
    enc_pos = meta_data["enc_pos"]
    enc_tag = meta_data["enc_tag"]
    num_poss = len(list(enc_pos.classes_))
    num_tagg = len(list(enc_tag.classes_))
    model = EntityModel(num_tag=num_tagg, num_pos=num_poss) # setup model structure
    model.load_state_dict(torch.load(
        'test_models/best_model_crf.pth',
        map_location=torch.device('cpu'))) # load params of pre-trained model
    model.to(device) # setup model to device {GPU, CPU}

    return device, model, enc_pos, enc_tag
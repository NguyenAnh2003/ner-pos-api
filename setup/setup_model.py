import torch
import joblib
from model.EntityCustomModel import EntityModel
from setup.setup_encoded import setup_encoded_data
from setup.sys_utils import setup_device
# setup model
def setup_model(enc_tag, enc_pos, device):
    """
    This function used to load pre-trained model with init structure
    load pre-trained params to state_dict and resulting pre-trained model.
    Init device with "cuda" or "cpu"
    :return: pre-trained model
    """
    num_pos = len(list(enc_pos.classes_))
    num_tag = len(list(enc_tag.classes_))
    model = EntityModel(num_tag=num_tag, num_pos=num_pos) # setup model structure
    model.load_state_dict(torch.load(
        'test_models/best_model_crf.pth',
        map_location=torch.device('cpu'))) # load params of pre-trained model
    model.to(device) # setup model to device {GPU, CPU}

    return model
import torch

def setup_device():
    """ Setup device for inference
    :return: device
    """
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    return device
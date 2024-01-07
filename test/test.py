from model.EntityCustomModel import EntityModel
from custom_dataset.EntityDataset import EntityDataset
from setup_predictor.setup_model import setup_model
from setup_predictor.setup_predictor import *

""" code test for ner pos """
def testing_mode(rsentence: str):
    """
    :param rsentence: raw sentence for testing prediction
    ner, pos tag of model.
    :return: tokens with tag(ner, pos)
    """
    model = setup_model() # setup model

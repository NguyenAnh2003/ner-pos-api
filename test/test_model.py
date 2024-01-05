from setup_predictor.setup_model import setup_model
from setup_predictor.setup_predictor import *

# calling pre-trained model
model = setup_model()
print(f"Model: {model.state_dict()}")
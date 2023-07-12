import matplotlib, scipy, sklearn
import torchcrf
# print(matplotlib._get_version())
# print(scipy.__version__)
# print(sklearn.__version__)
# print(torchcrf.__version__)
from predictor.ner_predictor import ner_predictor

print(ner_predictor("thủ đô Việt Nam là Hà Nội"))
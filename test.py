import matplotlib, scipy, sklearn
import torchcrf
import pydantic

print(matplotlib._get_version())
print(scipy.__version__)
print(sklearn.__version__)
print(torchcrf.__version__)
print('pydantic', pydantic.__version__)

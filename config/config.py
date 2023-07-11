import transformers
class config:
    MAX_LEN = 149
    TRAIN_BATCH_SIZE = 32
    VALID_BATCH_SIZE = 8
    EPOCHS = 10
    BASE_MODEL_PATH = "vinai/phobert-base-v2"
    # MODEL_PATH = "/content/drive/MyDrive/Colab Notebooks/ner vietnam"
    # TRAINING_FILE = "/content/drive/MyDrive/Colab Notebooks/vietnam ner/train_2016_fixed.csv"
    # TESTING_FILE = "/content/drive/MyDrive/Colab Notebooks/vietnam ner/test_2016_fixed.csv"
    TOKENIZER = transformers.AutoTokenizer.from_pretrained(BASE_MODEL_PATH, do_lower_case=True)
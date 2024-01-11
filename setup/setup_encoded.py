import joblib

def setup_encoded_data():
    meta_data = joblib.load("test_models/encoded.bin")
    enc_pos = meta_data["enc_pos"]
    enc_tag = meta_data["enc_tag"]
    # num_pos = len(list(enc_pos.classes_))
    # num_tag = len(list(enc_tag.classes_))
    return enc_pos, enc_tag
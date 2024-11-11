from keras.models import load_model
import joblib
import numpy as np
import pandas as pd
from keras.preprocessing.sequence import pad_sequences

def apply_model_on_dataset(preprocessed_data_path, tokenizer_path, model_path):
    # Load preprocessed data
    encode = 'ISO-8859-1'
    df = pd.read_csv(preprocessed_data_path, encoding=encode)
    texts = df['preprocessed_text'].to_list()

    # Load tokenizer
    tokenizer = joblib.load(tokenizer_path)

    # Tokenize and pad sequences
    sequences = tokenizer.texts_to_sequences(texts)
    max_len = 100  # Same as used during training
    X = pad_sequences(sequences, maxlen=max_len)

    # Load the trained model
    model = load_model(model_path)

    # Predict
    predictions = model.predict(X)
    predictions = (predictions > 0.5).astype(int)  # Convert to binary

    return predictions

# Example usage
predictions = apply_model_on_dataset('path_to_preprocessed_data.csv', 'path_to_tokenizer.pkl', 'path_to_trained_model.keras')

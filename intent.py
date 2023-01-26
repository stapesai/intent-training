import pandas as pd
import tensorflow as tf
from tensorflow.python.keras.layers import Input, Dense, Flatten,Embedding
from tensorflow.python.keras.models import Model

# data_reader=pd.read_json("increase_volume.json")
tokenizer=tf.keras.preprocessing.text.Tokenizer()
texts = ["This is an example sentence.", "Here is another example sentence."]
tokenizer.fit_on_texts(texts)
input_layer = Input(shape=(None,), dtype='int32')

# Create the embedding layer
embedding_layer= Embedding(input_dim=1000, output_dim=128)(input_layer)

# Flatten the embedding layer
flatten_layer = Flatten()(embedding_layer)
model = Model(inputs=input_layer, outputs=flatten_layer)
model.compile(optimizer='adam', loss='categorical_crossentropy')


print(tokenizer.word_index)


# Tokenize the text data
sequences = tokenizer.texts_to_sequences(texts)
model.fit(sequences, epochs=10)
print(sequences)
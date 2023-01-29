import tensorflow as tf
import pandas as pd

# Create a DataFrame with sample text data
df = pd.DataFrame({'text': ['This is a sample text.',
                            'This sample is a text.',
                            'Another sample text.',
                            'Yet another sample text.']})

# Create an instance of TextVectorization layer
vectorizer = tf.keras.layers.TextVectorization(output_mode='int')

# Fit the vectorizer on the text data
vectorizer.adapt(df['text'].tolist())

# Get the vocabulary
vocab = vectorizer.get_vocabulary()
print(vocab)

# Vectorize the text data
vectorized_text = vectorizer(df['text'].tolist())
print(vectorized_text)

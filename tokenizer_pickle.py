import pickle
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer

# Load your dataset
df = pd.read_csv("balanced_reddit_comments_updated.csv")  # Ensure this file exists

# Create and fit tokenizer
tokenizer = Tokenizer(num_words=5000)
df["Processed_Comment"] = df["Processed_Comment"].astype(str).fillna("")
tokenizer.fit_on_texts(df["Processed_Comment"])  # Use the cleaned text column

# Save tokenizer to a file
with open("tokenizer.pickle", "wb") as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("✅ Tokenizer saved successfully!")

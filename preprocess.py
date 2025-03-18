import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    if pd.isna(text):  # Handle missing values
        return ""
    text = text.lower()
    words = word_tokenize(text)
    
    # Handle negation words (e.g., "not good" → "not_good")
    negation_words = {"not", "no", "never", "n't"}
    processed_words = []
    i = 0
    while i < len(words):
        if words[i] in negation_words and i + 1 < len(words):
            processed_words.append(words[i] + "_" + words[i + 1])  # Merge negation
            i += 1  # Skip next word since it's already merged
        else:
            processed_words.append(words[i])
        i += 1

    words = [lemmatizer.lemmatize(word) for word in processed_words if word.isalnum() and word not in stop_words]
    return " ".join(words)

# Load dataset
df = pd.read_csv("balanced_reddit_comments.csv")

# Apply preprocessing
df["Processed_Comment"] = df["Comment"].apply(preprocess_text)

# Save updated dataset
df.to_csv("balanced_reddit_comments_updated.csv", index=False)

print("Preprocessing complete! New dataset saved as 'balanced_reddit_comments_updated.csv'.")

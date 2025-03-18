# Install these packages before running this script  
# pip install textblob
# pip install vaderSentiment

import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the dataset
df = pd.read_csv("reddit_comments.csv")  

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    if pd.isna(text) or not isinstance(text, str) or text.strip() == "":
        return "neutral"

    scores = analyzer.polarity_scores(text)
    print(f"🔹 Text: {text} | VADER Scores: {scores}")  # Debugging

    if scores["compound"] > 0.3:
        return "positive"
    elif scores["compound"] < -0.3:
        return "negative"
    else:
        return "neutral"

df["Sentiment"] = df["Comment"].apply(get_sentiment)


# Save the labeled dataset
df.to_csv("labeled_reddit_comments.csv", index=False)

print(" Sentiment labeling complete! Labeled data saved as 'labeled_reddit_comments.csv'.")

print(get_sentiment("I love this product!"))  # Expected: Positive
print(get_sentiment("This is the worst experience ever."))  # Expected: Negative
print(get_sentiment("The book was okay, nothing special."))  # Expected: Neutral

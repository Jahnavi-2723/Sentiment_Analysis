from flask import Flask, request, render_template, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import io
import base64
import os

app = Flask(__name__)

# Constants
MAX_LEN = 60  
MODEL_PATH = "lstm_sentiment_model.h5"
TOKENIZER_PATH = "tokenizer.pickle"

# Load Model & Tokenizer
if os.path.exists(MODEL_PATH) and os.path.exists(TOKENIZER_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
    with open(TOKENIZER_PATH, "rb") as handle:
        tokenizer = pickle.load(handle)
    print("✅ Model & Tokenizer loaded successfully!")
else:
    print("❌ ERROR: Model or tokenizer file is missing!")
    model, tokenizer = None, None

# Function to generate pie chart and return Base64 encoded image
def create_pie_chart(predictions):
    labels = predictions.keys()
    sizes = predictions.values()
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.title("Prediction Distribution")
    
    # Save plot to a BytesIO object
    img_io = io.BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)
    plt.close()

    # Convert image to Base64 string
    encoded_img = base64.b64encode(img_io.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{encoded_img}"


# Route for File Upload & Sentiment Prediction
@app.route("/")
def home():
    return render_template("frontend.html")  # Ensure frontend.html is in "templates" folder

@app.route("/predict", methods=["POST"])
def predict():
    if model is None or tokenizer is None:
        return jsonify({"error": "Model or tokenizer not loaded. Check server logs."}), 500

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded!"}), 400

    file = request.files["file"]

    # Validate if it's a CSV file
    if not file.filename.endswith(".csv"):
        return jsonify({"error": "Invalid file format. Please upload a CSV file."}), 400

    try:
        # Load file
        df = pd.read_csv(file)

        # Check if the required column exists
        if "Comment" not in df.columns:
            return jsonify({"error": "CSV must have a 'Comment' column."}), 400

        comments = df["Comment"].astype(str).tolist()  # Ensure text format

        # Convert text to sequences and pad them
        sequences = tokenizer.texts_to_sequences(comments)
        padded = pad_sequences(sequences, maxlen=MAX_LEN)

        # Make Predictions
        predictions = model.predict(padded)
        sentiment_labels = ["Negative", "Positive", "Neutral"]
        df["Sentiment"] = [sentiment_labels[i] for i in predictions.argmax(axis=1)]

        # Calculate Sentiment Distribution
        sentiment_counts = df["Sentiment"].value_counts().to_dict()

        # Generate pie chart
        pie_chart_url = create_pie_chart(sentiment_counts)

        # Render results.html with predictions and pie chart
        return render_template("results.html", predictions=df.to_dict(orient="records"), pie_chart_url=pie_chart_url)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

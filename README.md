#  Sentiment Analysis using LSTM  

Social media has become an integral part of our lives, where users frequently post comments, likes, and reactions.  
Every post can have different perspectives based on its reach and engagement.  

This project analyzes user comments using an **LSTM (Long Short-Term Memory) model** to classify sentiments.  
It involves **data extraction, preprocessing, balancing, training, and testing** to ensure accurate sentiment classification.  
The model is trained using **Reddit comments dataset**.  

---

##  Features  
✔️ Upload a `.csv` file with a **"Comment"** column  
✔️ Perform **Sentiment Analysis** using a **pre-trained LSTM model**  
✔️ Display **predictions in a tabular format**  
✔️ Generate a **pie chart** to visualize sentiment distribution  
✔️ Built using **Flask, TensorFlow, Pandas, Matplotlib**  

---

##  Tech Stack  
**Backend:**  
- Flask  
- TensorFlow  
- Keras  
- Pandas  

**Frontend:**  
- HTML  
- CSS  
- Bootstrap  

**Visualization:**  
- Matplotlib  

---

## Usage Instructions  

1️⃣ **Upload** a CSV file with a column named `"Comment"`.  
2️⃣ The **LSTM model** predicts sentiments: **Positive, Negative, or Neutral**.  
3️⃣ The results are displayed in **tabular format**.  
4️⃣ A **pie chart** visualizes the sentiment distribution on the same page.  

---

##  Demo Screenshot  
![Screenshot 2025-03-18 160529](https://github.com/user-attachments/assets/92ccfdaa-03ca-4839-bea5-b75556817d7d)
![Screenshot 2025-03-18 160518](https://github.com/user-attachments/assets/e37490e9-d3b5-41a7-bccc-bb2c89b5b6e3)
![Screenshot 2025-03-18 160501](https://github.com/user-attachments/assets/aae435eb-e87c-4762-b651-6ce83e195e80)


---

##  Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/Jahnavi-2723/Sentiment-Analysis.git
   cd Sentiment-Analysis
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the Application:
   ```bash
   python api.py
4. Open your browser and go to:
   ```cpp
   http://127.0.0.1:5000/



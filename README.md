# 📌 Sentiment Analysis App

This is a **Sentiment Analysis Web App** built using **Streamlit**, `transformers`, and `DistilBERT`. The app takes user input text and predicts whether the sentiment is **Positive** or **Negative**.

---

## 🚀 Features
✔️ User-friendly UI with **Streamlit**  
✔️ Uses **Hugging Face Transformers** (`DistilBERT`) for sentiment prediction  
✔️ Lightweight and fast inference  
✔️ Deployable on local or cloud servers  

---

## 📂 Project Structure
Sentiment Analysis/ │── sentiment_model/ # Pretrained model files │ ├── config.json │ ├── model.safetensors │ ├── tokenizer.json │── myenv/ # Virtual Environment (optional) │── app.py # Streamlit Web App │── requirements.txt # Dependencies │── README.md # Project Documentation



## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Sentiment-Analysis-App.git
cd Sentiment-Analysis-App

2️⃣ Create a Virtual Environment (Optional)
python -m venv myenv
source myenv/bin/activate   # On macOS/Linux
myenv\Scripts\activate      # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit App
streamlit run app.py

📢 Usage
Enter a sentence in the input field.
Click "Analyze" to get the sentiment prediction.
The model returns Positive or Negative sentiment along with a confidence score.

👨‍💻 Technologies Used
Python 3.x
Streamlit
Hugging Face Transformers
DistilBERT
PyTorch

📜 License
This project is open-source and free to use.

✨ Author
Your Arman Ali
https://github.com/armanali-400 |  linkedin.com/in/armana002

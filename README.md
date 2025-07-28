
🎯 Customer Churn Prediction using Random Forest and Gradio  
This repository contains a machine learning web app that predicts whether a customer is likely to churn using a trained **Random Forest Classifier**. The app is built with **Gradio** and deployed on **Hugging Face Spaces**.

🚀 Live Demo  
You can try the app instantly on Hugging Face Spaces:  
👉 https://huggingface.co/spaces/Trashika112/Customer-Churn-Prediction

📌 Project Description  
Customer churn prediction helps businesses identify customers who are likely to leave their service. This project includes:

✅ Random Forest Model: Robust and interpretable classification algorithm  
✅ Gradio Web App: Simple and interactive UI hosted online  
✅ User Input Form: Collects customer attributes via a form interface  
✅ Binary Classification: Predicts if the customer will churn (Yes/No)

🛠️ Setup and Usage  
1. Clone the Repository  
```bash
git clone https://github.com/Trashika112/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

2. Install Dependencies  
```bash
pip install -r requirements.txt
```

3. Run the App  
```bash
python app.py
```

📁 Project Files  
- `app.py` – Gradio app script for churn prediction  
- `churn_model_rf.pkl` – Trained Random Forest model  
- `requirements.txt` – Python dependency list  
- `README.md` – Project overview and instructions

📦 Dependencies  
- gradio  
- scikit-learn  
- pandas  
- numpy  
- joblib  

Install them using:  
```bash
pip install -r requirements.txt
```

📊 Dataset  
The model was trained on a kaggle dataset.

- Credit Score  
- Geography (France, Germany, Spain)  
- Gender  
- Age  
- Tenure (Years with bank)  
- Account Balance  
- Number of Products  
- Has Credit Card  
- Is Active Member  
- Estimated Salary  
- Exited (Target: 1 = Churn, 0 = No Churn)  

🤝 Contributing  
Contributions are welcome!  
If you'd like to contribute:

- Fork the repository  
- Create a new feature branch  
- Commit your changes  
- Push to your branch  
- Open a pull request  

🔮 Future Work  
🔁 Add advanced models like XGBoost or Deep Learning (e.g., BERT for textual input)  
📱 Build a mobile-friendly UI  
📉 Add prediction confidence or probability output  
📊 Visualize important features affecting churn

📄 License  
This project is licensed under the MIT License.

👩‍💻 Author  
Trashika S Karkera  

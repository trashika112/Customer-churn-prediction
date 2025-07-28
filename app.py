import gradio as gr
import joblib
import numpy as np

# Load the model
model = joblib.load("churn_model_rf.pkl")

# Prediction function
def predict_churn(credit_score, gender, age, tenure, balance, products, has_card, active, salary, geography):
    gender = 1 if gender == "Male" else 0
    has_card = int(has_card)
    active = int(active)

    # One-hot encode geography
    geo_Germany = 1 if geography == "Germany" else 0
    geo_Spain = 1 if geography == "Spain" else 0

    # Feature vector
    input_data = np.array([[credit_score, gender, age, tenure, balance,
                            products, has_card, active, salary,
                            geo_Germany, geo_Spain]])
    
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        return "⚠️ Churn Likely!"
    else:
        return "✅ Not Likely to Churn"

# Gradio Interface
demo = gr.Interface(
    fn=predict_churn,
    inputs=[
        gr.Slider(300, 850, label="💳 Credit Score", value=650),
        gr.Radio(["Male", "Female"], label="👤 Gender", value="Male"),
        gr.Slider(18, 100, label="🎂 Age", value=35),
        gr.Slider(0, 10, label="🏢 Tenure (Years)", value=5),
        gr.Number(label="💰 Account Balance", value=100000),
        gr.Slider(1, 4, step=1, label="📦 Number of Products", value=1),
        gr.Checkbox(label="💳 Has Credit Card", value=True),
        gr.Checkbox(label="✅ Is Active Member", value=True),
        gr.Number(label="💵 Estimated Salary", value=50000),
        gr.Dropdown(["France", "Germany", "Spain"], label="🌍 Geography", value="France")
    ],
    outputs=gr.Textbox(label="📢 Prediction"),
    title="📊 Customer Churn Prediction App",
    description="🔍 Fill in customer details and click **Submit** to get churn prediction. Click **Clear** to reset the form.",
    allow_flagging="never",
    live=False
)

demo.launch()

import gradio as gr
import numpy as np
import joblib

# Load the model
model = joblib.load("churn_model_rf.pkl")

# Prediction function
def predict_churn(credit_score, gender, age, tenure, balance, num_of_products,
                  has_credit_card, is_active_member, estimated_salary, geography):
    
    gender_binary = 1 if gender == "Male" else 0
    geography_map = {"France": 0, "Germany": 1, "Spain": 2}
    geo = geography_map.get(geography, 0)

    input_data = np.array([[credit_score, gender_binary, age, tenure, balance,
                            num_of_products, int(has_credit_card),
                            int(is_active_member), estimated_salary, geo]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        return f"⚠️ Churn Likely! (Confidence: {probability:.2%})"
    else:
        return f"✅ Customer Likely to Stay. (Confidence: {1 - probability:.2%})"

# Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🧠 Customer Churn Predictor")
    gr.Markdown("Enter the details below to predict churn likelihood.")

    credit_score = gr.Slider(300, 850, value=650, label="💳 Credit Score")
    gender = gr.Radio(["Male", "Female"], value="Male", label="👤 Gender")
    age = gr.Slider(18, 100, value=35, label="🎂 Age")
    tenure = gr.Slider(0, 10, value=5, label="📆 Tenure (Years)")
    balance = gr.Number(value=100000, label="💰 Account Balance")
    num_products = gr.Slider(1, 4, value=1, label="📦 Number of Products")
    has_card = gr.Checkbox(label="💳 Has Credit Card", value=True)
    is_active = gr.Checkbox(label="✅ Is Active Member", value=True)
    salary = gr.Number(value=50000, label="💵 Estimated Salary")
    geography = gr.Dropdown(["France", "Germany", "Spain"], value="France", label="🌍 Geography")

    output = gr.Textbox(label="📊 Result")
    submit = gr.Button("🔍 Predict")

    submit.click(fn=predict_churn,
                 inputs=[credit_score, gender, age, tenure, balance,
                         num_products, has_card, is_active, salary, geography],
                 outputs=output)

# Run the app
if __name__ == "__main__":
    demo.launch()

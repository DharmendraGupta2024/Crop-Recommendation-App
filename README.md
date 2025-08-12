# 🌾 Crop Recommendation System

## 📖 Introduction
This project is a **machine learning-based system** that recommends the best crop to cultivate based on various environmental and soil parameters.  
By analyzing factors such as **nutrient levels, temperature, humidity, pH, and rainfall**, the system helps farmers make **data-driven decisions** to maximize yield and profitability.

---

## ✨ Features
- **Crop Recommendation:** Suggests the most suitable crop for given soil and environmental conditions.  
- **Data-Driven Insights:** Uses a dataset of crop requirements for accurate predictions.  
- **User-Friendly:** Simple interface requiring minimal inputs for results.  

---

## 🚀 Live Demo
🔗 **[Try the Application Here](https://crop-recommendation-app-project.onrender.com)**

---

## 📸 Screenshots

**Home Page / Recommendation Interface**  
![Home Page](https://raw.githubusercontent.com/DharmendraGupta2024/Crop-Recommendation-App/main/images/home-page.png)

**About Me Section**  
![About Me](https://raw.githubusercontent.com/DharmendraGupta2024/Crop-Recommendation-App/main/images/about-me.png)

**Contact Page**  
![Contact Page](https://raw.githubusercontent.com/DharmendraGupta2024/Crop-Recommendation-App/main/images/contact-page.png)

---

## 💻 Technologies & Libraries
Built using **Python** with the following libraries:
- **Flask** – Backend micro-framework
- **Gunicorn** – WSGI HTTP server
- **Scikit-learn** – ML model implementation (Random Forest Classifier)
- **Pandas, NumPy** – Data manipulation and computation
- **Matplotlib, Seaborn** – Visualization
- **Joblib, Threadpoolctl** – Model saving & loading

---

## ⚙️ Installation & Setup

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/DharmendraGupta2024/Crop-Recommendation-App.git
cd Crop-Recommendation-App

2️⃣ Create a virtual environment:
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

3️⃣ Install dependencies:
pip install -r requirements.txt

▶️ Usage
Run the application:
# Development mode
flask run
# Or with Gunicorn (production)
gunicorn app:app

▶️Open browser:
Go to http://127.0.0.1:5000
```


## Enter required parameters:

Nitrogen

Phosphorus

Potassium

Temperature

Humidity

pH

Rainfall


---
**Click Get Recommendation to view the best crop suggestion.**


---
***🤝 Contributing***
Contributions are welcome! Please open an issue or submit a pull request for suggestions, bug reports, or improvements.


---
***📜 License***
© 2025 Crop Recommendation System. All Rights Reserved.


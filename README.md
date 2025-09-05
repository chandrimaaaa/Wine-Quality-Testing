# 🍷 Wine Quality Prediction: From Analysis to Deployment

An **end-to-end Machine Learning project** that predicts wine quality from physicochemical properties, culminating in a functional **Django web application** for live predictions.

---

## 📖 Table of Contents
- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Setup and Installation](#️-setup-and-installation)
- [Analytical Workflow](#-analytical-workflow)
- [Running the Web App](#️-running-the-web-app)
- [Key Findings & Model Performance](#-key-findings--model-performance)
- [Future Scope](#-future-scope)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## 🎯 About The Project
Traditionally, wine quality assessment is a **subjective and costly** process performed by human experts.  
This project demonstrates how **data science** can provide an **objective, scalable, and efficient** alternative.

By analyzing a dataset of chemical properties for thousands of *Vinho Verde* wine samples, this project builds and evaluates **machine learning models** to predict quality scores.

The project addresses the problem from two angles:
- **Regression Task** → Predict the exact quality score  
- **Classification Task** → Identify high-quality wines  

The final **champion model** is integrated into a **Django web application**, transforming the analytical findings into a practical, interactive tool.

---

## ✨ Key Features
- 📊 **Comprehensive Data Analysis** – In-depth EDA to uncover relationships and data distributions  
- 🤖 **Dual Modeling Approach** – Regression & Classification models  
- 🔍 **Rigorous Model Selection** – Multiple algorithms tested & tuned with GridSearchCV  
- 📈 **Actionable Insights** – Feature importance reveals key drivers of wine quality  
- 🌐 **Interactive Web Application** – Django app for live wine quality predictions  
- 📚 **Reproducible Workflow** – Structured Jupyter notebooks  

---

## 🛠️ Technology Stack
**Language**  
- Python 3.10+  

**Core ML/DS Libraries**  
- [Scikit-learn](https://scikit-learn.org/)  
- [Pandas](https://pandas.pydata.org/)  
- [NumPy](https://numpy.org/)  

**Visualization**  
- [Matplotlib](https://matplotlib.org/)  
- [Seaborn](https://seaborn.pydata.org/)  

**Web Framework**  
- [Django](https://www.djangoproject.com/)  

**Others**  
- Joblib → Model persistence  
- Jupyter Notebook → Iterative model development  

---

## ⚙️ Setup and Installation

### 1. Prerequisites
Make sure you have installed:
- Git  
- Python **3.10+**  

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/wine-quality-prediction.git
cd wine-quality-prediction
````

### 3. Create Virtual Environment & Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🔬 Analytical Workflow

The project analysis is structured into **five Jupyter notebooks** located in the `notebooks/` directory.

Run them in order to reproduce the workflow:

1. **01\_data\_cleaning\_eda.ipynb** → Data loading, cleaning & EDA
2. **02\_preprocess\_and\_features.ipynb** → Feature engineering & baseline models
3. **03\_regression\_models.ipynb** → Training & tuning regression models
4. **04\_classification\_models.ipynb** → Training & tuning classification models
5. **05\_analysis\_and\_summary.ipynb** → Consolidated results & champion model

---

## ▶️ Running the Web App

Navigate to the Django app folder:

```bash
cd django-wine-app
```

Ensure the **champion model** exists:

```bash
django-wine-app/models/champion_wine_quality_model.pkl
```

Run the development server:

```bash
python manage.py runserver
```

Now, open your browser at 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

You can use the form to **get live predictions**!

---

## 📊 Key Findings & Model Performance

**Regression Task**

* Champion Model: **Tuned Random Forest Regressor**
* Test RMSE: **0.680**
* Test R²: **0.40**

**Classification Task**

* Champion Model: **Tuned SVM**
* Test F1-Score (Good class): **0.61**
* Test Accuracy: **85.0%**

**Most Important Features**

1. Alcohol
2. Density
3. Volatile Acidity

---

## 🚀 Future Scope

* 🔥 Advanced Models: Try XGBoost / LightGBM
* 🧠 Deeper Interpretation: SHAP for model explainability
* ☁️ Production Deployment: Dockerize & deploy to AWS/GCP
* 🎨 Enhanced UI/UX: Add user accounts, history & interactive dashboards

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

Dataset: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality)

> P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
> *Modeling wine preferences by data mining from physicochemical properties.*
> In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

```

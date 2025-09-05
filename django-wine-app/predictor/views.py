from django.shortcuts import render
import pandas as pd
import numpy as np
import joblib
import os
from django.conf import settings

# Path to the saved model
MODEL_PATH = os.path.join(settings.BASE_DIR, 'models', 'champion_wine_quality_model.pkl')

def predict_quality(request):
    """
    Handles both displaying the form (GET) and processing the prediction (POST).
    """
    prediction_result = None
    prediction_text = None
    error_message = None

    if request.method == 'POST':
        try:
            # --- 1. Load the pre-trained model ---
            model = joblib.load(MODEL_PATH)

            # --- 2. Get user input from the form ---
            # Using .get() with a default value to prevent errors if a field is empty
            alcohol = float(request.POST.get('alcohol', 0))
            volatile_acidity = float(request.POST.get('volatile_acidity', 0))
            sulphates = float(request.POST.get('sulphates', 0))
            density = float(request.POST.get('density', 0))
            total_sulfur_dioxide = float(request.POST.get('total_sulfur_dioxide', 0))
            wine_type = request.POST.get('wine_type', 'red')

            # --- 3. Create a DataFrame for prediction ---
            # The model was trained on 12 features. We provide inputs for the most
            # important ones and use reasonable defaults (mean values) for the others.
            feature_dict = {
                'fixed acidity': 7.2, # Mean value
                'volatile acidity': volatile_acidity,
                'citric acid': 0.32, # Mean value
                'residual sugar': 5.4, # Mean value
                'chlorides': 0.05, # Mean value
                'free sulfur dioxide': 30.5, # Mean value
                'total sulfur dioxide': total_sulfur_dioxide,
                'density': density,
                'pH': 3.2, # Mean value
                'sulphates': sulphates,
                'alcohol': alcohol,
                'wine_type': wine_type
            }
            
            input_df = pd.DataFrame([feature_dict])

            # --- 4. Perform the same feature engineering as in training ---
            input_df['acid_ratio'] = input_df['fixed acidity'] / (input_df['volatile acidity'] + 1e-6)
            input_df['density_alcohol_interaction'] = input_df['density'] * input_df['alcohol']

            # --- 5. Make a prediction ---
            # The pipeline will handle preprocessing automatically
            prediction = model.predict(input_df)
            prediction_result = int(prediction[0])

            if prediction_result == 1:
                prediction_text = "Good Quality Wine"
            else:
                prediction_text = "Not-Good Quality Wine"

        except FileNotFoundError:
            error_message = "Error: Model file not found. Please ensure 'champion_wine_quality_model.pkl' is in the 'models' directory."
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"

    # --- 6. Render the page ---
    context = {
        'prediction_text': prediction_text,
        'error_message': error_message,
        'form_data': request.POST if request.method == 'POST' else None
    }
    return render(request, 'predictor/index.html', context)

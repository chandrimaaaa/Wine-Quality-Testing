Wine Quality Prediction - Django App
This is a simple Django web application that uses a pre-trained machine learning model to predict wine quality based on its chemical properties.

Project Structure
django-wine-app/
├── models/
│   └── champion_wine_quality_model.pkl  <-- PLACE YOUR SAVED MODEL HERE
├── manage.py
├── predictor/
│   ├── templates/
│   │   └── predictor/
│   │       └── index.html
│   ├── urls.py
│   └── views.py
├── requirements.txt
└── wine_predictor/
    ├── settings.py
    └── urls.py

Setup and Local Deployment
1. Prerequisite: Place Your Model
Crucial Step: Find the champion_wine_quality_model.pkl file you created in the previous steps.

Create a models/ directory at the root of this Django project.

Place the .pkl file inside the models/ directory. The application will not work without it.

2. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

# In your project's root directory (django-wine-app)
python -m venv venv

Activate the environment:

Windows: venv\Scripts\activate

macOS/Linux: source venv/bin/activate

3. Install Dependencies
Install all the required Python packages from requirements.txt.

pip install -r requirements.txt

4. Run the Django Server
Once the dependencies are installed, you can run the local development server.

python manage.py runserver

Open your web browser and navigate to https://www.google.com/search?q=http://127.0.0.1:8000/. You should see the wine quality prediction form.

Deployment to PythonAnywhere
Sign Up: Create a free "Beginner" account on PythonAnywhere.

Upload Files:

Go to the "Files" tab in your PythonAnywhere dashboard.

Upload all your project files and folders (manage.py, requirements.txt, the predictor folder, wine_predictor folder, and the models folder with your .pkl file).

Create a Web App:

Go to the "Web" tab and click "Add a new web app".

Follow the prompts. When asked to select a Python web framework, choose "Django".

When asked for the Python version, choose the one you used for development (e.g., Python 3.10 or newer).

It will automatically create a virtual environment for you.

Configure the Web App:

In the "Code" section on the "Web" tab, click the link to your WSGI configuration file. It will look something like /var/www/yourusername_pythonanywhere_com_wsgi.py.

Edit this file. Delete the default content and replace it with the content below, making sure to replace "yourusername" with your actual PythonAnywhere username.

import os
import sys

# Add your project directory to the Python path
path = '/home/yourusername/django-wine-app' # <-- CHANGE THIS
if path not in sys.path:
    sys.path.insert(0, path)

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'wine_predictor.settings'

# Import the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

Install Dependencies:

Go to the "Consoles" tab and open a Bash console.

This console will be inside your PythonAnywhere environment. Navigate to your project directory.

Install the requirements into the virtual environment PythonAnywhere created for your web app.

# Replace the path with the one shown on the "Web" tab for your virtualenv
pip install --python /home/yourusername/.virtualenvs/your-virtualenv-name/bin/python3 -r requirements.txt

Reload and Visit:

Go back to the "Web" tab and click the big green "Reload" button.

Click the link to your site (e.g., yourusername.pythonanywhere.com). Your app should now be live!
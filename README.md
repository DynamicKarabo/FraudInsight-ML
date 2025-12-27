🚀 Local Installation & Setup
To run the FRAUD_OS.v2 terminal on your local machine, follow these steps:

1. Environment Configuration
Clone the repository and initialize a clean Python virtual environment to manage dependencies:

PowerShell

# Clone the repository
git clone <your-repo-link>
cd fraud_insight_dashboard

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate
2. Dependency Injection
Install the specialized libraries required for Random Forest inference and the Django web framework:

PowerShell

pip install -r requirements.txt
3. Database & Model Warm-up
Initialize the Django SQLite backend and start the development server:

PowerShell

python manage.py migrate
python manage.py runserver
4. Access the Terminal
Once the server is live, navigate to the local host address to interact with the monitor:

URL: http://127.0.0.1:8000/dashboard/

🛠️ Developer Notes
Data Integrity: Ensure the creditcard.csv is located in the /data folder. The system uses this for real-time transaction sampling.

Inference Speed: Local execution allows the Random Forest model to perform classification in <50ms, bypassing the "Cold Start" latency found in cloud-native serverless functions.

Model Weights: The pre-trained fraud_model.pkl is located in dashboard/ml_assets/. If the file is missing, run the training script in the /scripts directory.
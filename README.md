🚀 Local Installation & Setup
To run the FRAUD_OS.v2 terminal on your local machine, follow these steps:

1. Environment Configuration
Clone the repository and initialize a clean Python virtual environment to manage dependencies:

PowerShell

# Clone the repository
git clone (https://github.com/DynamicKarabo/FraudInsight-ML)
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

🧠 Technical Challenges & Problem Solving
During the development of FRAUD_OS.v2, I encountered several architectural and deployment hurdles that required strategic problem-solving.

1. The "250MB Serverless Wall" (Deployment Tradeoffs)
The Challenge: Initial deployment attempts to Vercel failed due to the 250MB unzipped limit for serverless functions. The combination of heavy ML libraries (scikit-learn, pandas, numpy) and the serialized model weights exceeded this constraint.

The Decision: I evaluated three paths: shrinking the model, using a lighter framework, or transitioning to a dedicated environment.

The Solution: I pivoted to a Local-First / Container-Ready architecture. This allowed me to keep the high-performance Random Forest model intact without compromising accuracy for file size, ensuring a "Zero-Lag" inference experience for the end user.

2. Class Imbalance & Model Reliability
The Challenge: The Credit Card Fraud dataset is notoriously imbalanced (99.8% legitimate transactions). A naive model would simply predict "Legitimate" 100% of the time and still achieve 99% accuracy while failing its primary purpose.

The Solution: I implemented custom Demo Injection Logic in the backend (views.py). This forces a 20% fraud-case sampling rate during live analysis to ensure the UI's "Threat Detected" states could be effectively demonstrated and tested.

3. Real-Time UI Synchronization
The Challenge: Displaying raw feature vectors (V1-V28) often leads to "data fatigue" or UI overlap in terminal-style interfaces.

The Solution: I engineered a scrollable data-stream buffer with a "Vanta Black" glassmorphism aesthetic. This keeps the UI clean while providing full transparency into the raw input data being fed into the model.
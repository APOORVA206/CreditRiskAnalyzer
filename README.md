Credit Risk Analyzer

This project is a full-stack machine learning solution that predicts loan default risk based on applicant features like age, income, and loan amount. It demonstrates seamless integration between a Python-based machine learning model and a Java-based client using REST API communication.
Project Overview
- Developed a Credit Risk Prediction system using Logistic Regression.
- Created a Python Flask microservice to serve the ML model as a REST API.
- Built a Java client to interact with the Flask API by sending applicant data and receiving prediction results.
- Showcases real-time prediction capability using HTTP requests and JSON handling.
 Tech Stack

Machine Learning: Python, scikit-learn, joblib
API Backend: Flask
Client:Java (HttpURLConnection)
Tools:VS Code, Git, GitHub

Project Structure
python_service: Contains the ML model, Flask API, and training script.
java_client: Java client code to send requests to the Flask server.
model: Folder to store the serialized model file (`.pkl`).




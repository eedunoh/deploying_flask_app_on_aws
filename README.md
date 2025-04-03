# Description
This repository contains Python, HTML, and necessary files for a cloud project on deploying a highly scalable Flask web application on AWS with Auto Scaling Group, Application Load Balancer, and managed DynamoDB & S3 storage


## Project Structure
- **app.py**: Contains the core Flask application logic (routes for login, signup, and dashboard). Manages the login process with AWS Cognito and renders the homepage for authenticated users.
  
- **templates/**: Contains HTML files rendered by Flask for the frontend.
  - **signup.html**: Handles user registration.
  - **login.html**: Handles user login.
  - **home.html**: Displays the static file upload app homepage for authenticated users.
    
- **requirements.txt**: Specifies Python dependencies like Flask, boto3 (for AWS services), and any other libraries the app needs.
  
- **utils.py**: Includes helper functions like `authenticate_user()` and `register_user()` that interact with AWS Cognito for user authentication and sign-up.
  
- **config.py**: A configuration file that interacts with the AWS SSM Parameter store to fetch Cognito secrets, store environment variables and settings for the Flask application.
  
- **Dockerfile**: Contains instructions for building the Docker image (e.g., install dependencies, copy app code, run the app).
  
- **run.sh**: A shell script used to set environment variables (e.g., FLASK_APP, FLASK_ENV) and run the Flask application within the Docker container.

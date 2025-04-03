# Description
This repository contains Python, HTML, and necessary files for a cloud project on deploying a highly scalable Flask web application on AWS with Auto Scaling Group, Application Load Balancer, and managed DynamoDB & S3 storage

## Architecture Diagram

![image](https://github.com/user-attachments/assets/7ee127a8-06cd-4fa6-868d-16afa85cb982)


## Project Structure
- **app.py**: Contains the core Flask application logic, built using python. Manages file upload and stores uploaded files in the correct storage option.
    
- **requirements.txt**: Specifies Python dependencies like Flask, boto3 (for AWS services), pymysql, mysql-connector-python, and any other libraries the app needs. 
  
- **Dockerfile**: Contains instructions for building the Docker image (e.g., install dependencies, copy app code, run the app).
  
- **Docker-Compose.yml**: Stores environment variables and services
  
- **run.sh**: A shell script used to set environment variables (e.g., FLASK_APP, FLASK_ENV) and run the Flask application within the Docker container.

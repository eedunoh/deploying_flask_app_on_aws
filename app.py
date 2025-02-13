from flask import Flask, request, render_template, jsonify
import boto3
import os
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# AWS Session
session = boto3.Session(
    region_name="eu-north-1"  # Make sure to specify region
)

# AWS S3 Configuration
S3_BUCKET = os.getenv("S3_BUCKET")
s3 = boto3.client("s3", region_name="eu-north-1")  # Ensure region is set for S3

# AWS DynamoDB Configuration
dynamodb = boto3.resource("dynamodb", region_name="eu-north-1")  # Ensure region is set for DynamoDB
TABLE_NAME = os.getenv("DYNAMODB_TABLE")
table = dynamodb.Table(TABLE_NAME)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    """Upload a file to S3 and store metadata in DynamoDB."""
    file = request.files.get("file")
    additional_info = request.form.to_dict()
    
    if file:
        filename = file.filename  # Keep the original filename
        try:
            logging.info(f"Uploading {filename} to S3...")
            s3.upload_fileobj(file, S3_BUCKET, filename)
            logging.info(f"File uploaded successfully to S3: {filename}")
            
            # Store metadata in DynamoDB
            additional_info["id"] = filename  # Use filename as ID
            logging.info(f"Storing metadata in DynamoDB: {additional_info}")
            table.put_item(Item=additional_info)
            return "File and metadata uploaded successfully!"
        except Exception as e:
            logging.error(f"Error uploading to S3 or storing in DynamoDB: {e}")
            return f"Error: {e}"
    return "No file uploaded." 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
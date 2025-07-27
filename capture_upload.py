import pyautogui
import boto3
import os
from datetime import datetime
import uuid

# AWS Config
BUCKET_NAME = 'mybucketyadnyesh'
FOLDER_NAME = 'screenshots/'
AWS_REGION = 'ap-south-1'

# Take Screenshot
def capture_screenshot():
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}.png"
    filepath = os.path.join(os.getcwd(), filename)
    image = pyautogui.screenshot()
    image.save(filepath)
    return filepath, filename

# Upload to S3
def upload_to_s3(filepath, filename):
    s3 = boto3.client('s3', region_name=AWS_REGION)
    s3.upload_file(filepath, BUCKET_NAME, FOLDER_NAME + filename)
    print(f"Uploaded {filename} to S3.")
    os.remove(filepath)

if __name__ == "__main__":
    path, name = capture_screenshot()
    upload_to_s3(path, name)

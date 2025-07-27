# RemoteDesk-Tracker
A Screenshot Surveillance System for Remote Work Monitoring (Windows + AWS + Python)

---


```markdown
# 🖥️ RemoteDesk Tracker

> A Screenshot Surveillance System for Remote Work Monitoring (Windows + AWS + Python)

RemoteDesk Tracker is a lightweight Python-based tool designed to monitor remote work by capturing desktop screenshots every 5 minutes and uploading them securely to AWS S3. Ideal for remote teams, work-from-home employees, and productivity tracking.

---

## 📌 Features

- 🔁 Takes automatic screenshots every 5 minutes
- ☁️ Uploads screenshots to AWS S3 Bucket
- 🪟 Compatible with Windows (tested on EC2 instance)
- 🔐 Secure storage using IAM credentials
- 🕒 Runs silently using Windows Task Scheduler
- 📝 Auto-naming of screenshots using timestamp

---

## 🧰 Tech Stack

- Python
- Boto3 (AWS SDK for Python)
- AWS S3 (Storage)
- Windows Task Scheduler

---

## 📂 Project Structure

```

RemoteDesk-Tracker/
├── capture\_upload.py         # Main script for capture + upload
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── /screenshots              # (Optional) Local screenshot backup

````

---

## ⚙️ How It Works

1. Captures screenshot using Python
2. Saves screenshot temporarily
3. Uploads the image to AWS S3 bucket with timestamped filename
4. Deletes local file (optional)
5. Repeats every 5 minutes via Windows Task Scheduler

---

## 🪟 Windows Task Scheduler Setup

1. Press `Win + R` → type `taskschd.msc` → Enter
2. Click **Create Basic Task**
3. Give it a name: `RemoteDesk Tracker`
4. Trigger: **Daily** → Recur every 1 day
5. Repeat task every: **5 minutes**, for a duration of: **1 day**
6. Action: **Start a program**
   - Program/script: `python`
   - Add arguments: `C:\path\to\capture_upload.py`
   - Start in: `C:\path\to\script-folder`
7. Finish. ✅

---

## ☁️ AWS Setup (S3 + IAM)

### 1. S3 Bucket
- Create bucket (e.g. `remotedesk-screenshots`)
- Disable public access
- Optional: Enable versioning or lifecycle rules

### 2. IAM User
- Create IAM user with **Programmatic Access**
- Attach Policy: `AmazonS3FullAccess` (or custom limited access)
- Note `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

---

## 🔑 AWS Credentials Setup (Windows)

Open Command Prompt and run:
```bash
aws configure
````

Enter:

* Access Key ID
* Secret Access Key
* Region (e.g. `ap-south-1`)
* Output format: `json`

---

## 📦 Install Dependencies

Install Python libraries:

```bash
pip install -r requirements.txt
```

`requirements.txt` should include:

```
boto3
pillow
```

---

## ✅ Sample Output

* Filename: `screenshot_2025-07-27_14-10-00.png`
* S3 Path: `s3://remotedesk-screenshots/screenshots/<filename>`

---

## 📌 Use Cases

* Remote employee monitoring
* Productivity tracking for freelancers
* WFH activity logging
* EC2 lab monitoring

---

## 🙌 Author

Made with ❤️ by \[Yadnyesh Chaudhari]
GitHub: [github.com/yourusername](https://github.com/yourusername)

---

## 🛡️ Disclaimer

This tool is for educational or organizational monitoring purposes only. Always inform users being monitored. Do not use without consent.

```

---



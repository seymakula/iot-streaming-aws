# 🌡️ Real-Time IoT Data Streaming — AWS

**BLM3522 Cloud Computing Course | Project 2**  
**Şeyma Kula**

---

## 📌 About the Project

This project is an end-to-end system that processes simulated IoT sensor data in real time using the MQTT protocol on the AWS cloud platform.

**Data flow:**
```
Python Simulator → AWS IoT Core → AWS Lambda → DynamoDB → Flask Dashboard
```

---

## 🏗️ System Architecture

| Component | Technology | Description |
|---|---|---|
| IoT Simulator | Python 3 + awsiotsdk | Produces sensor data via MQTT |
| Protocol | MQTT (TLS/SSL) | Secure data transmission |
| Cloud Broker | AWS IoT Core | Receives and routes MQTT messages |
| Rule Engine | AWS IoT Rule | Forwards incoming data to Lambda |
| Processing | AWS Lambda (Python 3.12) | Processes data via serverless function |
| Database | AWS DynamoDB | NoSQL real-time data storage |
| Dashboard | Python Flask | Web interface for visualization |

---

## 📁 File Structure

```
iot-project/
│
├── publisher.py        # IoT sensor simulator (MQTT publisher)
├── lambda_function.py  # AWS Lambda function
├── dashboard.py        # Flask web dashboard
├── certs/              # AWS IoT certificates (excluded from git)
│   ├── device.pem.crt
│   ├── private.pem.key
│   ├── public.pem.key
│   └── rootCA.pem
└── README.md
```

---

## ⚙️ Setup and Usage

### 1. Requirements

- Python 3.8+
- AWS account
- AWS CLI configured

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install awsiotsdk flask boto3
```

### 3. AWS IoT Core setup

1. AWS Console → IoT Core → Things → Create `iot-sensor-01`
2. Download certificates → place them in `certs/` folder
3. Create IoT Policy (Connect, Publish, Subscribe, Receive permissions)
4. Create IoT Rule: `SELECT * FROM 'sensor/data'` → forward to Lambda

### 4. AWS Lambda setup

1. Lambda → Create `iot-sensor-handler` function (Python 3.12)
2. Paste `lambda_function.py` code and Deploy
3. Attach `AmazonDynamoDBFullAccess` policy to IAM Role

### 5. DynamoDB table

```
Table name    : iot-sensor-data
Partition key : device_id (String)
Sort key      : timestamp (String)
```

### 6. Run the application

**Sensor simulator:**
```bash
python3 publisher.py
```

**Dashboard:**
```bash
python3 dashboard.py
# Open in browser: http://127.0.0.1:5000
```

---

## 📊 Sample Data

```json
{
  "device_id": "sensor-01",
  "temperature": 28.52,
  "humidity": 67.32,
  "pressure": 1017.95,
  "timestamp": "2026-04-18T14:06:37"
}
```

---

## ☁️ AWS Configuration

| Setting | Value |
|---|---|
| AWS Region | eu-central-1 (Frankfurt) |
| IoT Endpoint | a1rim3gq9hoffc-ats.iot.eu-central-1.amazonaws.com |
| MQTT Topic | sensor/data |
| Thing Name | iot-sensor-01 |

---

## 🔒 Security Note

The `certs/` folder is excluded from git via `.gitignore`. Never upload certificate files to a public repository.

---

## 📚 References

- [AWS IoT Core Documentation](https://docs.aws.amazon.com/iot/)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [AWS DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)
- [awsiotsdk Python SDK](https://github.com/aws/aws-iot-device-sdk-python-v2)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MQTT Protocol](https://mqtt.org/)

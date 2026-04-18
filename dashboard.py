from flask import Flask, render_template_string
import boto3

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('iot-sensor-data')

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>IoT Sensor Dashboard</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: Arial; background: #1a1a2e; color: white; padding: 20px; }
        h1 { color: #00d4ff; text-align: center; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th { background: #00d4ff; color: black; padding: 10px; }
        td { padding: 10px; border-bottom: 1px solid #333; text-align: center; }
        tr:hover { background: #16213e; }
    </style>
</head>
<body>
    <h1>IoT Sensor Dashboard</h1>
    <p style="text-align:center">Her 5 saniyede otomatik yenilenir</p>
    <table>
        <tr>
            <th>Device ID</th>
            <th>Timestamp</th>
            <th>Sicaklik (C)</th>
            <th>Nem (%)</th>
            <th>Basinc (hPa)</th>
        </tr>
        {% for item in items %}
        <tr>
            <td>{{ item.device_id }}</td>
            <td>{{ item.timestamp }}</td>
            <td>{{ item.temperature }}</td>
            <td>{{ item.humidity }}</td>
            <td>{{ item.pressure }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/')
def index():
    response = table.scan()
    items = sorted(response['Items'], key=lambda x: x['timestamp'], reverse=True)[:20]
    return render_template_string(HTML, items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

📊 Task 6 – Monitoring Stack with Prometheus & Grafana

This project sets up a complete monitoring stack for a containerized application using Prometheus, Grafana, and a Flask sample app that exposes custom metrics via a /metrics endpoint.

📌 Objective

Deploy a sample application with Prometheus metrics support

Deploy Prometheus + Grafana using Docker Compose

Scrape custom metrics using Prometheus

Visualize metrics in Grafana

Export a Grafana dashboard as JSON


🚀 Setup Instructions
1️⃣ Build & Start the Monitoring Stack

Run the following command in the task_6 directory:

docker-compose up --build -d


This starts:

Sample App (port 5000)

Prometheus (port 9090)

Grafana (port 3000)

🧪 2️⃣ Verify Services
✔ Sample App

Visit:

http://localhost:5000

<img width="1919" height="460" alt="image" src="https://github.com/user-attachments/assets/38d6d20b-a122-434e-97d7-81167b0ef7c5" />


✔ Sample App Metrics

Visit:

http://localhost:5000/metrics

<img width="1919" height="871" alt="image" src="https://github.com/user-attachments/assets/cdbe9c96-375a-4715-9756-f69090a38b61" />


✔ Prometheus

Visit:

http://localhost:9090/targets

Verify target status:

You should see sample-app as UP.

<img width="1919" height="609" alt="image" src="https://github.com/user-attachments/assets/cad463d0-ae29-4116-8803-311607df8164" />


✔ Grafana

Visit:

http://localhost:3000


Login credentials:

Username: admin
Password: admin

📡 3️⃣ Prometheus Configuration

prometheus.yml:

global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'sample-app'
    static_configs:
      - targets: ['sample-app:5000']


Prometheus scrapes:
👉 http://sample-app:5000/metrics

📝 4️⃣ Sample Application Code (Flask + Prometheus Client)

main.py:

from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('sample_app_requests_total', 'Total requests to the sample app')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Hello from Sample App"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

📊 5️⃣ Create Dashboard in Grafana
Steps:

Go to Grafana → Dashboards → New → New Panel

In the Prometheus query editor, use:

sample_app_requests_total


Click Run queries

Choose visualization:

Graph (recommended)

Click Apply

Save dashboard as:

Sample App Monitoring

🔄 6️⃣ Generate Metrics

To generate traffic:

Open the app:

http://localhost:5000


Refresh the page 5–10 times

Prometheus will scrape new values

Grafana graph updates automatically

📤 7️⃣ Export Grafana Dashboard

Open your dashboard

Click Share (top-right)

Go to Export

Click Export JSON

It will download:

sample-app-dashboard.json


This is your final deliverable.

✅ Final Deliverables

Working Prometheus instance scraping metrics

Working Grafana visualization

Exported dashboard JSON

Running Flask app with /metrics endpoint

📌 Useful Commands

Stop containers:

docker-compose down


Restart:

docker-compose up -d


Check logs:

docker logs task_6-sample-app-1


Final output:

<img width="1919" height="1019" alt="image" src="https://github.com/user-attachments/assets/723c3ee1-3427-40be-aed6-fc645df91ac6" />


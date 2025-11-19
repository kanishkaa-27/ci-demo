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
    return generate_latest(), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

🚀 Simulated Production Incident – Buggy App Deployment (Kubernetes + Minikube)

This project demonstrates how to deploy a buggy Flask application into a local Minikube Kubernetes cluster and simulate a production incident.
The application intentionally fails at random times to replicate real-world system instability.

📌 1. Prerequisites

Before you begin, ensure you have:

Docker Desktop

Minikube

kubectl

Python Flask app + Dockerfile (included in this project)

📌 2. Start Minikube
minikube start


Check node status:

kubectl get nodes

📌 3. Build the Docker Image Inside Minikube

Run the following so Docker builds inside Minikube’s environment:

& minikube -p minikube docker-env | Invoke-Expression


Now build the image:

docker build -t buggy-app:1 .


Verify:

docker images

📌 4. Deploy Kubernetes Resources

Apply deployment:

kubectl apply -f deployment.yaml


Apply service:

kubectl apply -f service.yaml


Check running pods:

kubectl get pods -o wide

📌 5. Access the Application
Option 1 — Port Forward (Recommended on Windows)
kubectl port-forward svc/buggy-service 8080:80


Now open in browser:

http://localhost:8080

📌 6. Simulate Load / Reproduce Failures

Use PowerShell:

for ($i=1; $i -le 50; $i++) {
  try { Invoke-RestMethod http://localhost:8080 }
  catch { Write-Host "FAILED" -ForegroundColor Red }
}


You will observe:

200 OK

500 Internal Server Error

Failed requests

Random timeouts

This is expected behavior.

📌 7. View Application Logs
kubectl logs -l app=buggy-app --tail=50


You will see logs such as:

ZeroDivisionError

Random internal failure

Slow responses

These are part of the simulated incident.

📌 8. Root Cause Analysis (RCA)

A complete RCA of the incident—including logs, evidence, explanation, and proposed fixes—has been documented separately.

📄 For the full RCA, refer to the document:
👉 “Simulated Production Incident Report”

This document contains the detailed analysis and conclusions for this task.
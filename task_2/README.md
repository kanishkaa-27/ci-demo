📘 Task 2 – Kubernetes Deployment Using Minikube








This task demonstrates deploying a Dockerized Python application to a local Kubernetes cluster using Minikube.
The deployment uses a local Docker image, a Deployment, and a NodePort Service to expose the application externally.

🚀 Objective

Dockerize a simple Python app

Create Kubernetes manifests:

deployment.yaml

service.yaml

Deploy the application to Minikube

Verify pods and services with kubectl

Access the application via NodePort

📂 Folder Structure
task_2/
│
├── k8s_manifests/
│   ├── deployment.yaml
│   ├── service.yaml
│
└── screenshots/
    ├── pods-running.png
    ├── service.png
    └── app-output.png

🛠 Prerequisites

Docker Desktop installed

Minikube installed

kubectl installed

A local docker image, e.g.

ci-demo-app:16

🧱 Step-by-Step Guide
1️⃣ Start Minikube
minikube start

2️⃣ Load Local Docker Image into Minikube

Since Minikube uses its own Docker engine, load your local image:

minikube image load ci-demo-app:16


To verify:

minikube image ls

📄 Kubernetes Manifests
deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: python-app
  template:
    metadata:
      labels:
        app: python-app
    spec:
      containers:
        - name: python-app
          image: ci-demo-app:16
          imagePullPolicy: Never
          ports:
            - containerPort: 5000

service.yaml
apiVersion: v1
kind: Service
metadata:
  name: python-app-service
spec:
  type: NodePort
  selector:
    app: python-app
  ports:
    - port: 5000
      targetPort: 5000
      nodePort: 30050

🚀 Deploy to Kubernetes
Apply manifests:
kubectl apply -f k8s_manifests/deployment.yaml
kubectl apply -f k8s_manifests/service.yaml

🔍 Verification

kubectl get pods
<img width="704" height="177" alt="image" src="https://github.com/user-attachments/assets/53fb79f1-5f2e-4fa1-bf29-986954ec9308" />

kubectl get svc
<img width="808" height="241" alt="image" src="https://github.com/user-attachments/assets/03e781b0-5d36-42a1-b0ac-e548de3eb858" />



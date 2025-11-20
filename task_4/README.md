

🚀 Task 4 – End-to-End CI/CD Pipeline (GitHub Actions → Docker Hub → Minikube)

This task demonstrates how to build a complete CI/CD pipeline using:

GitHub Actions

Self-Hosted Runner (Windows)

Docker & Docker Hub

Kubernetes (Minikube)

Python Flask application


This pipeline automates the entire workflow from code commit → Docker image build → Docker Hub push → Kubernetes deployment update.


---

🎯 Objective

Build a CI/CD pipeline that performs:

1. Builds and tests a Python app


2. Builds a Docker image


3. Pushes the image to Docker Hub


4. Updates Kubernetes manifests


5. Deploys automatically into Minikube



All steps run on a self-hosted GitHub Actions runner.


---

⚙ Step 1 — Self-Hosted Runner Setup (Windows)

1. Download GitHub runner from repo:
Settings → Actions → Runners → New self-hosted runner


2. Extract and configure:



cd D:\Task\ci-demo\actions-runner
.\config.cmd --url https://github.com/kanishkaa-27/ci-demo --token <RUNNER_TOKEN>
.\run.cmd

Runner must show:

√ Connected to GitHub
Listening for Jobs...


---

🐳 Step 2 — Build & Run the Docker Image Locally

docker build -t task4:local .
docker run -p 5000:5000 task4:local


---

☸ Step 3 — Deploy to Kubernetes (Minikube)

minikube start
minikube image load task4:local
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
minikube service task4-service --url


---

🤖 Step 4 — GitHub Actions CI/CD Workflow

File: .github/workflows/ci-cd.yml

This workflow:

✔ Installs dependencies
✔ Builds Docker image
✔ Pushes to Docker Hub
✔ Updates Kubernetes deployment
✔ Restarts the deployment

Your working Docker login step:

- name: Login to Docker Hub
  run: |
    docker login --username $env:DOCKERHUB_USERNAME --password $env:DOCKERHUB_TOKEN
  env:
    DOCKERHUB_USERNAME: ${{ secrets.DOCKERHUB_USERNAME }}
    DOCKERHUB_TOKEN: ${{ secrets.DOCKERHUB_TOKEN }}


---

🔐 GitHub Secrets Required

Go to:

Settings → Secrets → Actions

Create:

Secret Name	Value

DOCKERHUB_USERNAME	kanishkaa27
DOCKERHUB_TOKEN	Docker Hub access token



---

🚀 CI/CD Flow

1. Developer pushes code → GitHub


2. GitHub triggers workflow


3. Self-hosted runner builds Docker image


4. Runner logs into Docker Hub


5. Image is pushed (latest)


6. YAML file updates automatically


7. Minikube deployment is restarted


8. Application updates live with zero downtime




---

🧪 Testing the Deployment

Check pods:

kubectl get pods

Check service:

kubectl get svc

Get external Minikube URL:

minikube service task4-service --url

View app response in browser.


---

🛠 Challenges Faced & Solutions

1. PowerShell ExecutionPolicy blocking scripts

❌ Error: running scripts is disabled on this system
✔ Fixed using:

Set-ExecutionPolicy RemoteSigned -Scope LocalMachine -Force


---

2. Docker login failing (non-TTY error)

❌ Error: Cannot perform an interactive login from a non TTY device
✔ Fixed using Windows-compatible syntax:

docker login --username $env:DOCKERHUB_USERNAME --password $env:DOCKERHUB_TOKEN


---

3. Runner not picking jobs

✔ Fixed by running:

cd actions-runner
.\run.cmd

and leaving the window open.


---

🎉 Final Outcome

A fully automated CI/CD system that:

Builds and tests a Python app

Generates a Docker image

Pushes image to Docker Hub

Updates and deploys Kubernetes resources

Runs smoothly on a self-hosted Windows runner!

![WhatsApp Image 2025-11-20 at 10 10 34_a6afc8bf](https://github.com/user-attachments/assets/8897478f-220a-479d-b8ee-3ccf4e686190)



![WhatsApp Image 2025-11-20 at 10 10 19_2748d811](https://github.com/user-attachments/assets/e1fba62b-7ecf-404c-b6f0-23605a7db2cc)

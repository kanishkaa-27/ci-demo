🚀 GitOps Workflow Using Argo CD on Minikube (Windows)

This project demonstrates a complete GitOps workflow using Argo CD, Kubernetes, and a GitHub repository.
Applications deployed to Kubernetes are fully controlled by Git, and ArgoCD automatically syncs any changes pushed to the repository.

📌 Prerequisites

Windows 10/11

Kubernetes (Minikube) installed

kubectl installed

Git installed

Minikube running with Docker driver (recommended)

🏗 1. Start Minikube
minikube start --memory=4096 --cpus=2 --driver=docker


Verify cluster:

kubectl get nodes

🎯 2. Install Argo CD

Create namespace:

kubectl create namespace argocd


Install ArgoCD:

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


Check pods:

kubectl get pods -n argocd


All ArgoCD components should be Running.

🌐 3. Expose Argo CD UI (LoadBalancer for Windows)

Patch the service:

kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'


Start Minikube tunnel:

minikube tunnel


Get external IP:

kubectl get svc argocd-server -n argocd


Now access ArgoCD UI in browser:

👉 https://127.0.0.1

or
👉 https://<EXTERNAL-IP>

🔐 4. Get Argo CD Admin Password

Windows PowerShell:

$pwd = kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}"
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($pwd))


Default login:

Username: admin

Password: (decoded value)

🔄 5. Connect Argo CD to GitHub Repository

Go to ArgoCD UI

Click → Settings → Repositories

Add your GitHub repo URL

Select authentication type (HTTPS / SSH)

📦 6. Create ArgoCD Application (GitOps)

Example application.yaml:

apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: demo-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: "https://github.com/<your-user>/<your-repo>.git"
    targetRevision: main
    path: k8s
  destination:
    server: https://kubernetes.default.svc
    namespace: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true


Apply:

kubectl apply -f application.yaml


ArgoCD will:

✔ Pull manifests from Git
✔ Deploy to Kubernetes
✔ Auto-sync changes when you push updates

🔁 7. GitOps Workflow

Modify Kubernetes YAML in your Git repo

Commit and push changes

ArgoCD auto-detects changes

Cluster updates automatically

outputs:

<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/0adfcccc-f33e-40a9-b522-515481b11cfb" />
<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/a0c9fcfc-217d-4709-90de-c879ca0a95b4" />
<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/92b1965a-baa7-48e0-b61e-14cda0b367b5" />
<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/7ec30f2a-1499-4344-8031-f4812d4721bf" />

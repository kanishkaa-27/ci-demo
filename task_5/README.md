Here is your **updated README.md**, fully changed from **task_7 → task_5** everywhere.
You can paste this directly into:

```
ci-demo/task_5/README.md
```

---

# 🚀 Task 5 – Infrastructure Automation using Shell + Docker Compose

This task demonstrates how to automate a full DevOps-style environment **locally** without any cloud services.
Using **Docker Compose** and a **Shell script**, we deploy and orchestrate:

* **Jenkins** (CI/CD Server)
* **Redis** (In-memory key-value store)
* **Python Flask App** (Sample API)
* **Nginx Reverse Proxy** (Front-end router)

This setup simulates a realistic local DevOps environment with multiple interconnected services.

---

## 📁 Project Structure

```
task_5/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   └── default.conf
│
├── data/
│   └── jenkins_home/        # Jenkins persistent storage
│
├── docker-compose.yml
└── setup.sh
```

---

## 🎯 Objective

* Automate local infrastructure setup
* Run multiple services using Docker Compose
* Use a shell script to bootstrap the complete environment
* Implement service dependencies (Nginx → App → Redis)
* Demonstrate container networking and service orchestration

---

# ⚙️ Services Overview

### **1️⃣ Jenkins**

* CI/CD server
* Runs on: **[http://localhost:8080](http://localhost:8080)**
* Uses persistent volume: `data/jenkins_home/`
* Get the initial admin password:

```bash
docker exec -it task_5-jenkins-1 cat /var/jenkins_home/secrets/initialAdminPassword
```

---

### **2️⃣ Redis**

* Default port: **6379**
* Used by Flask app to store hit counter

```bash
docker exec -it task_5-redis-1 redis-cli
> ping
> get hits
```

---

### **3️⃣ Flask Sample App**

* Internal port: **5000**
* Returns JSON:

```json
{"status": "ok", "message": "Hello from Sample App", "hits": 1}
```

* Connects to Redis for hit count
* Built from its own Dockerfile

---

### **4️⃣ Nginx Reverse Proxy**

* Public URL: **[http://localhost/](http://localhost/)**
* Routes traffic → Flask app
* Config stored in `nginx/default.conf`

---

# ▶️ How to Run the Project

### **1. Run the setup script**

```bash
bash setup.sh
```

It performs:

✔ Builds Docker images
✔ Starts all services
✔ Shows logs
✔ Prints access URLs

---

# 🌐 Access the Applications

| Service                   | URL                                            | Description                         |
| ------------------------- | ---------------------------------------------- | ----------------------------------- |
| **Flask App (via Nginx)** | [http://localhost/](http://localhost/)         | JSON output + hit counter           |
| **Jenkins UI**            | [http://localhost:8080](http://localhost:8080) | Admin setup and plugin installation |
| **Flask Direct**          | [http://localhost:5000](http://localhost:5000) | Raw Flask API                       |

---

# 🧪 Verification Steps

### Check running services:

```bash
docker compose ps
```

Expected output:

```
task_5-app-1      Up
task_5-jenkins-1  Up
task_5-nginx-1    Up
task_5-redis-1    Up
```

### Test main endpoint:

```bash
curl http://localhost/
```

### View logs:

```bash
docker compose logs jenkins
docker compose logs app
docker compose logs nginx
docker compose logs redis
```

---

# 🔧 Troubleshooting

| Issue                      | Cause                 | Fix                                     |
| -------------------------- | --------------------- | --------------------------------------- |
| **Port 8080 in use**       | Jenkins conflict      | Change to `9090:8080` in compose file   |
| **Redis port in use**      | Redis already running | Stop existing Redis or change port      |
| **Nginx not starting**     | Wrong config file     | Validate `default.conf`                 |
| **App failing to connect** | Redis not ready       | Compose `depends_on` handles dependency |

---

output:
<img width="975" height="84" alt="image" src="https://github.com/user-attachments/assets/2f4cf7f9-07a9-48b4-a232-1dea0816d37a" />

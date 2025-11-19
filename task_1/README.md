# CI Demo Project

This project demonstrates a simple CI/CD workflow using **Jenkins**, **Docker**, and **Python Flask**.

## 📁 Project Structure

```
ci-demo/
└── task_1/
    ├── Jenkinsfile
    ├── app.py
    ├── Dockerfile
    ├── requirements.txt
    └── tests/
        └── test_app.py
```

## 🚀 What This Pipeline Does

The Jenkins pipeline performs the following stages:

1. **Checkout**

   * Pulls the latest code from the Git repository.

2. **Install & Test**

   * Upgrades pip
   * Installs dependencies from `requirements.txt`
   * Runs unit tests using `pytest`

3. **Build Docker Image**

   * Builds a Docker image using the Dockerfile in `task_1/`
   * Tags the image as `ci-demo-app:<BUILD_NUMBER>`

4. **Run Container**

   * Runs the built Docker container on port **5001 -> 5000**

5. **Post Actions**

   * Prints SUCCESS or FAILED based on pipeline result

---

## 🐳 Docker

### Build Image Manually

```
docker build -t ci-demo-app .
```

### Run Container

```
docker run -p 5001:5000 ci-demo-app
```

Then open:

```
http://localhost:5001/
```

---

## 🧪 Running Tests Locally

To run tests manually:

```
pip install -r task_1/requirements.txt
pytest task_1/tests -q
```

---

## 🔧 Jenkins Requirements

* Jenkins running inside Docker
* Docker socket mounted:

```
-v /var/run/docker.sock:/var/run/docker.sock
```

* Custom Jenkins agent image: `python-docker-agent`

---

## 📦 Python Application

A simple Flask app located in `task_1/app.py`:

* Exposes endpoint `/`
* Runs on port **5000** inside the container

---

## 📝 Jenkinsfile Summary

The Jenkinsfile uses:

* Docker agent for Python and Docker CLI
* `dir("task_1")` to run commands inside the project directory


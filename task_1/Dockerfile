FROM python:3.10

# Install Docker CLI + Curl
RUN apt-get update && \
    apt-get install -y docker.io curl && \
    apt-get clean

# Upgrade pip
RUN python -m pip install --upgrade pip

# Set working directory
WORKDIR /app

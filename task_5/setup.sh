#!/usr/bin/env bash
set -euo pipefail

echo "==> Preparing environment..."
mkdir -p data/jenkins_home

docker compose build

echo "==> Starting services..."
docker compose up -d

echo "==> Waiting for services..."
sleep 5

docker compose ps

echo "==> Setup complete!"
echo "Jenkins: http://localhost:8080"
echo "App: http://localhost"

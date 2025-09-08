#!/bin/bash

IMAGE_NAME="ghcr.io/yourusername/yourimage:latest"
CONTAINER_NAME="your_container"
DOCKERFILES_DIR="$(dirname "$0")/../docker"

function deploy() {
    echo "Deploying all Docker images in $DOCKERFILES_DIR to GitHub Container Registry..."
    for dockerfile in "$DOCKERFILES_DIR"/*; do
        if [[ -f "$dockerfile" ]]; then
            IMG_TAG="${IMAGE_NAME}-$(basename "$dockerfile" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g')"
            echo "Building $IMG_TAG from $dockerfile..."
            docker build -f "$dockerfile" -t "$IMG_TAG" "$DOCKERFILES_DIR"
            echo "Pushing $IMG_TAG..."
            docker push "$IMG_TAG"
        fi
    done
    echo "Deploy complete."
}

function reset() {
    echo "Stopping and removing all containers..."
    docker ps -aq | xargs -r docker stop
    docker ps -aq | xargs -r docker rm
    for dockerfile in "$DOCKERFILES_DIR"/*; do
        if [[ -f "$dockerfile" ]]; then
            IMG_TAG="${IMAGE_NAME}-$(basename "$dockerfile" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g')"
            echo "Pulling $IMG_TAG from GitHub Container Registry..."
            docker pull "$IMG_TAG"
            echo "Running new container from $IMG_TAG..."
            docker run -d --name "${CONTAINER_NAME}-$(basename "$dockerfile")" "$IMG_TAG"
        fi
    done
    echo "Reset complete."
}

case "$1" in
    deploy)
        deploy
        ;;
    reset)
        reset
        ;;
    *)
        echo "Usage: $0 {deploy|reset}"
        exit
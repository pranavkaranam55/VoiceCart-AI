FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nodejs \
    npm \
    git \
    docker.io

# Add jenkins user to docker group
RUN groupadd -f docker && usermod -aG docker jenkins

USER jenkins
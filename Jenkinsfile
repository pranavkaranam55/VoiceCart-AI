pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/pranavkaranam55/VoiceCart-AI.git'
            }
        }

        stage('Frontend Build') {
            steps {
                dir('FrontEnd') {
                    bat 'npm install'
                    bat 'npm run build'
                }
            }
        }

        stage('Backend Dependencies') {
            steps {
                dir('BackEnd') {
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker compose build'
            }
        }
    }
}
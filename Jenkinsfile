pipeline {

    agent any

    environment {
        PATH = "/var/jenkins_home/.local/bin:${env.PATH}"
    }

    stages {

        stage('Frontend Build') {
            steps {
                dir('FrontEnd') {
                    sh 'npm install'
                    sh 'npm run build'
                }
            }
        }

        stage('Backend Dependencies') {
            steps {
                dir('BackEnd') {

                  sh 'pip3 install --break-system-packages -r requirements-ci.txt'                }
            }
        }

        stage('Docker Build Backend') {
            steps {
                sh 'docker build -t voicecart-backend ./BackEnd'
            }
        }

        stage('Docker Build Frontend') {
            steps {
                sh 'docker build -t voicecart-frontend ./FrontEnd'
            }
        }

    }

    post {

        success {
            echo 'VoiceCart AI CI/CD Pipeline Completed Successfully!'
        }

        failure {
            echo 'Pipeline Failed!'
        }

    }
}
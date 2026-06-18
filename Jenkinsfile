pipeline {

    agent any

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
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker compose build'
            }
        }

    }
}
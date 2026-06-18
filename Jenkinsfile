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
sh 'pip3 install --break-system-packages -r requirements.txt'                }
            }
        }

        stage('Docker Build') {
    steps {
        sh 'docker build -t voicecart-backend ./BackEnd'
        sh 'docker build -t voicecart-frontend ./FrontEnd'
    }
}
    }
}
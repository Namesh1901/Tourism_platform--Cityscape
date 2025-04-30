pipeline {
    agent any

    environment {
        DEPLOY_SERVER = '34.173.159.205'
        DEPLOY_USER = 'namesh-ubuntu'
        SSH_CREDENTIALS_ID = 'your-ssh-credentials-id'
        GIT_REPO = 'git@github.com:Namesh1901/Tourism_platform--Cityscape.git'
        BRANCH = 'main'
        PROJECT_DIR = '/path/to/your/project/on/deploy/server'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "${BRANCH}", url: "${GIT_REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("yourdockerhubusername/tourism_platform:latest")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials-id') {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                sshagent (credentials: ["${SSH_CREDENTIALS_ID}"]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_SERVER} '
                        cd ${PROJECT_DIR} &&
                        docker-compose pull &&
                        docker-compose up -d --build
                    '
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}

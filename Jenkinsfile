pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'syedali4/myapp-backend:v1'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE_NAME ."
                }
            }
        }

       stage('Push Docker Image to Docker Hub') {
            steps {
                // Log in to Docker Hub and push the image using the credentials stored in Jenkins.
                withCredentials([usernamePassword(credentialsId: '123', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    bat "echo %DOCKERHUB_PASSWORD% | docker login -u %DOCKERHUB_USERNAME% --password-stdin"
                    bat "docker push ${env.DOCKER_IMAGE_NAME}"
                }
            }
        }

    post {
        always {
            // Clean up Docker images
            sh 'docker system prune -af'
        }
        success {
            echo 'Pipeline Success'
            mail bcc: '', body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "Success CI: Project name -> ${env.JOB_NAME}", to: "umar.waseem@gmail.com";
        }
        failure {
            echo 'Pipeline Failed'
            mail bcc: '', body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "umar.waseem@gmail.com";
        }
    }
}

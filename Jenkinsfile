pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'syedali4/myapp-backend:v1' // Specify the desired Docker image name and tag
    }

    stages {
        stage('Code Quality Check') {
            steps {
                // Add steps for code quality check
                sh 'flake8' // Example command for running Flake8, replace with actual command
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Use Docker CLI commands or a Docker plugin to build the Docker image
                sh 'docker build -t $DOCKER_IMAGE_NAME .'
            }
        }
        
        stage('Push Docker Image to Docker Hub') {
            steps {
                // Use Docker CLI commands or a Docker plugin to push the Docker image to Docker Hub
                sh 'docker push $DOCKER_IMAGE_NAME'
            }
        }
        
        stage('Notification') {
            steps {
                // Add steps for sending email notification
                mail to: 'your-email@example.com', // Update with your email address
                     subject: "Pipeline Success: ${env.JOB_NAME}",
                     body: "The pipeline ${env.JOB_NAME} has been successfully executed.\nBuild Number: ${env.BUILD_NUMBER}\nBuild URL: ${env.BUILD_URL}"
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
        }
        failure {
            echo 'Pipeline Failed'
        }
    }
}

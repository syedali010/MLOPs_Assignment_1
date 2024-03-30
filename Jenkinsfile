pipeline {
    agent any

    environment {
        // Set your Docker image name here
        DOCKER_IMAGE_NAME = 'syedali4/myapp-backend:v1'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                // Build the Docker image with the specified tag
                bat "docker build -t %DOCKER_IMAGE_NAME% ."
            }
        }
        


        stage('Login Dockerhub and Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials1', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                    echo "Logging in to Docker Hub"
                    bat "docker login --username %DOCKER_HUB_USERNAME% --password %DOCKER_HUB_PASSWORD%"
                    bat "docker push %DOCKER_IMAGE_NAME%"
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images using Windows batch command
            bat "docker system prune -af"
        }
        success {
            echo 'Pipeline Success'
            // Sending email notification. Configure the 'mail' step according to your Jenkins email setup
            echo 'Email notification for successful build would be sent here.'
        }
        failure {
            echo 'Pipeline Failed'
            // Sending email notification. Configure the 'mail' step according to your Jenkins email setup
            echo 'Email notification for failed build would be sent here.'
        }
    }
}

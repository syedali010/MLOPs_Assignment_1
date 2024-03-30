pipeline {
    agent any

    environment {
        // Define the Docker image name here. This name will be used in the build, tag, and push stages.
        DOCKER_IMAGE_NAME = 'syedali4/myapp-backend:v1'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                // Check out your code from the source control management system you're using.
                checkout scm
            }
        }

        stage('Code Quality Check') {
            steps {
                // Add steps for code quality check, if applicable.
                // Example: sh 'flake8'
                echo 'Code quality checks would go here.'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Build the Docker image with a temporary tag
                sh 'docker build -t myapp-backend:v1 .'
            }
        }

        stage('Tag Docker Image') {
            steps {
                // Tag the built image with the full Docker Hub repository name
                sh "docker tag myapp-backend:v1 ${env.DOCKER_IMAGE_NAME}"
            }
        }
        
       stage('Push Docker Image to Docker Hub') {
       steps {
        // Use the 'withCredentials' block to inject your Docker Hub credentials into the environment variables
        withCredentials([usernamePassword(credentialsId: '123', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
            // Log in to Docker Hub using the credentials
            sh 'echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin'
            // Push the Docker image using the environment variable for the image name
            sh "docker push ${env.DOCKER_IMAGE_NAME}"
        }
    }
}

        
        stage('Notification') {
            steps {
                // Send a notification about the build status. Customize the email as necessary.
                mail to: 'i200863@nu.edu.pk',
                     subject: "Pipeline ${currentBuild.result}: Job ${env.JOB_NAME}",
                     body: "The pipeline ${env.JOB_NAME} build ${currentBuild.result}.\n\nBuild Number: ${env.BUILD_NUMBER}\nBuild URL: ${env.BUILD_URL}"
            }
        }
    }

    post {
        always {
            // Clean up by removing unused Docker images and containers to free up space
            sh 'docker system prune -af'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs for more information.'
        }
    }
}

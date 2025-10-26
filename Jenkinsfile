pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                bat 'docker build -t sony1750812/library:t6 .'
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub..."
                bat 'docker login -u sony1750812 -p sony@1415'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing image to Docker Hub..."
                bat 'docker push sony1750812/library:t6'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo "✅ Library Management System successfully deployed!"
        }
        failure {
            echo "❌ Pipeline failed. Check Jenkins logs."
        }
    }
}

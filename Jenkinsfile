pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Clonando repositorio...'
            }
        }

        stage('Test') {
            steps {
                sh 'pip install flask pytest --break-system-packages'
                sh 'pytest'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t Assimela7/python-app:latest .'
            }
        }

        stage('DockerHub') {
            steps {
                sh 'docker push Assimela7/python-app:latest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}

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
                sh 'python3 -m pytest test_app.py'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t assimeb/python-app:latest .'
            }
        }

        stage('DockerHub') {
            steps {
                sh 'docker push assimeb/python-app:latest'
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

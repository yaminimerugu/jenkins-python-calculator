pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials1', url: 'https://github.com/yaminimerugu/jenkins-python-calculator.git'
            }
        }

        stage('List Files') {
            steps {
                bat 'dir'  // List files in the current workspace for debugging
            }
        }

        stage('Setup') {
            steps {
                script {
                    bat 'C:\\Users\\yamin\\AppData\\Local\\Programs\\Python\\Python312\\python -m venv venv'
                    bat 'venv\\Scripts\\pip install -r requirements.txt'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo "Building the application..."
                    bat 'venv\\Scripts\\python --version'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    bat 'venv\\Scripts\\python -m unittest test_calculator.py'
                }
            }
        }

        stage('Notify') {
            steps {
                script {
                    echo "Sending email notification..."
                    mail to: 'ymerugu6104@Conestogac.on.ca',
                         subject: "Jenkins Build Notification",
                         body: "The Jenkins build has completed. Check Jenkins for details."
                }
            }
        }
    }

    post {
        success {
            echo "Build was successful!"
        }
        failure {
            echo "Build failed!"
        }
    }
}

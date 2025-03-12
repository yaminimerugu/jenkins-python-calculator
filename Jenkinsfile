pipeline {
    agent any  // Use any available agent

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials1', url: 'https://github.com/yaminimerugu/jenkins-python-calculator.git'
            }
        }

        stage('Setup') {
            steps {
                script {
                    sh  'C:\\Users\\yamin\\AppData\\Local\\Programs\\Python\\Python312\\python -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo "Building the application..."
                    sh 'python --version'  // Example build step
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    sh 'source venv/bin/activate && python -m unittest test_calculator.py'
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

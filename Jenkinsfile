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
                    sh 'python3 -m venv venv'
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
                    mail to: 'your_college_email@example.com',
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

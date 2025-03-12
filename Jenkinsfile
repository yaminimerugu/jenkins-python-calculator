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
                    // Use Windows style paths for virtual environment setup
                    bat 'C:\\Users\\yamin\\AppData\\Local\\Programs\\Python\\Python312\\python -m venv venv'
                    // Activate the virtual environment and install dependencies
                    bat 'venv\\Scripts\\pip install -r requirements.txt'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo "Building the application..."
                    // Use Windows path for Python version check
                    bat 'venv\\Scripts\\python --version'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    // Activate the virtual environment and run tests
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

pipeline {
    agent any

    environment {
        // Path to your Python virtual environment
        PYTHON_ENV = "/media/bladerunner95/Fast/Portfolio/selenium-automation-showcase/pythonProject/.jenkins_venv"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from the repository
                checkout scm
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    // Create and activate a Python virtual environment
                    sh 'python3 -m venv $PYTHON_ENV'
                    // Install dependencies from requirements.txt
                    sh '$PYTHON_ENV/bin/pip install -r /media/bladerunner95/Fast/Portfolio/selenium-automation-showcase/pythonProject/requirements.txt'
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Activate venv and run Selenium tests with JUnit XML reporting
                    sh '''
                    source .jenkins_venv/bin/activate
                    pytest selenium_tests/ --junitxml=reports/selenium-test-results.xml
                    '''
                }
            }
        }

        stage('Run API Tests') {
            steps {
                script {
                    // Activate venv and run API tests with JUnit XML reporting
                    sh '''
                    source .jenkins_venv/bin/activate
                    pytest api_tests/ --junitxml=reports/api-test-results.xml
                    '''
                }
            }
        }
    }

    post {
        always {
            // Cleanup after tests have run (if necessary)
            echo 'Cleaning up the workspace...'
            cleanWs()
        }

        success {
            // Success notification or actions (e.g., email or Slack)
            echo 'Tests ran successfully!'
        }

        failure {
            // Failure notification or actions (e.g., email or Slack)
            echo 'Tests failed. Investigate the logs for details.'
        }
    }
}


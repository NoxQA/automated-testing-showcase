pipeline {
    agent any

    environment {
        PYTHON_ENV = "/media/bladerunner95/Fast/Portfolio/selenium-automation-showcase/pythonProject/.jenkins_venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    sh 'python3 -m venv $PYTHON_ENV'
                    sh '$PYTHON_ENV/bin/pip install -r /media/bladerunner95/Fast/Portfolio/selenium-automation-showcase/pythonProject/requirements.txt'
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
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
            echo 'Cleaning up the workspace...'
            cleanWs()
        }

        success {
            echo 'Tests ran successfully!'
        }

        failure {
            echo 'Tests failed. Investigate the logs for details.'
        }
    }
}


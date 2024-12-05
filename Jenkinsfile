pipeline {
    agent any

    tools {
        git 'Default' 
    }

    environment {
        PYTHON_ENV = "${WORKSPACE}/.jenkins_venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test File Access') {
            steps {
                script {
                    sh '''
                    echo "Checking file access for requirements.txt"
                    ls -l /media/bladerunner95/Fast/Portfolio/selenium-automation-showcase/pythonProject/requirements.txt
                    cat /media/bladerunner95/Fast/Portfolio/selenium-automation-showcase/pythonProject/requirements.txt
                    '''
                }
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    sh '''
                    python3 --version
                    which python3
                    python3 -m venv $PYTHON_ENV || { echo "Failed to create virtual environment"; exit 1; }
                    $PYTHON_ENV/bin/pip install --upgrade pip
                    $PYTHON_ENV/bin/pip install -r /media/bladerunner95/Fast/Portfolio/selenium-automation-showcase/pythonProject/requirements.txt || { echo "Failed to install dependencies"; exit 1; }
                    '''
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    sh '''
                    . $PYTHON_ENV/bin/activate
                    pytest selenium_tests/ --junitxml=reports/selenium-test-results.xml
                    '''
                }
            }
        }

        stage('Run API Tests') {
            steps {
                script {
                    sh '''
                    . $PYTHON_ENV/bin/activate
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

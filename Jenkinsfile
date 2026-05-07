pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat 'python -m pip install pytest pytest-html'

            }
        }

        stage('Run Pytest Tests') {

            steps {

                bat 'python -m pytest tests/ --html=report.html'

            }
        }
    }
}

pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat 'pip install pytest pytest-html'

            }
        }

        stage('Run Pytest Tests') {

            steps {

                bat 'pytest tests/ --html=report.html'

            }
        }
    }
}

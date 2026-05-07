pipeline {

    agent any

    stages {

        stage('Run Pytest Tests') {

            steps {

                bat 'pytest tests/ --html=report.html'

            }
        }
    }
}

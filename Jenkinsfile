pipeline {

    agent any

    stages {

        stage('Run Pytest Tests') {

            steps {

                sh 'pytest tests/ --html=report.html'

            }
        }
    }
}

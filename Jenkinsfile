pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install pytest pytest-html'

            }
        }

        stage('Run Pytest Tests') {

            steps {

                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pytest tests/ --html=report.html'

            }
        }
    }
}

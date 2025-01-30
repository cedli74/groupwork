pipeline {
    agent any
 
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/cedli74/groupwork.git', branch: 'main'
            }
        }
        stage('Install dependencies') {
            steps {
                sh """
                  python -m venv venv
                  source venv/bin/activate
                  pip install --upgrade pip
                  pip install -r requirements.txt
                """
            }
        }
        stage('Lint') {
            steps {
                sh """
                  source venv/bin/activate
                  flake8 src
                """
            }
        }
        stage('Unit Tests') {
            steps {
                sh """
                  source venv/bin/activate
                  pytest --junitxml=reports/tests.xml --cov=src --cov-report=xml
                """
            }
            post {
                always {
                    // Publier/archiver les rapports
                    junit 'reports/tests.xml'
                    archiveArtifacts artifacts: 'coverage.xml', fingerprint: true
                }
            }
        }
    }
    post {
        success {
            echo "Build réussi !"
        }
        failure {
            echo "Build échoué. Vérifiez les logs."
        }
    }
}

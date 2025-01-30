pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/cedli74/groupwork.git'
            }
        }
        stage('Code Linting') {
            steps {
                bat 'echo Running linter...'  // Remplace par la commande réelle pour le lint
            }
        }
        stage('Tests Unitaires') {
            steps {
                bat '''
                    echo Running unit tests...
                    python -m pytest --max-fail=1 --disable-warnings
                    '''
                
            }
        }
        stage('Build') {
            steps {
                bat 'echo Building project...'  // Remplace par la commande réelle pour builder le projet
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo Deploying application...'  // Remplace par la commande réelle pour déployer
            }
        }
    }
}

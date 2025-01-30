pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/cedli74/groupwork.git'
            }
        }
        stage('Install dependencies') {
            steps {
                bat 'echo Installing dependencies'  // Remplace par la commande réelle
            }
        }
        stage('Lint') {
            steps {
                bat 'echo Running linter'  // Remplace par la commande réelle
            }
        }
        stage('Unit Tests') {
            steps {
                bat 'echo Running unit tests'  // Remplace par la commande réelle
            }
        }
    }
}

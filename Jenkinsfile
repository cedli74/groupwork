pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/cedli74/groupwork.git'
            }
        }
        stage('Install dependencies') {
            steps {
                bat 'npm install'
            }
        }
        stage('Lint') {
            steps {
                bat 'npm run lint'
            }
        }
        stage('Unit Tests') {
            steps {
                bat 'npm test'
            }
        }
    }
}

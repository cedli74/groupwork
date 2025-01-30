pipeline {
    agent any
 
    environment {
        // Variables d'environnement, si besoin
        GIT_REPO = 'https://github.com/cedli74/groupwork.git'
    }
 
    stages {
        stage('Checkout') {
            steps {
                // Récupération du code depuis GitHub
                git url: "${env.GIT_REPO}", branch: 'main'
            }
        }
 
        stage('Code Linting') {
            steps {
                // Linting du code pour vérifier les bonnes pratiques
                sh 'pylint ton_code.py'
            }
        }
 
        stage('Tests Unitaires') {
            steps {
                // Lancer les tests unitaires (exemple avec pytest)
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
 
        stage('Build') {
            steps {
                // Ici, tu peux ajouter les étapes de build, par exemple pour créer des artefacts ou déployer.
                echo 'Building...'
            }
        }
 
        stage('Deploy') {
            steps {
                // Si tu veux déployer ton application quelque part (ex. sur un serveur), ajoute les étapes ici.
                echo 'Deployment in progress...'
            }
        }
    }
 
    post {
        always {
            // Actions à effectuer après le pipeline, comme envoyer des notifications ou sauvegarder des artefacts
            echo 'Pipeline terminé'
        }
 
        success {
            echo 'Tout s\'est bien passé !'
        }
 
        failure {
            echo 'Le pipeline a échoué.'
        }
    }
}

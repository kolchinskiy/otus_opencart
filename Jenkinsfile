pipeline {
    agent any
    
    stages {
        stage('Run Existing Job') {
            steps {
                script {
                    build job: 'otus-opencart'
                }
            }
        }
    }
}

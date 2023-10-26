pipeline {
    agent any
    stages {
        stage('Run Job in Parallel') {
            matrix {
                axes {
                    axis {
                        name 'THREAD'
                        values "${params.THREADS}"
                    }
                }
                stages {
                    stage("Thread \${THREAD}") {
                        steps {
                            build job: 'otus-opencart'
                        }
                    }
                }
            }
        }
    }
}

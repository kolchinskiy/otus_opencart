pipeline {
    agent any
    stages {
        stage('Run Job in Parallel') {
            matrix {
                axes {
                    axis {
                        name 'THREAD'
                        values "${params.NUMBER_OF_THREADS}"
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

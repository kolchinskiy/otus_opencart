pipeline {
    agent any

    parameters {
        choice(name: 'NUMBER_OF_THREADS', choices: ['2', '4', '6'], description: 'Выберите количество потоков')
    }

    stages {
        stage('Run Job in Parallel') {
            steps {
                script {
                    def threads = params.NUMBER_OF_THREADS.toInteger()

                    parallelThreads = [:]
                    for (int i = 1; i <= threads; i++) {
                        parallelThreads["Thread-${i}"] = {
                            build job: 'otus-opencart'
                        }
                    }

                    parallel parallelThreads
                }
            }
        }
    }
}

pipeline {
    agent any

    parameters {
        choice(name: 'NUMBER_OF_THREADS', choices: ['2', '4', '6'], description: '')
        string(name: 'LOCAL_IP', defaultValue: '192.168.1.101', description: '')
        string(name: 'OPENCART_PORT', defaultValue: '8081', description: '')
        string(name: 'EXECUTOR', defaultValue: '192.168.1.101', description: '')
        choice(name: 'BROWSER', choices: ['chrome', 'firefox'], description: '')
        choice(name: 'BV', choices: ['117.0', '118.0'], description: 'Browser version')
    }

    stages {
        stage('Run Job in Parallel') {
            steps {
                script {
                    def threads = params.NUMBER_OF_THREADS.toInteger()
                    def local_ip = params.LOCAL_IP
                    def opencart_port = params.OPENCART_PORT
                    def executor = params.EXECUTOR
                    def browser = params.BROWSER
                    def bv = params.BV

                    parallelThreads = [:]
                    for (int i = 1; i <= threads; i++) {
                        def threadName = "Thread-${i}"
                        parallelThreads[threadName] = {
                            build job: 'otus-opencart', parameters: [
                                string(name: 'LOCAL_IP', value: local_ip),
                                string(name: 'OPENCART_PORT', value: opencart_port),
                                string(name: 'EXECUTOR', value: executor),
                                string(name: 'BROWSER', value: browser),
                                string(name: 'BV', value: bv)
                            ]
                        }
                    }

                    parallel parallelThreads
                }
            }
        }

        stage('Publish Allure Reports') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']],
                    reportBuildPolicy: 'ALWAYS',
                    report: 'allure-report'
                ])
            }
        }
    }
}

pipeline {
    agent any

    parameters {
        choice(name: 'NUMBER_OF_THREADS', choices: ['2', '4', '6'], description: 'Выберите количество потоков')
        string(name: 'LOCAL_IP', defaultValue: '192.168.1.101', description: 'Адрес приложения')
        string(name: 'OPENCART_PORT', defaultValue: '8081', description: 'Порт')
        string(name: 'EXECUTOR', defaultValue: '192.168.1.101', description: '')
        string(name: 'BROWSER', choices: ['chrome', 'firefox'], description: '')
        string(name: 'BV', choices: ['117.0', '118.0'], description: 'Версия браузера')
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
    }
}

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                    docker stop web_dbbbbbb || true
                    cd web_db
                    docker stop web_db
                    docker build -t web_db .
                    docker run --rm -d -p 8099:8099 --name web_db web_db
                '''

            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
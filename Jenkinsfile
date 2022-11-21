pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                    cd web_db
                    docker stop web_db || true
                    docker build -t web_db .
                    docker run --rm -d -p 8099:8099 --name web_db web_db
                '''
                sh("docker run --rm -d -p 8099:8099 --name web_db web_db")
                echo 'Builded successfully!'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh("docker exec web_db pytest -v tests/")
                echo 'Tested successfully!'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
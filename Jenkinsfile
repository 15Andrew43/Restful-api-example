pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                    cd web_db
                    docker stop restful_api_example || true
                    docker build -t restful_api_example .
                '''
                sh("docker run --rm -d -p 8099:8099 --name restful_api_example restful_api_example")
                echo 'Built successfully!'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh("docker exec restful_api_example pytest -v tests/")
                echo 'Tested successfully!'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh("cat /home/runner/my_password.txt | docker login --username avborovets --password-stdin")
                sh("docker tag restful_api_example avborovets/restful_api_example")
                sh("docker push avborovets/restful_api_example")
                echo 'Pushed to DockerHub'
            }
        }
    }
}
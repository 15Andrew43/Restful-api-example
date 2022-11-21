pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                    cd web_db
                    docker stop restful_api_example || true
                    sleep 2
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
                sh("docker stop restful_api_example || true")
                echo 'Tested successfully!'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh("whoami")
                sh("cat /home/runner/my_password.txt | docker login --username avborovets --password-stdin")
                sh("docker tag restful_api_example avborovets/restful_api_example")
                sh("docker push avborovets/restful_api_example")
                echo 'Pushed to DockerHub'
                sh '''
                    cd ..
                    git clone https://github.com/15Andrew43/Ansible-example.git
                    cd Ansible-example
                    git checkout dev
                    cd deploy
                    ansible-playbook playbooks/site.yaml
                    ansible-playbook playbooks/project.yaml
                '''
            }
        }
    }
}
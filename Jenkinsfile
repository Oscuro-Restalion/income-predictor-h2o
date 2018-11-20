#!groovy

pipeline {
    agent any

    parameters {
        string(name: 'localPath', defaultValue: '/Users/oscuro/workspace/commitconf2018/income-predictor-data', description: 'Local path of income predictor data')
    }

    environment {
        ORG_NAME = "oscurorestalion"
        APP_NAME = "income-predictor-h2o"
        APP_CONTEXT_ROOT = "oscuroweb"
        CONTAINER_NAME = "ci-${APP_NAME}"
        IMAGE_NAME = "${ORG_NAME}/${APP_NAME}"

    }

    stages {

        stage('Build Docker image') {
            steps {
                echo "-=- building image -=-"
                script {
                    def image = docker.build("${IMAGE_NAME}:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Docker image') {
           
            steps {
                echo "-=- run Docker image -=-"
                sh "docker run --rm -p 8383:8383 -v ${params.localPath}:/data/income-predictor -e LOCAL_PATH=/data/income-predictor --name ${CONTAINER_NAME} -d ${IMAGE_NAME}:${env.BUILD_ID}"
            }
        }

        stage('Integration tests') {
            steps {
                echo "-=- execute integration tests -=-"
                echo "Not an executable project so no integration test phase needed"
            }
        }

        stage('Performance tests') {
            steps {
                echo "-=- execute performance tests -=-"
                echo "Not an executable project so no performance test phase needed"
            }
        }

        stage('Dependency vulnerability tests') {
            steps {
                echo "-=- run dependency vulnerability tests -=-"
                echo "Not an executable project so no performance test phase needed"
            }
        }

        stage('Push Artifact') {
            steps {
                echo "-=- push Artifact -=-"
                sh "docker push ${IMAGE_NAME}:${env.BUILD_ID}"
            }
        }
    }

    post {
        always {
            echo "-=- remove deployment -=-"
            echo "Not an executable project so no Docker image needed"
        }
    }
}
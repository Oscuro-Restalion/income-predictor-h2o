#!groovy

pipeline {
    agent any

    environment {
        ORG_NAME = "oscuroweb"
        APP_NAME = "income-predictor-h2o"
        APP_CONTEXT_ROOT = "oscuroweb"
        TEST_CONTAINER_NAME = "ci-${APP_NAME}-${BUILD_NUMBER}"
    }

    stages {
        // stage('Compile') {
        //     steps {
        //         echo "-=- compiling project -=-"
        //         sh "mvn clean compile"
        //     }
        // }

        //    stage('Unit tests') {
        //        steps {
        //            echo "-=- execute unit tests -=-"
        //            sh "mvn dependency:tree -Dverbose -Dincludes=oscuroweb"
        //            sh "mvn test"
        //        }
        //    }

        // stage('Package') {
        //     steps {
        //         echo "-=- packaging project -=-"
        //         sh "mvn package -DskipTests"
        //         archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
        //     }
        // }

        stage('Build Docker image') {
            steps {
                echo "-=- building image -=-"
                script {
                    def image = docker.build("${APP_NAME}:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Docker image') {
           
            steps {
                echo "-=- run Docker image -=-"
                sh "docker run --rm -p 8383:8383 --name ${APP_NAME} -d ${APP_NAME}:${env.BUILD_ID}"
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
                echo "Not an executable project so no Docker image needed, anyway jar file need to be installed"
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
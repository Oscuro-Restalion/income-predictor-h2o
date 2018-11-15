#!groovy

pipeline {
    stages {
        stage('Clone repository') {
            checkout scm       
        }
        stage('Build  image') {
            steps {
                app = docker.build("income-predictor-h2o:${env.BUILD_ID}")
            }
        }
        stage('Test') {
            steps {
                app.inside {
                    sh 'echo "Test passed"'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
pipeline{
    agent any

    tools{
        jdk 'java-8'
        maven 'maven-3.9'
    }

    stages{
        stage('compile') {
            steps{
                sh 'mvn compile'

            }
        }

        stage('UnitTest') {
            steps {
                echo 'Run the test cases'
                sh 'mvn test'
            }
            post{
                always{
                    junit 'target/surefire-reports/*.xml'
                }
            }
            
        }

        stage('Package') {
            agent {label 'linux_slave'}
            steps{
                sh 'mvn package'
            }
        }

    }
}


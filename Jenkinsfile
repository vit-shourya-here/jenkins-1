pipeline{
    agent any
    stages{
        stage('Checkout'){
            step{
                git branch:'main', url:'https://github.com/vit-shourya-here/jenkins-1.git'
            }
        }
        stage('Build'){
            steps{
                bat 'python -m py_compile app.py'
                echo 'Build success!!'
            }
        }
        stage('Send Notification'){
            steps{
                echo 'EMAIL SI SENT -> TO: shourya.oza2024@vitstudent.ac.in|Subject: Build Notification JobName: ${env.JOB_NAME} Build Number: #${env.BUILD_NUMBER}'
            }
        }
    }
}
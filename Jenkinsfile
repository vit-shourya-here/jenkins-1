pipeline{
    agent any
    parameters{
        booleanParam(
            name:'RUN_EXTRA_CHECKS',
            defaultValue: true,
            description: 'Run when true'
        )
    }
    stages{
        stage('Checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/vit-shourya-here/jenkins-1.git'
            }
        }
        stage('Build'){
            steps{
                bat 'python -m py_compile conditional.py'
            }
        }
        stage('EXTRA CHECK'){
            when{
                expression{
                    params.RUN_EXTRA_CHECKS == true
                }
            }
            steps{
                bat "python -c \"from conditional import greet; print(greet('Students'))\""
            }
        }
    }
}
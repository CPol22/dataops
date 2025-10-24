pipeline {
    agent any

    environment {
        TERRAFORM_PATH = "E:\\PYTHON\\dataops\\terraform\\terraform.exe"
        PYTHON_PATH = "C:\\Users\\paulb\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
    }

    stages {
        stage('Clonando repositorio') {
            steps {
                deleteDir()
                git branch: 'main', url: 'https://github.com/CPol22/dataops.git'
            }
        }

        stage('Terraform Init') {
            steps {
                dir('terraform') {
                    echo " Inicializando Terraform..."
                    bat "\"${env.TERRAFORM_PATH}\" init"
                }
            }
        }

        stage('Terraform Validate') {
            steps {
                dir('terraform') {
                    echo " Validando configuración de Terraform..."
                    bat "\"${env.TERRAFORM_PATH}\" validate"
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                dir('terraform') {
                    echo " Simulando infraestructura ..."
                    bat "\"${env.TERRAFORM_PATH}\" plan -out=plan.txt"
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                dir('terraform') {
                    echo " Aplicando simulación de infraestructura..."
                    bat "\"${env.TERRAFORM_PATH}\" apply -auto-approve"
                }
            }
        }

        stage('Preparar entorno Python') {
            steps {
                echo "Creando entorno virtual e instalando dependencias..."
                bat "\"${env.PYTHON_PATH}\" -m venv venv"
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Ejecutar análisis climático') {
            steps {
                echo "Ejecutando script principal..."
                bat 'venv\\Scripts\\activate && python main.py'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: '**/*.txt', fingerprint: true
            echo ' Infraestructura y análisis completados exitosamente.'
        }
        failure {
            echo ' Error durante la ejecución del pipeline.'
        }
        always {
            echo ' Pipeline finalizado.'
        }
    }
}




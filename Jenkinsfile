pipeline {
    agent any
    stages {
        stage('Clonar repositorio') {
            steps {
                deleteDir()
                git branch: 'main', url: 'https://github.com/CPol22/dataops.git'
            }
        }
        stage('Ejecutar Terraform') {
            steps {
                dir('terraform') {
                    bat 'terraform init'
                    bat 'terraform plan'
                    bat 'terraform validate'
                }
            }
        }
        stage('Preparar entorno') {
            steps {
                echo "Instalando dependencias..."
                bat '"C:\\Users\\paulb\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv'
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
            echo 'Análisis climático completado exitosamente.'
        }
        failure {
            echo 'Error en la ejecución del análisis climático.'
        }
    }
}



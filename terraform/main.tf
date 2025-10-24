terraform{
    required_providers {
      local ={
        source = "hashicorp/local"
        version = "~> 2.5.1"
      }
    }
}

provider "local" {}

# Variable opcional ( servidor)
variable "nombre_servidor" {
  description = "Icarus"
  type = string
  default = "Servidor_Prueba"
} 

#Este recurso crea un archivo local que representa la 'infraestructura'
resource "local_file" "infra" {
  filename = "${var.nombre_servidor}.txt"
  content  = "Infraestructura simulada creada exitosamente. Timestamp: ${timestamp()}"
}


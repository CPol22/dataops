terraform{
    required_providers {
      local ={
        source = "hashicorp/local"
        version = "> 1.13.4"
      }
    }
}

provider "local" {}

# Variable opcional ( servidor)
variable "icarus" {
  description = "Icarus"
  type = string
  default = "Servidor_Prueba"
}

#Este recurso crea un archivo local que representa la 'infraestructura'
resource "local_file" "infra" {
  filename = "${var.icarus}.txt"
  content  = "Infraestructura simulada creada exitosamente. Timestamp: ${timestamp()}"
}
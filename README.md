##  DATA OPS

Este proyecto fue desarrollado con fines académicos para demostrar la aplicación de principios de **DataOps**, combinando automatización, análisis de datos y control de versiones.  
Su propósito es integrar la **obtención, procesamiento y reporte de información climática** dentro de un flujo automatizado, asegurando eficiencia, trazabilidad y reproducibilidad en cada ejecución.

---

##  Flujo del Pipeline 

El proceso completo se ejecuta automáticamente mediante **Jenkins** en las siguientes etapas:

1. **Clonar repositorio** – Obtiene el código actualizado desde GitHub.  
2. **Terraform Init / Validate / Plan / Apply** – Inicializa, valida y aplica la infraestructura simulada definida como código.  
3. **Preparar entorno Python** – Crea un entorno virtual y descarga dependencias.  
4. **Ejecutar análisis climático** – Procesa los datos JSON, genera el gráfico y crea el reporte.  
5. **Publicar resultados** – Archiva los reportes generados y muestra el resultado en Jenkins.

---

##  Infraestructura como Código (IaC)

Terraform se utiliza para definir y desplegar infraestructura de manera declarativa.  
En este caso, genera un archivo local que simula una infraestructura virtual.  
El código IaC garantiza **automatización, reproducibilidad, control de versiones y escalabilidad**, integrándose directamente en el flujo CI/CD del pipeline.

---

##  Integración Continua / Entrega Continua (CI/CD)

El pipeline CI/CD de Jenkins:
- Ejecuta todo el flujo automáticamente al realizar un *commit* en GitHub.  
- Garantiza que cada etapa sea reproducible, controlada y auditable.  
- Permite escalar el proyecto fácilmente hacia entornos reales de nube o contenedores.

---

##  Requisitos Previos

- **Python 3.12** instalado y accesible en el PATH.
- **Terraform** disponible localmente (ruta configurada en `Jenkinsfile`).
- **Jenkins** configurado con el plugin *Pipeline*.
- **Git** instalado y accesible desde el agente Jenkins.

---

##  Ejecución Manual (modo local)

Puedes probar el flujo sin Jenkins:

```bash
# 1. Clonar el repositorio
git clone https://github.com/CPol22/dataops.git
cd dataops

# 2. Ejecutar Terraform
cd terraform
terraform init
terraform apply -auto-approve

# 3. Volver al directorio principal
cd ..

# 4. Crear entorno virtual e instalar dependencias
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# 5. Ejecutar el análisis
python main.py
```
---
AUTOR: PAUL CHAVEZ


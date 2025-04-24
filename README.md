# agnervillafabrega-devops

Bienvenido a mi repositorio **DevOps Labs**, donde documento mis prácticas, laboratorios y scripts de automatización para diferentes entornos cloud y locales.

## 📂 Estructura del repositorio

- **docs/**  
  Guías, plantillas y normas de estilo para contribuir y documentar nuevos laboratorios.

- **labs/**  
  Laboratorios “hands-on” organizados por tecnología:
  - `k8s/` – Kubernetes
  - `localstack/` – Emulación AWS con Localstack (Terraform y OpenTofu)
  - `oci/` – Oracle Cloud Infrastructure

- **aws/**  
  Scripts reales para AWS (DynamoDB, EC2, etc.).

- **oci/**  
  Scripts reales para OCI.
- **localstack-setup/**  
  Archivo `compose.yml` y configuración general de Localstack.

- **python-labs/**  
  (Por crear) Laboratorios de Python para automatización, análisis de datos, etc.

- **technical-test/** _(submódulo)_  
  Pruebas técnicas para procesos de selección, mantenidas como sub-módulo Git.

## 🚀 Cómo empezar

1. Clona el repositorio y submódulos:
   ```bash
   git clone --recurse-submodules https://github.com/AgnerVillaFabrega/agnervillafabrega-devops.git
2. Instala dependencias globales (por ejemplo Docker, AWS CLI, Terraform).

3. Revisa la carpeta docs/LAB_TEMPLATE.md para guiarte al crear nuevos labs.
# agnervillafabrega-devops

Bienvenido a mi repositorio **DevOps Labs**, donde documento mis prácticas, laboratorios y scripts de automatización para diferentes entornos cloud y locales.

## Informacion básica:
¡Laboratorio Localstack junto a Terraform y OpenTofu para aprovisionar recursos de AWS de forma 100% local! 🔧💻

🔹 __¿Qué es Localstack?__

Es un emulador de servicios AWS que corre en Docker, ideal para pruebas y desarrollo sin necesidad de cuentas en la nube ni costos asociados.

🔹 __¿Qué se hace en el lab?__

1️⃣ Instala y verifica Terraform y OpenTofu en WSL/Ubuntu.

2️⃣ Configura Localstack en Docker Compose (S3, DynamoDB, EC2).

3️⃣ Crea y destruye un bucket S3, una tabla DynamoDB y una “instancia EC2” simulada con Terraform apuntando a Localstack.

4️⃣ Repite todo el flujo con OpenTofu, demostrando que puedes migrar sin esfuerzo.


__¿Por qué vale la pena?__

✔️ Cero costes: practica sin consumir recursos reales.

✔️ Workflow real: usa las mismas herramientas de IaC que en producción.

✔️ Flexibilidad: cambia entre Terraform y OpenTofu en segundos.

 
## 📂 Estructura del repositorio

```plaintext
agnervillafabrega-devops/
├── README.md            ← Visión general del repo
├── aws/                 ← Scripts y utilidades para AWS “reales”  
├── docs/                ← Guías, plantillas y normas de contribución/documentación
│   └── PR-README.md     ← Plantilla e instrucciones para Pull Requests y documentación de
├── labs/                ← Laboratorios prácticos organizados por tecnología  
├── oci/                 ← Scripts y herramientas para Oracle Cloud Infrastructure  
└── technical-tests/     ← Submódulos con pruebas técnicas usadas en procesos de selección  
```

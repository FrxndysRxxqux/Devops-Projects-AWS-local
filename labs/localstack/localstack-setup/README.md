Ejercicio 3: Configurar Localstack y AWS CLI

Levanta Localstack: Asegúrate de que tu docker-compose.yml incluya (o en su defecto usar el del repositorio):

```
services:
  localstack:
    image: localstack/localstack
    ports:
      - "4566:4566"
    environment:
      - SERVICES=s3,dynamodb,ec2
      - AWS_DEFAULT_REGION=us-east-1
```

```bash
docker-compose up -d
```

Configurar perfil AWS local: Edita ~/.aws/credentials y agrega:

```text
[localstack]
aws_access_key_id = test
aws_secret_access_key = test
```

En ~/.aws/config:

```text
[profile localstack]
region = us-east-1
output = json
```

Verificar con awscli:

```bash
aws --endpoint-url=http://localhost:4566 s3 ls --profile localstack
```

Debe regresar un listado vacío sin error.
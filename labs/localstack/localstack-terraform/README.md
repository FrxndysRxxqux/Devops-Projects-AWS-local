**Inicializar Terraform:**

```bash
terraform init
```

Planificar:

```bash
terraform plan
```

Aplicar:

```bash
terraform apply -auto-approve
```

Verificar en Localstack:

```bash
aws --endpoint-url=http://localhost:4566 s3 ls --profile localstack
aws --endpoint-url=http://localhost:4566 dynamodb list-tables --profile localstack
aws --endpoint-url=http://localhost:4566 ec2 describe-instances --profile localstack
```

Destruir recursos:

```bash
terraform destroy -auto-approve

```

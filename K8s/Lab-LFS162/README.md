# 🚀 Desplegar una Aplicación de Ejemplo en Kubernetes

En este ejercicio, desplegaremos una aplicación básica (`nginx`) y la accederemos localmente.

---

## 1. Crear el archivo `webapp.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
        - name: nginx
          image: nginx
```

## 2. Desplegar la aplicación
Aplica el manifiesto con:

```bash
kubectl apply -f webapp.yaml
```

## 3. Verificar el despliegue
Comprueba que el Deployment se creó correctamente:

```bash
kubectl get deployments
```
Ejemplo de salida:

```pgsql
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
webapp   2/2     2            2           30s
```

## 4. Exponer la aplicación con port-forwarding
En una nueva terminal, ejecuta:
```bash
kubectl port-forward deploy/webapp 8080:80
```
Esto redirige el puerto 8080 de tu máquina local al puerto 80 del contenedor nginx dentro del pod. Puedes acceder desde el navegador o con curl a `http://localhost:8080`

## 5. Eliminar el despliegue
Cuando termines, puedes limpiar el entorno con:
```bash
kubectl delete deploy webapp
```

📄 Basado en contenido de The Linux Foundation 2024. Todos los derechos reservados.
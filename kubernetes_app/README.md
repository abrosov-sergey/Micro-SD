# запуск

1. **запустить/подключиться к k8s кластеру**

2.

```
docker build -t fastapi-app:latest .
```
3.  

```
docker push  <ваш логин в dockerhub>/fastapi-app:latest
```

3. 
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

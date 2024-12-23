#!/bin/bash

docker build -t awesomecosmonaut/config-service-app /home/oleg/Documents/Micro-SD/kubernetes_app/config_service
docker build -t awesomecosmonaut/dataprocessing-app /home/oleg/Documents/Micro-SD/kubernetes_app/dataprocessing
docker build -t awesomecosmonaut/db-service-app /home/oleg/Documents/Micro-SD/kubernetes_app/db_service
docker build -t awesomecosmonaut/email-app /home/oleg/Documents/Micro-SD/kubernetes_app/email_service
docker build -t awesomecosmonaut/session-service-app /home/oleg/Documents/Micro-SD/kubernetes_app/session_service

docker push awesomecosmonaut/config-service-app:latest
docker push awesomecosmonaut/dataprocessing-app:latest
docker push awesomecosmonaut/db-service-app:latest
docker push awesomecosmonaut/email-app:latest
docker push awesomecosmonaut/session-service-app:latest 

kubectl delete deployments --all -n metal-project
kubectl delete services --all -n metal-project

kubectl apply -f config_service/deployment -n metal-project
kubectl apply -f dataprocessing/deployment -n metal-project
kubectl apply -f db_service/deployment -n metal-project
kubectl apply -f email_service/deployment -n metal-project
kubectl apply -f session_service/deployment -n metal-project



# kubectl apply -f network-policy.yaml -n metal-project

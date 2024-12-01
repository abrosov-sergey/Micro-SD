# startup

1. **select asd2024 k8s cluster context**
2.
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```


ChatGPT prompt:
```
I am working on software design project. Here is my project architecture. Here is wagger documentation. I want you to add a router for Data Processor. It should include functions such as data quality check, data cleansing, data merging, data anonymizer and data transformer. It should take dataset a, dataset b as input and return the finished dataset. I want you to add a router for Data Processor to swagger documenttaion. It should include functions such as data quality check, data cleansing, data merging, data anonymizer and data transformer. It should take dataset a, dataset b as input and return the finished dataset. add enum field to /anonymize with possible params +string HidePhoneNum +string HideEMail +string HideRandomSymbols +string ApplyHash. 
I want you to generate a python microservice based on the information in this swagger documentation. Please use pandas for data manipulation, also use fastapi as a framework to create rest api. use headers like that headers = {'Content-Disposition': 'inline; filename="sample.pdf"',"content-type": "application/octet-stream"} .  add raise HTTPException at whole code.
```

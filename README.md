# architectureMAI

Запуск приложения 

```commandline
docker network create composition_network
docker-compose up -d
```

После запуска доступен swagger по адресу http://localhost:8080/docs

OpenApi документация доступна по адресу http://localhost:8080/openapi.json

Запрос для проверки работы nginx
```
 curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d '{"login": "Pupkin", "password": "Abracadabra"}' http://127.0.0.1:8080/login/
```

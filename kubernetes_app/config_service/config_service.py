from fastapi import FastAPI, UploadFile, HTTPException
import yaml
import requests

app = FastAPI()

# Настройки API — используем имена контейнеров
DB_SERVICE_URL = "http://db-service:8000"
SESSION_SERVICE_URL = "http://session-service:8080/sessions"

@app.post("/process-config/")
async def process_config(file: UploadFile):
    """
    Получает YAML файл, валидирует и обрабатывает его
    """
    try:
        # 1. Считываем содержимое файла
        content = await file.read()
        config = yaml.safe_load(content)

        # 2. Проверяем базовую структуру YAML
        if not isinstance(config, dict):
            raise HTTPException(status_code=400, detail="Некорректный YAML файл")

        if "file_name" not in config or "action" not in config or "columns" not in config:
            raise HTTPException(status_code=400, detail="YAML файл должен содержать file_name, action, columns")

        # 3. Проверяем наличие файла в первом микросервисе
        file_name = config["file_name"]
        response = requests.get(f"{DB_SERVICE_URL}/download/{file_name}")
        
        if response.status_code == 422:
            raise HTTPException(status_code=400, detail="Файл отсутствует в DB")

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Ошибка при запросе к DB")

        # 4. Загружаем файл в первый микросервис
        with open(file_name, "rb") as file_to_upload:
            upload_response = requests.post(
                f"{DB_SERVICE_URL}/upload/",
                files={"file": (file_name, file_to_upload)}
            )

        if upload_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Ошибка при загрузке файла в DB")

        # 5. Передаём конфигурацию в третий микросервис в формате JSON
        session_request_payload = {
            "file_name": config["file_name"],
            "action": config["action"],
            "columns": config["columns"]
        }

        session_service = requests.post(SESSION_SERVICE_URL, json=session_request_payload)

        if session_service.status_code == 201:
            return {"message": "Сессия успешно создана"}
        elif session_service.status_code == 400:
            raise HTTPException(status_code=400, detail="Неверные данные запроса в Session")
        else:
            raise HTTPException(status_code=500, detail="Ошибка при создании сессии в Session")

    except yaml.YAMLError as e:
        raise HTTPException(status_code=400, detail=f"Ошибка в синтаксисе YAML: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Неизвестная ошибка: {str(e)}")
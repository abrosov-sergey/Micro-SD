from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import FileResponse
from decouple import config
import boto3
from botocore.exceptions import NoCredentialsError
import os
from uuid import uuid4

app = FastAPI()

# Настройка клиента S3
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_BUCKET_NAME = config("AWS_BUCKET_NAME")
AWS_ENDPOINT_URL = config("AWS_ENDPOINT_URL")  # Кастомный эндпоинт

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    endpoint_url=AWS_ENDPOINT_URL,
)

@app.post("/upload/")
async def upload_file(file: UploadFile):
    """
    Эндпоинт для загрузки файла в S3.
    """
    try:
        unique_filename = f"{uuid4()}_{file.filename}"
        s3_client.upload_fileobj(file.file, AWS_BUCKET_NAME, unique_filename)
        file_url = f"{AWS_ENDPOINT_URL}/{AWS_BUCKET_NAME}/{unique_filename}"
        return {"message": "Файл успешно загружен!", "url": file_url}

    except NoCredentialsError:
        raise HTTPException(status_code=500, detail="Проблема с доступом к AWS S3")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{file_name}")
def download_file(file_name: str):
    """
    Эндпоинт для скачивания файла из S3 в локальную папку temp.
    """
    try:
        download_path = os.path.join("temp", file_name)
        os.makedirs("temp", exist_ok=True)

        s3_client.download_file(
            AWS_BUCKET_NAME,
            file_name,
            download_path,
        )
        return {"message": "Файл успешно скачан!", "file_path": download_path}

    except NoCredentialsError:
        raise HTTPException(status_code=500, detail="Проблема с доступом к AWS S3")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/serve/{file_name}")
async def serve_file(file_name: str):
    """
    Эндпоинт для передачи файла из локальной папки temp другому микросервису.
    """
    file_path = os.path.join("temp", file_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Файл не найден в локальной папке temp")
    
    try:
        return FileResponse(file_path, media_type="application/octet-stream", filename=file_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
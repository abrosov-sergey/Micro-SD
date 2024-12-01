# Используем официальный базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip && \
pip install --no-cache-dir -r requirements.txt

# Открываем порт
EXPOSE 8001

# Команда запуска приложения
CMD ["uvicorn", "config_service:app", "--host", "0.0.0.0", "--port", "8080"]
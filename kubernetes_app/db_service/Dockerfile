# Используем официальный базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Открываем порт для приложения
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

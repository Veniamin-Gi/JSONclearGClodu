# Указываем базовый образ Python
FROM python:3.9

# Копируем файлы внутрь контейнера
COPY clearjson.py /app/clearjson.py
COPY requirements.txt /app/requirements.txt
COPY YourJSON.json /app/YourJSON.json

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r /app/requirements.txt

# Указываем рабочую директорию
WORKDIR /app

# Запускаем скрипт ClearJSON.py
CMD ["python", "clearjson.py"]

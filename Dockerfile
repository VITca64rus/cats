# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.9
# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR sber
# Скачиваем/обновляем необходимые библиотеки для проекта 

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip -r requirements.txt
# |ВАЖНЫЙ МОМЕНТ| копируем содержимое папки, где находится Dockerfile, 
# в рабочую директорию контейнера
COPY sber sber
COPY start.py start.py
# Устанавливаем порт, который будет использоваться для сервера
EXPOSE 3000
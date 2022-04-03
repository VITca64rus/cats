# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.10.1
# Устанавливаем рабочую директорию для проекта в контейнере
RUN apt-get update
RUN mkdir /sber
WORKDIR /sber
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

ENTRYPOINT ["python3", "start.py"]
FROM python:3.10.1
RUN apt-get update
RUN mkdir /sber
WORKDIR /sber
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3000
ENTRYPOINT ["python3", "start.py"]
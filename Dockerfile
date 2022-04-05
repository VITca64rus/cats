FROM python:3.10.1

WORKDIR /sber

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000
ENTRYPOINT ["python3", "start.py"]
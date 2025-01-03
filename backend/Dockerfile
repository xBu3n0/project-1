FROM python:latest

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD [ "uvicorn", "src.main:app", "--reload", "--port=5000", "--host=0.0.0.0" ]

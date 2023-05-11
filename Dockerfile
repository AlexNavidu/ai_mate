FROM python:3.9

WORKDIR /code

COPY app/requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app/ /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]

FROM python:3.9

WORKDIR /app

COPY api_ai_mate/ .

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir --upgrade

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

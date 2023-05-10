# main.py

from fastapi import FastAPI

# Создание объекта приложения.
app = FastAPI()

# Декоратор, определяющий, что GET-запросы к основному URL приложения
# должны обрабатываться этой функцией.
@app.get('/')
def read_root():
    return {'Hello': 'FastAPI'}

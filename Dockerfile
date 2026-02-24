FROM python:3.11

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code

EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--port", "8000"]
FROM python:3.11-slim

WORKDIR /Nutrient-Calculator

ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir logs

EXPOSE 8000

COPY . .

RUN find . -name "__pycache__" -type d -exec rm -rf {} +

CMD [ "uvicorn", "Backend.urls:app", "--host", "0.0.0.0" ]
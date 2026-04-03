FROM python:3.11-slim

WORKDIR /Nutrient-Calculator_Frontend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir logs

EXPOSE 65011

COPY . .

RUN find . -name "__pycache__" -type d -exec rm -rf {} +

CMD [ "flet", "run", "--web","--host", "0.0.0.0", "--port", "8500", "main.py" ]

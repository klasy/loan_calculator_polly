#server django Dockerfile
FROM python

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "loan_calculator_calculator.wsgi:application", "--config", "gunicorn.conf.py"]
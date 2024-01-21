FROM python

WORKDIR /app

COPY . /app



CMD ["python", "./password_generator.py"]

# Microservice-Calculator

pip install -r requirements.txt

python -m venv venv

source .venv/bin/activate



### CURRENTLY TO TEST CELERY APP:

```bash
docker run -d -p 5672:5672 rabbitmq
celery -A celery worker -l info
```


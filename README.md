# Microservice-Calculator

pip install -r requirements.txt

python -m venv venv

source .venv/bin/activate



### CURRENTLY TO TEST CELERY APP:

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
docker run -d -p 5672:5672 rabbitmq
celery -A celery worker -l info
```


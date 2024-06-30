# Microservice-Calculator

pip install -r requirements.txt

python -m venv venv

source .venv/bin/activate



### CURRENTLY TO TEST CELERY APP:

docker-compose -f src/proj/docker-compose.yml up --build

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
docker run -d -p 5672:5672 rabbitmq
celery -A celery worker -l info
```

### New Run Stuff

Make sure Docker Desktop is up and running

```bash
docker-compose build
```
```bash
docker pull mher/flower:0.9.5 
```
```bash
docker pull rabbitmq:management
```
```bash
docker stack deploy --compose-file=docker-compose.yml calculator
```


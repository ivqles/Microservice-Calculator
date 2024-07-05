# Microservice Calculator

This application simulates a calculator using Flask, Python, Celery, RabbitMQ, and Docker. The Flask API exposes user requests to generate operations to test the queue performance.

## How To Execute

1. Install the requirements and (optional) create a virtual environment.
    ```bash
    pip install -r requirements.txt

    python -m venv venv

    source .venv/bin/activate
    ```
    If you'd like to manually install requirements, here is the list:
    - Flask 3.0.3
    - Celery 5.4.0
2. Install [RabbitMQ](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#id7) and [Docker](https://docs.docker.com/engine/install/).
3. Ensure your Docker Daemon is running. For easier monitoring, Docker Desktop is suggested.
4. Run the Docker Compose command line to set up the Docker containers:
    ```bash
    docker-compose -f src/proj/docker-compose.yml up --build
    ```
5. To generate \<count> random tasks per each operation (add, subtract, multiply, divide), run the following line in your web url, replacing \<count> with your desired number of tasks:
   ```
   0.0.0.0/5001/create_tasks/<count>
   ```
6. Observe the queue performance by visiting the included [RabbitMQ Management tool](http://localhost:15672/).

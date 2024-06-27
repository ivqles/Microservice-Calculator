from proj.rabbitmq_config import RABBITMQ_USER, RABBITMQ_PWD, RABBITMQ_HOST, RABBITMQ_PORT

broker_url = f'pyamqp://{RABBITMQ_USER}:{RABBITMQ_PWD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}'
backend = 'rpc://'
# Docker

This is the file used to build the docker-container:

* ``docker-compose.yml``

# Dev Environment

Setting up the docker dev environment is quite simple (it is assumed you have docker up and running, and you know how to use docker-compose):

1. Run ```docker-compose build``` to build the Dockerfiles for this project
2. Follow these steps to settup the project:
2.a: Run migrations: ```docker-compose run --rm python python manage.py migrate```
2.b: Create a super user: ```docker-compose run --rm python python manage.py createsuperuser```
3. Last but not least, we can start all services using ```docker-compose up```. You should be able to access the app via **http://0.0.0.0:8000/** in your browser.

# System Maintenance

1. Reload systemd: ``systemctl daemon-reload``
2. And enable the service: ``systemctl enable docker-compose-django``
3. Start the service (or reboot): ``systemctl start docker-compose-django``

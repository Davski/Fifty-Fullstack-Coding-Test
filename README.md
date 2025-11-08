# Fifty-Fullstack-Coding-Test
A coding test for Fifty using Python, Django, PostgreSQL

An example .env file to have within your root folder of the project

POSTGRES_DB=sensorsdb
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
DJANGO_SECRET_KEY=djangosecretkey
DJANGO_DEBUG=False

Use the Makefile commands to run the system locally.
make up: Put up containers, networks and volumes.
make down: Turn off and remove containers and networks.
make migrate: Run makemigrations and migrate
make seed: Seed the database by creating the sensors table and seeding it with the csv-file.
make test to run all tests
make clean to turn off and remove containers and networks and also remove volumes.

The API overview is located within http://localhost:8000/api/docs
# Fifty-Fullstack-Coding-Test
A coding test for Fifty using Python, Django, PostgreSQL

An example .env file to have within your root folder of the project

```env
POSTGRES_DB=sensorsdb
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
DJANGO_SECRET_KEY=djangosecretkey
DJANGO_DEBUG=False
```

Use the Makefile commands to run the system on docker.  
make full: runs make up && make migrate && make seed. (Recommended for first time use)  
make up: Put up containers, networks and volumes.  
make logs: Show the Docker console logs.  
make down: Turn off and remove containers and networks.  
make migrate: Run makemigrations and migrate.  
make seed: Seed the database with one user, five sensors and run make seed_readings.  
make seed_readings: Seed the database with sensor readings from csv file. Uses a hacky method under development.  
make test to run all tests, currently no tests exist.  
make clean to turn off and remove containers and networks and also remove volumes.  
make connect: Connects to psql through CLI to check the database manually using env variables.

The API overview is located within http://localhost:8000/api/docs

The code currently DOES NOT support.

Actually logging in and owning sensors by user.  
What happens is on successful login the access and refresh tokens are printed on the screen.  

Seeding the readings database through a model manager.  
This would be required to make each sensor own its readings through a foreign key.  
An actual separate frontend page with paginations to see readings and filter them, own or delete them.  
A graph to show the data visually.  
Styling for the frontend.  
Actual tests using pytest and pytest-django.  

What can be tested:  
api/docs works, has schemas and docstrings to explain the different apis.  
The frontend and backend has error handling included, and one can register, "login", and get sensor readings.

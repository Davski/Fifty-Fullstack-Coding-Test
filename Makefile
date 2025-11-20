ifneq (,$(wildcard .env))
	include .env
	export $(shell sed 's/=.*//' .env)
endif

up:
	docker compose run --rm web python manage.py makemigrations fifty_apis
	docker compose up --build -d
logs:
	docker compose logs -f

connect:
	docker compose exec db psql -d ${POSTGRES_DB} -U ${POSTGRES_USER}

migrate:
	docker compose exec web python manage.py makemigrations && docker compose exec web python manage.py migrate

test:

seed:
	docker compose exec web python manage.py seed_database

seed_old:
	docker compose exec db psql -d ${POSTGRES_DB} -U ${POSTGRES_USER} -c "\COPY fifty_apis_reading FROM '/tmp/seed_files/sensor_readings_wide.csv' DELIMITER ',' CSV HEADER"

down:
	docker compose down

full:
	make up &&  make migrate && make seed

clean:
	docker compose down -v
	rm -rf backend/fifty_apis/migrations/0*.py

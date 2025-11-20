up:
	docker compose run --rm web python manage.py makemigrations fifty_apis
	docker compose up --build -d
logs:
	docker compose logs -f

migrate:
	docker compose exec web python manage.py makemigrations && docker compose exec web python manage.py migrate

test:

seed:
	docker compose exec db psql -d sensorsdb -U fiftyuser -c "\COPY fifty_apis_reading FROM '/tmp/seed_files/sensor_readings_wide.csv' DELIMITER ',' CSV HEADER"

down:
	docker compose down

clean:
	docker compose down -v
	rm -rf backend/fifty_apis/migrations/0*.py

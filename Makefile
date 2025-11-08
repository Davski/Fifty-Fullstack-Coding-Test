up:
	docker compose up --build
migrate:
	docker compose exec web python manage.py makemigrations && docker compose exec web python manage.py migrate
test:
seed:
	docker compose exec db psql -d sensorsdb -U fiftyuser -f /tmp/seed_database.sql
	docker compose exec db psql -d sensorsdb -U fiftyuser -c "\COPY sensors FROM '/tmp/sensor_readings_wide.csv' DELIMITER ',' CSV HEADER"
down:
	docker compose down
clean:
	docker compose down -v

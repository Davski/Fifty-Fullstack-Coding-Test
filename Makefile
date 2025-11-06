up:
	docker compose up --build
migrate:
	docker compose exec web python manage.py makemigrations && docker compose exec web python manage.py migrate
test:
seed:
down:
	docker compose down
clean:
	docker compose down -v

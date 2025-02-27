PORT = 8080
HOST = localhost

start_db:
	docker compose -f dev.docker-compose.yml up -d

stop_db:
	docker compose -f dev.docker-compose.yml down

migrate:
	alembic upgrade head

migration.autogenerate:
	alembic revision --autogenerate -m "${name}"

migration.manual:
	alembic revision -m "${name}"

run:
	python main.py



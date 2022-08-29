deps-up:
	docker-compose up -d

deps-down:
	docker-compose down --volumes

migrate-up:
	python3 manage.py migrate

make-migrations:
	python3 manage.py makemigrations classesmodules

dev-run:
	python3 manage.py runserver

test: deps-down deps-up
	AUTH_ENABLED=FALSE \
	pytest -s

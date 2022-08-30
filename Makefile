deps-up:
	docker-compose up -d

deps-down:
	docker-compose down --volumes

migrate-up:
	python3 manage.py migrate

make-migrations:
	python3 manage.py makemigrations classesmodules

create-superuser:
	python3 manage.py createsuperuser

dev-run:
	python3 manage.py runserver

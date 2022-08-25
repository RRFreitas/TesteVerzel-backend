deps-up:
	docker-compose up -d
	docker attach testeverzel-wait-1 || true

deps-down:
	docker-compose down --volumes

migrate-up:
	python3 manage.py migrate

dev-run:
	python3 manage.py runserver

test: deps-down deps-up
	AUTH_ENABLED=FALSE \
	pytest -s
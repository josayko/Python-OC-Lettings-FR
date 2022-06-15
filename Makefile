all:	build run

build:
	docker build -t oc-lettings .

run:
	docker run --rm -p 8000:8000 --env-file .env oc-lettings

fixture:
	python manage.py loaddata users addresses lettings profiles

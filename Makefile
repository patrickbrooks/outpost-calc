# outpost-calc/Makefile

all: image

image:
	docker build -t outpost-calc:latest .

run:
	docker run --name outpost-calc -d -p 8000:5000 --rm outpost-calc:latest
#!make

build:
	docker build . -t alpine-blockchain

dev:
	docker run --rm -ti alpine-blockchain

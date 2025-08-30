SHELL := /bin/bash

# Variables definitions
# -----------------------------------------------------------------------------

ifeq ($(TIMEOUT),)
TIMEOUT := 60
endif

ifeq ($(MODEL_PATH),)
MODEL_PATH := ./ml/model/
endif

ifeq ($(MODEL_NAME),)
MODEL_NAME := model.pkl
endif

# Target section and Global definitions
# -----------------------------------------------------------------------------
.PHONY: all clean test install run deploy down dev dev-down dev-logs dev-worker dev-worker-logs service-logs

all: clean test install run deploy down

test:
	poetry run pytest tests -vv --show-capture=all

install: generate_dot_env
	pip install --upgrade pip
	pip install poetry
	poetry install --with dev

run:
	PYTHONPATH=app/ poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000

run_worker:
	python -m saq app.worker.settings

deploy: generate_dot_env
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

# Development environment targets
dev: generate_dot_env_dev
	docker-compose -f docker-compose.dev.yml up -d

dev-down:
	docker-compose -f docker-compose.dev.yml down

dev-logs:
	docker-compose -f docker-compose.dev.yml logs -f

dev-worker:
	docker-compose -f docker-compose.dev.yml up -d mainframe_worker

dev-worker-logs:
	docker-compose -f docker-compose.dev.yml logs -f mainframe_worker

service-logs:
	docker-compose -f docker-compose.dev.yml logs -f mainframe_services

generate_dot_env:
	@if [[ ! -e .env ]]; then \
		cp .env.example .env; \
	fi

generate_dot_env_dev:
	@if [[ ! -e .env ]]; then \
		cp env.dev.example .env; \
	fi

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
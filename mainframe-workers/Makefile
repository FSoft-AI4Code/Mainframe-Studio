.PHONY: install test lint clean run setup-rabbitmq dev dev-logs dev-down dev-restart dev-status help

help:
	@echo "Available commands:"
	@echo "  install      - Install dependencies and setup RabbitMQ"
	@echo "  test         - Run tests"
	@echo "  lint         - Run linting checks"
	@echo "  format       - Format code with black and isort"
	@echo "  clean        - Clean up Python cache files"
	@echo "  run          - Run the worker"
	@echo ""
	@echo "Airflow Dev Stack:"
	@echo "  dev          - Start Airflow dev stack"
	@echo "  dev-logs     - Tail Airflow dev stack logs"
	@echo "  dev-down     - Stop Airflow dev stack"
	@echo "  dev-restart  - Restart Airflow dev stack"
	@echo "  dev-status   - Show Airflow dev stack status"
	@echo ""
	@echo "Web UI: http://localhost:8080 (when dev stack is running)"

setup-rabbitmq:
	@docker ps | grep rabbitmq > /dev/null || ( \
		docker run -d --name rabbitmq \
		-p 5672:5672 -p 15672:15672 \
		rabbitmq:3-management \
	)

install: setup-rabbitmq
	poetry install

test:
	python -m pytest tests/

lint:
	flake8 .
	black --check .
	isort --check-only .

format:
	black .
	isort .

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +

run:
	poetry run python src/worker.py all

# Airflow Dev Stack Commands
dev:
	@echo "Starting Airflow dev stack..."
	@docker network create mainframe-dev-network 2>/dev/null || true
	@docker-compose -f docker-compose-airflow-dev.yaml up -d
	@echo "Airflow dev stack started. Web UI: http://localhost:8080"

dev-logs:
	@echo "Tailing Airflow dev stack logs..."
	@docker-compose -f docker-compose-airflow-dev.yaml logs -f --tail=100

dev-down:
	@echo "Stopping Airflow dev stack..."
	@docker-compose -f docker-compose-airflow-dev.yaml down
	@echo "Airflow dev stack stopped"

dev-restart:
	@echo "Restarting Airflow dev stack..."
	@docker-compose -f docker-compose-airflow-dev.yaml down
	@docker-compose -f docker-compose-airflow-dev.yaml up -d
	@echo "Airflow dev stack restarted. Web UI: http://localhost:8080"

dev-status:
	@echo "Airflow dev stack status:"
	@docker-compose -f docker-compose-airflow-dev.yaml ps
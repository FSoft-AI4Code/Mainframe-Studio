FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

COPY pyproject.toml ./

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends default-jdk-headless git \
    && rm -rf /var/lib/apt/lists/*

COPY . /workspace

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONPATH=/workspace/app/

RUN poetry install --no-root  && rm -rf $POETRY_CACHE_DIR
RUN poetry self add poetry-dotenv-plugin

CMD ["poetry", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port","8000"]

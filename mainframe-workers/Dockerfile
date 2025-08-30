FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /workspace

COPY pyproject.toml ./

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

RUN apt update \
    && apt install -y git

COPY . /workspace

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONPATH=/workspace/app/

RUN poetry lock --regenerate
RUN poetry -v install --no-root  && rm -rf $POETRY_CACHE_DIR
RUN poetry self add poetry-dotenv-plugin

CMD ["poetry", "run", "python", "src/worker.py", "all"]

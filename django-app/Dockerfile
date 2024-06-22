FROM python:3.12-slim

ENV POETRY_VERSION=1.8.3

WORKDIR /src

COPY ./ ./

RUN set -e

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false
RUN if [ $DEV = "true" ]; then \
        poetry install --no-interaction --no-root --no-ansi ; \
    else \
        poetry install --no-interaction --no-root --no-ansi --no-dev ; \
    fi

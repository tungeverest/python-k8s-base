FROM python:3.8-slim-bookworm as python-base-prod
LABEL maintainer="Tony Tran <tttung.everest@outlook.com>"
WORKDIR /app
EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Install dependencies
RUN apt-get update -y && apt-get install -y \
    ca-certificates wget jq curl git nano gettext \
    chrpath iputils-ping postgresql-client \
    procps shared-mime-info mime-support
RUN apt-get install -y --no-install-recommends build-essential \
    libxft-dev libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev \
    libffi-dev libjpeg-dev libpq-dev libssl-dev libtiff-dev libwebp-dev zlib1g-dev
# Cleanup apt cache
RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry==1.7


FROM python-base-prod
COPY ./pyproject.toml ./poetry.lock* ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

CMD  ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

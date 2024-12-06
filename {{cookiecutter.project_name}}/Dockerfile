# Builder Stage
FROM python:3.12-slim as builder

# Set environment variables for Poetry
ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME="/opt/poetry" \
    PATH="$POETRY_HOME/bin:$PATH"

# Install Poetry and other necessary tools
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get remove -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency files for Poetry
COPY pyproject.toml poetry.lock /app/

# Install dependencies in a virtual environment
RUN poetry config virtualenvs.create true \
    && poetry install --no-root --only main

# Application Stage
FROM python:3.12-slim as final

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/poetry/ /opt/poetry/
COPY --from=builder /root/.cache/pypoetry/ /root/.cache/pypoetry/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app

# Expose application port
EXPOSE {{cookiecutter.app_host_port}}

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "{{cookiecutter.app_host_port}}"]

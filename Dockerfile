FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY ../pyproject.toml .
COPY ../src/ ./src/

RUN uv venv
RUN uv pip install --upgrade pip

RUN uv sync

CMD ["uv", "run", "-m", "src.pipeline.main"]
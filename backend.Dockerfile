FROM python:3.9

COPY ./backend /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR app

RUN pip install --no-cache-dir --upgrade --user poetry
FROM python:3.9

COPY ./backend /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR app

RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install -e .

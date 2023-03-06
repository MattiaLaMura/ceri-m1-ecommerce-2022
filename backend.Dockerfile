FROM python:3.9

COPY ./backend /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR app

RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install -e .

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:2222", "--timeout", "600"]

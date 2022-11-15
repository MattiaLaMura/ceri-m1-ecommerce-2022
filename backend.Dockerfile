FROM python:3.9

COPY ./backend /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR app

RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install -e .

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:22", "--timeout", "600"]

# docker run -d -p 3306:3306 --name db -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=db mysql
# docker build -t backend -f backend.Dockerfile . && docker run -d --name backend --env-file .env -p 8000:22 backend
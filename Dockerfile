FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --upgrade pip
RUN pip install pygments
RUN pip install aiofiles

COPY ./app /app
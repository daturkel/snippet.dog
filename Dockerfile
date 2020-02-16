FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --upgrade pip
RUN pip install pygments
RUN pip install aiofiles
RUN pip install gunicorn==20.0.4
RUN pip install uvicorn==0.11.2

COPY ./app /app
COPY ./start.sh /start.sh
RUN chmod +x /start.sh

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app/ai_trace


RUN pip install --upgrade pip
COPY requirements.txt /app/ai_trace/
RUN pip install -r /app/ai_trace/requirements.txt


COPY ai_trace /app/ai_trace
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh


CMD ["/app/entrypoint.sh"]




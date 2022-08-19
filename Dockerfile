ARG PYTHON_VERSION="3.9.5"
FROM python:${PYTHON_VERSION}-slim-buster

CMD ["python3"]

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get -y install libpq-dev gcc

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN groupadd -g 61000 iheros \
  && useradd -g 61000 -l -M -s /bin/false -u 61000 iheros

COPY --chown=iheros:iheros . .
RUN pip install -r /usr/src/app/requirements.txt
RUN pip install gunicorn==20.1.0

COPY --chown=iheros:iheros entrypoint.sh /opt/bin/
RUN chmod +x /opt/bin/entrypoint.sh
RUN chown -R iheros /usr/src/app

USER iheros:iheros

ENTRYPOINT [ "/opt/bin/entrypoint.sh" ]

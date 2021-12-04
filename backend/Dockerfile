FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
EXPOSE 8000/tcp
RUN mkdir /backend
WORKDIR /app

RUN apk add --no-cache --virtual build-deps \
    make gcc g++ `# для сборки пакетов` \
    postgresql-dev `# для psycopg2` \
    libjpeg-turbo-dev zlib-dev libffi-dev cairo-dev libwebp-dev `# для pillow`

RUN apk add --no-cache \
    git `# для установки зависимостей из git` \
    libpq `# для psycopg2` \
    libjpeg-turbo zlib libffi cairo libwebp `# для pillow` \
    gettext


RUN pip install --upgrade pip
COPY requirements.txt /app
RUN pip install -r requirements.txt

RUN apk del --no-cache build-deps

COPY entrypoint.sh /app
RUN ["chmod", "+x", "entrypoint.sh"]
#ENTRYPOINT ["sh", "/backend/entrypoint.sh"]

COPY / /app/



FROM python:3.9.2
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR /app
COPY ./Pipfile /app/
COPY ./Pipfile.lock /app/

RUN pipenv update

#EXPOSE 8000

CMD ["pipenv", "run", "python", "pollsite/manage.py", "migrate"]
CMD ["pipenv", "run", "python", "pollsite/manage.py", "runserver", "0.0.0.0:8000"]


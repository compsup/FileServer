FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY mysite/requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
CMD [ "entrypoint.sh" ]
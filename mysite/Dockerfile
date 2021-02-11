FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY mysite/requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN cd /mysite/
RUN python3 /mysite/manage.py migrate
RUN cd ..
EXPOSE 8000
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000", "--settings=mysite.settings.production", "--insecure"]
FROM python:3
COPY requirements.txt /
COPY gunicorn.conf /
COPY . /
RUN pip install gunicorn
RUN pip install -r requirements.txt
CMD [ "gunicorn", "-c", "gunicorn.conf", "host_page:init_app" ]

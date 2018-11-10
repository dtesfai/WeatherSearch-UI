FROM python:3.6
ADD ./src /var/www/html/
WORKDIR /var/www/html/
RUN pip install -r requirements.txt
CMD python app.py
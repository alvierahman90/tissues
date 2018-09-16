FROM python:3.7
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app .
COPY config.json ./
EXPOSE 80
CMD [ "gunicorn", "-b", ":80", "tissues:app"]

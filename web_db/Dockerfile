FROM python:3

WORKDIR /website

EXPOSE 8099

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt # --no-cache-dir

COPY . .

CMD [ "python", "./main.py" ]
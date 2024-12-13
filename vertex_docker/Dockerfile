FROM python:3.11-slim

RUN python3 -m pip install --upgrade pip

WORKDIR /ws

COPY requirements.txt /ws/

COPY app/ /ws/

RUN pip3 install -r requirements.txt

COPY app/ .

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
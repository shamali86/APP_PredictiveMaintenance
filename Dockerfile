# Base Image
FROM python:3.11

WORKDIR /app

# push all files into a folder as app in the docker image
COPY . .

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5000

CMD ["streamlit", "run", "AppMachineFailurePredictor.py", "--server.port", "5000"]


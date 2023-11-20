FROM python:3.10-slim-buster
LABEL maintainer="it-support@cbmed.at"
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install -y \
    build-essential \
    curl \
    software-properties-common
RUN pip install pipenv
# creates Pipfile.lock
RUN pipenv lock
# creates requirements.txt file from Pipfile.lock
RUN pipenv requirements > requirements.txt
# installs from requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

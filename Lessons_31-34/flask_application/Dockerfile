FROM python:3.10
WORKDIR /data
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 4200
CMD ["python","run.py"]
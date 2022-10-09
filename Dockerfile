FROM python:3.8.10
RUN mkdir -p /usr/src/app/
COPY . /usr/src/app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
CMD ["python","/usr/src/app/main.py"]
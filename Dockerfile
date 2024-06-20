FROM python:3.13.0a2-slim-bullseye
WORKDIR /src
COPY requirements.txt .
RUN echo "default soft nofile 65535" >> /etc/security/limits.conf
RUN echo "fs.file-max = 65535" >> /etc/sysctl.conf
RUN python -m venv venv
RUN . venv/bin/activate

RUN pip install -r requirements.txt
COPY . ./
RUN ln -sf /dev/stdout /src/app.log \
    && ln -sf /dev/stderr /src/error.log
EXPOSE 5000
ENTRYPOINT ["python3", "src/app/app.py"]

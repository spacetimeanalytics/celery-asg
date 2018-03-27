FROM python:3-slim

ADD . /tmp/install_dir
RUN cd /tmp/install_dir && \
    pip install . && \
    rm /tmp/install_dir -rf

ENTRYPOINT /usr/local/bin/celery-asg

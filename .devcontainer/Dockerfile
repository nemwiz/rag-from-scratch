FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV PATH="/root/.local/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends curl python3 python3-pip python3.10-venv \
    && curl -sSL https://install.python-poetry.org | python3 -

CMD ["sleep", "infinity"]
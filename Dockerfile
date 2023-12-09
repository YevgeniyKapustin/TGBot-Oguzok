FROM python:3.12.1

WORKDIR /bot/

RUN pip install 'poetry==1.6.1'
COPY poetry.lock pyproject.toml /bot/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --only main

COPY . .

CMD python run.py

FROM python

WORKDIR /app

COPY test_wallet/requirements.txt .

RUN pip install -r requirements.txt

COPY test_wallet .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
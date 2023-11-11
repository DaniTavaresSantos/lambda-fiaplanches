import calendar
import datetime
import json
import os

import jwt

secret_key = os.environ.get("SECRET_KEY").strip()


def create_token(cpf: str) -> json:
    payload = {
        "cpf": cpf,
        "exp": generate_exp_time()
    }

    token = jwt.encode(payload, secret_key, algorithm="HS512")

    return {
        "expiration": 3600,
        "access_token": token
    }


def generate_exp_time() -> int:
    day_current = datetime.datetime.now() + datetime.timedelta(hours=1)
    return calendar.timegm(day_current.timetuple())

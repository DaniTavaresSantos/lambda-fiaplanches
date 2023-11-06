import calendar
import datetime
import json
import os

import jwt

secret_key = "52d3f853c19f8b63c0918c126422aa2d99b1aef33ec63d41dea4fadf19406e54"


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

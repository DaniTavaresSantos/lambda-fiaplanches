import psycopg2
import os


def get_user(cpf: str):
    connection = psycopg2.connect(
        dbname="fiaplanches",
        host="fiaplanches.cf5bq2g9b2j1.us-east-1.rds.amazonaws.com",
        password="w44JZd3d4BYQiNDhNLg4",
        user="fiap_lanches"
    )

    with connection as conn:
        with conn.cursor() as curs:
            query = f"""
                select 1 from cliente
                where cpf = '{cpf}'
            """

            curs.execute(query)
            record = curs.fetchone()

            if record is not None:
                return record[0]
            else:
                return record

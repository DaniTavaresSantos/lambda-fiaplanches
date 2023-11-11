import psycopg2
import os


def get_user(cpf: str):
    connection = psycopg2.connect(
        dbname=os.environ.get("FIAP_LANCHES_DB_NAME").strip(),
        host=os.environ.get("FIAP_LANCHES_HOST").strip(),
        password=os.environ.get("FIAP_LANCHES_PASSWORD").strip(),
        user=os.environ.get("FIAP_LANCHES_USER").strip()
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

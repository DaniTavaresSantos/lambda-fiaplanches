from jwt_token import create_token
from repository import get_user


def lambda_handler(event, context):
    try:
        cpf = event["body"]['cpf']

        user_exist = get_user(cpf)

        if user_exist:
            return {
                "status_code": 200,
                "body": create_token(cpf)
            }
        else:
            return {
                "status_code": 401,
                "body": {
                    "description": "Unauthorized"
                }
            }
    except Exception as e:
        return {
                "status_code": 400,
                "body": {
                    "description": f"{e}"
                }
            }


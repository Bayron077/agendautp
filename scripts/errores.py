"""Paso 1: cómo leer los errores de AWS y configurar reintentos."""
import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

config = Config(
    retries={"max_attempts": 5, "mode": "standard"},
    connect_timeout=3,
    read_timeout=10,
)
s3 = boto3.client("s3", config=config)

for bucket in ["agendautp-no-existe-9z9z9z", "commoncrawl"]:
    try:
        s3.head_bucket(Bucket=bucket)
        print(f"{bucket}: existe y tengo acceso")
    except ClientError as error:
        codigo = error.response["Error"]["Code"]
        estado = error.response["ResponseMetadata"]["HTTPStatusCode"]
        if codigo == "404":
            print(f"{bucket}: no existe ({estado})")
        elif codigo == "403":
            print(f"{bucket}: existe, pero es de otra cuenta ({estado})")
        else:
            raise
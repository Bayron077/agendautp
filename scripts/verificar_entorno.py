"""Paso 1: verifica identidad, región y origen de las credenciales."""
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def main():
    sesion = boto3.Session()
    print(f"Región configurada: {sesion.region_name}")

    credenciales = sesion.get_credentials()
    if credenciales is None:
        raise SystemExit("No se encontraron credenciales. Revisen el Paso 0.3.")
    print(f"Origen de las credenciales: {credenciales.method}")

    identidad = sesion.client("sts").get_caller_identity()
    print(f"Cuenta: {identidad['Account']}")
    print(f"ARN: {identidad['Arn']}")

    buckets = sesion.client("s3").list_buckets()["Buckets"]
    print(f"Buckets en la cuenta: {len(buckets)}")

if __name__ == "__main__":
    try:
        main()
    except NoCredentialsError:
        raise SystemExit("boto3 no encontró credenciales.")
    except ClientError as error:
        info = error.response["Error"]
        raise SystemExit(f"AWS rechazó la solicitud: {info['Code']} - {info['Message']}")

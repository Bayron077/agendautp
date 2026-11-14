"""Paso 1: recorrer todas las páginas de una respuesta."""
import boto3

ec2 = boto3.client("ec2")
paginador = ec2.get_paginator("describe_instance_types")

paginas = 0
tipos = 0

for pagina in paginador.paginate(PaginationConfig={"PageSize": 100}):
    paginas += 1
    tipos += len(pagina["InstanceTypes"])
    
print(f"{tipos} tipos de instancia en {paginas} páginas")
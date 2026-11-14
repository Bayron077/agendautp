export AWS_REGION=us-east-1
export INICIALES=bc
export SUFIJO=1004
export BUCKET=agendautp-medios-$INICIALES-$SUFIJO
export CUENTA=$(aws sts get-caller-identity --query Account --output text)
export ROLE_ARN=arn:aws:iam::$CUENTA:role/LabRole
export TABLA_EVENTOS=Eventos
export TABLA_INSCRIPCIONES=Inscripciones

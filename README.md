# DevOps: Agilizando el Despliegue Continuo de Aplicaciones

## Integrantes

|Nombre                        |Correo                           |
|------------------------------|---------------------------------|
|Julian Padilla Molina         |j.padilla@uniandes.edu.co        |
|Santiago Fajardo Tellez       |s.fajardot@uniandes.edu.co       |
|Laura Helena Cabra Acela      |lh.cabra@uniandes.edu.co         |
|Daniel Felipe Hernandez Parra |df.hernandezp12@uniandes.edu.co  |

## Despliegue microservicio

### Despliegue remoto

Para correr el microservicio "Blacklist" de forma remota se utiliza los servicios de AWS: ECR, RDS, EC2, ECS, CodeBuild, CodeDeploy y CodePipeline permitiendo que este sea accedido por medio de la url:

- [load-balancer-2102978182.us-east-1.elb.amazonaws.com](load-balancer-2102978182.us-east-1.elb.amazonaws.com)

### Despliegue manual

Para correr el microservicio "Blacklist" se debe seguir los siguientes pasos (comandos):

1. Clonar el repositorio en la ubicación de preferencia dentro de su dispositivo.
2. Abrir el proyecto con el editor de preferencia se recomienda utilizar <code>visual studio code</code>.
3. Abrir la terminal integrada en el editor de código seleccionado.
4. Ingresar el comando <code>pip install -r requirements.txt</code> para instalar las dependencias necesarias del proyecto de flask.
5. Ingresar el comando <code>pyhton3 application.py</code> para correr el proyecto de flask.

Una vez ejecutado la serie de pasos anterior se tiene disponible el API en la siguiente dirección http://localhost:8000/

## Documentación API

En el siguiente enlace encontrará la documentación de la API construida para el microservicio Blacklist con la herramienta de POSTMAN:

- [Documentación Blacklist](https://documenter.getpostman.com/view/21689315/2sAXxTdBYh)

## Pruebas

### Despliegue remoto

Para correr las pruebas de la API "Blacklist" de forma remota se utiliza el servicio de AWS: Code Build permitiendo descargar y configurar la aplicación, correr las pruebas definidas para los endpoints de la API y generar el artefacto que se sube al S3.

### Despliegue manual

Para correr las pruebas de la API "Blacklist" de forma local es necesario tener presente los comandos del 1 al 4 del despliegue:

1. Ingresar el comando <code>pytest --cov=. --cov-fail-under=70</code> para ejecutar las pruebas desarrolladas para probar la API.

Una vez ejecutado el paso anterior se tiene el reporto de las pruebas ejecutadas con el porcentaje de cobertura abarcado.

## Video explicación entrega

En el siguiente enlace encontrará el video donde se explica y sustenta lo realizado en la entrega 1:

- [Video entrega 1](https://uniandes-my.sharepoint.com/:v:/g/personal/j_padilla_uniandes_edu_co/EQHt8U9MWc1Llw3dnPQICkgBzzYvLugPOEQtyAY-dGPkGQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=ZbFJ0F)

En el siguiente enlace encontrará el video donde se explica y sustenta lo realizado en la entrega 2:

- [Video entrega 2](https://uniandes-my.sharepoint.com/:v:/g/personal/j_padilla_uniandes_edu_co/Ee9Faxzdh9RNvTqQ4pKuufQBbEPkQ4vOTMLaHz6EZW0Pag?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=9mqaSP)

En el siguiente enlace encontrará el video donde se explica y sustenta lo realizado en la entrega 3:

- [Video entrega 3](https://uniandes-my.sharepoint.com/:v:/g/personal/j_padilla_uniandes_edu_co/EeoOu0oNIP5NqjdoQlQCfGYBF9kB7lKBxlrN3a04Ann9YQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=qDs7vD)

En el siguiente enlace encontrará el video donde se explica y sustenta lo realizado en la entrega 4:

- [Video entrega 4](https://uniandes-my.sharepoint.com/:v:/g/personal/j_padilla_uniandes_edu_co/ERIwn3ov729KsqSBfoehxhkBhw58DkjeoJ2JtIiiEHUWUA?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=WUiNYW)

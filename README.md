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

Para correr el microservicio "Blacklist" de forma remota se utiliza los servicios de AWS: RDS y Beanstalk permitiendo que este sea accedido por medio de la url:

- http://beanstalk-blacklists.eba-pxp33nh2.us-east-1.elasticbeanstalk.com/

### Despliegue manual

Para correr el microservicio "Blacklist" se debe seguir los siguientes pasos (comandos):

1. Clonar el repositorio en la ubicación de preferencia dentro de su dispositivo.
2. Abrir el proyecto con el editor de preferencia se recomienda utilizar <code>visual studio code</code>.
3. Abrir la terminal integrada en el editor de código seleccionado.
4. Ingresar el comando <code>pip install -r requirements.txt</code> para instalar las dependencias necesarias del proyecto de flask.
6. Ingresar el comando <code>pyhton3 application.py</code> para correr el proyecto de flask.

Una vez ejecutado la serie de pasos anterior se tiene disponible el API en la siguiente dirección http://localhost:8000/

## Documentación API

En el siguiente enlace encontrará la documentación de la API construida para el microservicio Blacklist con la herramienta de POSTMAN:

- [Documentación Blacklist](https://documenter.getpostman.com/view/21689315/2sAXxTdBYh)


## Video explicación entrega

En el siguiente enlace encontrará el video donde se explica y sustenta lo realizado en la entrega 1:

- [Video entrega 1](https://uniandes-my.sharepoint.com/:v:/g/personal/j_padilla_uniandes_edu_co/EQHt8U9MWc1Llw3dnPQICkgBzzYvLugPOEQtyAY-dGPkGQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=ZbFJ0F)


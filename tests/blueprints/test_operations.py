import os
import json
import unittest
from flask import Flask
from application import application
from flask_sqlalchemy import SQLAlchemy

os.environ['DATABASE'] = 'sqlite:///test_blacklists.db'

class TestBlacklistsOperations(unittest.TestCase):

    def test_blacklists_add_without_token(self):
        with application.test_client() as test_client:
            response = test_client.post('/blacklists',
                                            json={
                                                "email": "laura@uniandes.edu.co",
                                                "app_uuid": "08043ed9-6823-426b-9900-e431e1d744f8",
                                                "blocked_reason": "This user is PEP"
                                            })

            assert response.status_code == 401
            assert response.get_json()['error'] == 'Unauthorized'

    def test_blacklists_add_email_success(self):
        with application.test_client() as test_client:
            response = test_client.post('/blacklists',
                                            json={
                                                'email': 'laura@uniandes.edu.co',
                                                'app_uuid': '08043ed9-6823-426b-9900-e431e1d744f8',
                                                'blocked_reason': 'This user is PEP'
                                            }, headers={'Authorization': f'Bearer {os.environ["TOKEN"]}'})

            assert response.status_code == 200
            assert response.get_json()['msg'] == 'Email agregado a la blacklist'

    def test_blacklists_add_without_email(self):
        with application.test_client() as test_client:
            response = test_client.post('/blacklists', headers={'Authorization': f'Bearer {os.environ["TOKEN"]}'},
                                            json={
                                                "app_uuid": "08043ed9-6823-426b-9900-e431e1d744f8",
                                                "blocked_reason": "This user is PEP"
                                            })

            assert response.status_code == 400
            assert response.get_json()['error'] == 'Email y app_uuid son obligatorios'

    def test_blacklists_add_without_app_uuid(self):
        with application.test_client() as test_client:
            response = test_client.post('/blacklists', headers={'Authorization': f'Bearer {os.environ["TOKEN"]}'},
                                            json={
                                                "email": "laura@uniandes.edu.co",
                                                "blocked_reason": "This user is PEP"
                                            })

            assert response.status_code == 400
            assert response.get_json()['error'] == 'Email y app_uuid son obligatorios'

    def test_blacklists_add_invalid_app_uuid(self):
        with application.test_client() as test_client:
            response = test_client.post('/blacklists', headers={'Authorization': f'Bearer {os.environ["TOKEN"]}'},
                                            json={
                                                "email": "laura@uniandes.edu.co",
                                                "app_uuid": "08",
                                                "blocked_reason": "This user is PEP"
                                            })

            assert response.status_code == 400
            assert response.get_json()['error'] == 'app_uuid no es un uuid válido'

    def test_blacklists_add_invalid_blocked_reason(self):
        with application.test_client() as test_client:
            response = test_client.post('/blacklists', headers={'Authorization': f'Bearer {os.environ["TOKEN"]}'},
                                            json={
                                                "email": "juan@uniandes.edu.co",
                                                "app_uuid": "08043ed9-6823-426b-9900-e431e1d744f8",
                                                "blocked_reason": "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas Letraset, las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum."
                                            })

            assert response.status_code == 400
            assert response.get_json()['error'] == 'blocked_reason debe tener máximo 255 caracteres'

    def test_blacklists_get_email_without_token(self):
        with application.test_client() as test_client:
            response = test_client.get(f'/blacklists/j@hotmail.com')

            assert response.status_code == 401
            assert response.get_json()['error'] == 'Unauthorized'

    def test_blacklists_get_email_success(self):
        with application.test_client() as test_client:
            responseAdd = test_client.post('/blacklists', headers={'Authorization': f'Bearer {os.environ["TOKEN"]}'},
                                            json={
                                                "email": "laura@uniandes.edu.co",
                                                "app_uuid": "08043ed9-6823-426b-9900-e431e1d744f8",
                                                "blocked_reason": "This user is PEP"
                                            })
            response_json = json.loads(responseAdd.data)
            print(response_json)

            response = test_client.get(f'/blacklists/{response_json["blacklist"]["email"]}', headers={'Authorization': f'Bearer {os.environ["TOKEN"]}'})

            assert response.status_code == 200
            assert response.get_json()['is_blacklisted'] == True

    def test_blacklists_get_email_failed(self):
        with application.test_client() as test_client:
            response = test_client.get(f'/blacklists/j@hotmail.com', headers={'Authorization': f'Bearer token'})

            assert response.status_code == 200
            assert response.get_json()['is_blacklisted'] == False
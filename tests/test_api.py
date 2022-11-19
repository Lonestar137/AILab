from decimal import Decimal
from ailab.ext.restapi.api import *
from flask import Flask

import requests

class TestPOSTRoutes:
    def test_post_generate_image_post(client):
        myData = {'somekey': 'somevalue'}
        with app.test_client() as c:
            response = c.post("/api/v1/post/generate/image", json=myData)
            assert response.status_code == 200

    def test_post_generate_image_post(client):
        with app.test_client() as c:
            response = c.get("/api/v1/post/generate/image")
            assert response.status_code == 405 


class TestGETRoutes:
    def test_post_index_get(client):
        with app.test_client() as c:
            response = c.get("/api/v1/post")
            assert response.status_code == 200

    def test_validate_user_edit_get(client):
        with app.test_client() as c:
            response = c.get('/')
            assert response.status_code == 200


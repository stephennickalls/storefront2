from rest_framework import status
from rest_framework.test import APIClient

class TestCreateCollection:
    def test_it_user_is_anonymous_returns_401(self):
        client = APIClient()
        response = client.post('/store/collections/', {'title': 'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
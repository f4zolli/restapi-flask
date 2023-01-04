import pytest
from application import create_app


class TestApplication():
    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

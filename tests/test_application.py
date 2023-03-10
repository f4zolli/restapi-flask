import pytest
from application import create_app


class TestApplication():
    # criando a fixture para rodar os testes
    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()

    # criando a fixture para testar a inserção de um user com json
    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "Fix",
            "last_name": "Test",
            "cpf": "05100646047",
            "email": "fix_test@teste.com",
            "birth_date": "2000-10-01"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "Fix",
            "last_name": "Test",
            "cpf": "05100646041",
            "email": "fix_test@teste.com",
            "birth_date": "2000-10-01"
        }

    # testando status code 200 no /users
    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    # testando metodo post no user
    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"sucessfully" in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data

    # testando get no user criado no ultimo teste
    def test_get_user(self, client, valid_user, invalid_user):
        response = client.get('/user/%s' % valid_user["cpf"])
        assert response.status_code == 200
        assert response.json[0]["first_name"] == "Fix"
        assert response.json[0]["last_name"] == "Test"
        assert response.json[0]["cpf"] == "05100646047"
        assert response.json[0]["email"] == "fix_test@teste.com"

        # alteracao feita por conta do tamanho da linha
        birth_date = response.json[0]["birth_date"]["$date"]
        assert birth_date == "2000-10-01T00:00:00Z"

        response = client.get('/user/%s' % invalid_user["cpf"])
        assert response.status_code == 400
        assert b"not exist" in response.data

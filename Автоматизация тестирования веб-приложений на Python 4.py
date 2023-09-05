python
import pytest
from api.api_client import APIClient
from api.api_exceptions import APIException

# Остальные импорты

class TestAPI:
    def setup_class(self):
        self.client = APIClient()

    def test_api_method1(self):
        try:
            # Шаги по вызову API метода 1 и проверке результата
        except APIException as e:
            pytest.fail(f"API Exception occurred: {e}")

    def test_api_method2(self):
        try:
            # Шаги по вызову API метода 2 и проверке результата
        except APIException as e:
            pytest.fail(f"API Exception occurred: {e}")
response = self.client.call_api_method1(param1, param2)
assert response.status_code == 200
assert response.json()["result"] == expected_result

response = self.client.call_api_method2(param1, param2)
assert response.status_code == 200
assert response.json()["result"] == expected_result

try:
    response = self.client.call_api_method1(param1, param2)
    assert response.status_code == 200
    assert response.json()["result"] == expected_result
except APIException as e:
    pytest.fail(f"API Exception occurred: {e}")
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_api_method1(self):
    try:
        response = self.client.call_api_method1(param1, param2)
        logger.info(f"API method 1 called with params: {param1}, {param2}")
        logger.info(f"API method 1 response: {response.text}")
        assert response.status_code == 200
        assert response.json()["result"] == expected_result
    except APIException as e:
        logger.error(f"API Exception occurred: {e}")
        pytest.fail(f"API Exception occurred: {e}")

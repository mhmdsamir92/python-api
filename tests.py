import unittest
from utils import add, multiply, substract
from app import app
import mock

class TestUtils(unittest.TestCase):

    def test_add(self):
        actual = add(1, 2)
        expected = 3
        self.assertEqual(actual, expected)

    def test_multiply(self):
        actual = multiply(4, 2)
        expected = 8
        self.assertEqual(actual, expected)
    
    def test_substract(self):
        actual = substract(4, 2)
        expected = 2
        self.assertEqual(actual, expected)


class TestAPI(unittest.TestCase):
    testing_client = app.test_client()

    @mock.patch("app.add", return_value=0)
    @mock.patch("app.multiply", return_value=0)
    @mock.patch("app.substract", return_value=-1)
    def test_api(self, substract_mock, muliply_mock, add_mock):
        response = self.testing_client.get("http://localhost:5000/math/5/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "add": 0,
            "mutiply": 0,
            "substract": -1
        })
        muliply_mock.assert_called_once_with(5, 2)
        add_mock.assert_called_once_with(5, 2)
        substract_mock.assert_called_once_with(5, 2)
        

    def test_api_integration(self):
        response = self.testing_client.get("http://localhost:5000/math/5/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "add": 7,
            "mutiply": 10,
            "substract": 3
        })


if __name__ == "__main__":
    unittest.main()
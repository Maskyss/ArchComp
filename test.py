import unittest
import arrow
import requests


class PythonApi(unittest.TestCase):
    def test_get_items(self):
        utc = arrow.utcnow()
        res = requests.get('http://127.0.0.1:5000/tasks')

        if res.status_code == 200:
            print("Test 'get_items()' PASS at " + str(utc))
        else:
            print("Test 'get_items()' FAIL at " + str(utc))

    def test_get_item(self):
        utc = arrow.utcnow()
        res = requests.get('http://127.0.0.1:5000/tasks/1')

        if res.status_code == 200:
            print("Test 'get_item()' PASS at " + str(utc))
        else:
            print("Test 'item()' FAIL at " + str(utc))


if __name__ == "__main__":
    unittest.main()
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

    def test_create_item(self):
        utc = arrow.utcnow()

        item = {"title": "Reading",
                        "done": "False",
                        "day": "2",
                        "month": "44",
                        "year": "2019"}

        res = requests.post('http://127.0.0.1:5000/tasks', data=item)

        if res.status_code == 201:
            print("Test 'create_item()' PASS at " + str(utc))
        else:
            print("Test 'create_item()' FAIL at " + str(utc))

    def test_update_item(self):
        utc = arrow.utcnow()

        item = {"title": "Reading",
                        "done": True,
                        "day": "2",
                        "month": "44",
                        "year": "2019"
                       }

        res = requests.put(url='http://127.0.0.1:5000/tasks/2', data=item)
        if res.status_code == 200:
            print("Test 'update_item()' PASS at " + str(utc))
        else:
            print("Test 'update_item()' FAIL at " + str(utc))

    def test_delete_item(self):
        utc = arrow.utcnow()

        res = requests.delete('http://127.0.0.1:5000/tasks/2')
        if res.status_code == 200:
            print("Test 'delete_measurements()' PASS at " + str(utc))
        else:
            print("Test 'delete_measurements()' FAIL at " + str(utc))

            
if __name__ == "__main__":
    unittest.main()

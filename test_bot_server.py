import requests
import unittest
import json



class TestServer(unittest.TestCase):

    def test_post_json(self):
        """
        Ensure that json POST gets parsed in bot_server as string 
        In the format of https://core.telegram.org/bots/api#message
        """

        with open("fixtures/basic.json") as json_data:
            data = json.load(json_data)
            string_data = json_data.read()
        r = requests.post("http://127.0.0.1:8000/",
                          json=json.dumps(data))
        assert r.text == """{"content_type": "text", "chat_id": 22959774, "response": "_NOACTION_"}"""

if __name__ == '__main__':
    unittest.main()

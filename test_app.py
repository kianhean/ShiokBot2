import unittest
import app
import json


class TestParsingMethods(unittest.TestCase):


    def test_parse_jason_response(self):
        """ Mock Using Local Json """

        with open("fixtures/basic.json") as json_data:
            data = json.load(json_data)

        output = app.handle(data)
        self.assertEqual(output['content_type'], 'text')
        self.assertEqual(output['chat_id'], 22959774)


if __name__ == '__main__':
    unittest.main()

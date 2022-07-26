import unittest
import requests
import responses

class TestCase(unittest.TestCase):

  @responses.activate  
  def testExample(self):
    responses.add(**{
      'method'         : responses.GET,
      'url'            : 'https://none6104.freshdesk.com/api/v2/contacts',
      'body'           : '{"error": "reason"}',
      'status'         : 404,
      'content_type'   : 'application/json',
      'adding_headers' : {'X-Foo': 'Bar'}
    })

    response = requests.get('https://none6104.freshdesk.com/api/v2/contacts')

    self.assertEqual({'error': 'reason'}, response.json())
    self.assertEqual(404, response.status_code)


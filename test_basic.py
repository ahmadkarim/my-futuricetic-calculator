import os
import unittest
import base64
import json
from app import app

  
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False     
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

 
###############
#### tests ####
###############
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_addition(self):
        equation = '2 + 2'
        base64EncodedBytes = base64.b64encode(equation.encode('UTF-8'))
        base64EncodedBytesAsString = str(base64EncodedBytes, 'UTF-8')
        response = self.app.get('/calculus?query='+base64EncodedBytesAsString, follow_redirects=True)
        responseJson = json.loads(response.data)
        self.assertEqual(responseJson['message'], 4)
    
    def test_subtraction(self):
        equation = '2 - 2'
        base64EncodedBytes = base64.b64encode(equation.encode('UTF-8'))
        base64EncodedBytesAsString = str(base64EncodedBytes, 'UTF-8')
        response = self.app.get('/calculus?query='+base64EncodedBytesAsString, follow_redirects=True)
        responseJson = json.loads(response.data)
        self.assertEqual(responseJson['message'], 0)
    
    def test_multiplication(self):
        equation = '2 * 2'
        base64EncodedBytes = base64.b64encode(equation.encode('UTF-8'))
        base64EncodedBytesAsString = str(base64EncodedBytes, 'UTF-8')
        response = self.app.get('/calculus?query='+base64EncodedBytesAsString, follow_redirects=True)
        responseJson = json.loads(response.data)
        self.assertEqual(responseJson['message'], 4)
   
    def test_division(self):
        equation = '2 / 2'
        base64EncodedBytes = base64.b64encode(equation.encode('UTF-8'))
        base64EncodedBytesAsString = str(base64EncodedBytes, 'UTF-8')
        response = self.app.get('/calculus?query='+base64EncodedBytesAsString, follow_redirects=True)
        responseJson = json.loads(response.data)
        self.assertEqual(responseJson['message'], 1.0)

    def test_brackets(self):
        equation = '2 + (2/2) - 2'
        base64EncodedBytes = base64.b64encode(equation.encode('UTF-8'))
        base64EncodedBytesAsString = str(base64EncodedBytes, 'UTF-8')
        response = self.app.get('/calculus?query='+base64EncodedBytesAsString, follow_redirects=True)
        responseJson = json.loads(response.data)
        self.assertEqual(responseJson['message'], 1.0)

    def test_invalid_expressions_with_syntax_error(self):
        equation = '2 + )(2/2) - 2'
        base64EncodedBytes = base64.b64encode(equation.encode('UTF-8'))
        base64EncodedBytesAsString = str(base64EncodedBytes, 'UTF-8')
        response = self.app.get('/calculus?query='+base64EncodedBytesAsString, follow_redirects=True)
        responseJson = json.loads(response.data)
        self.assertEqual(responseJson['error'], True)

    def test_invalid_base64_String(self):
        response = self.app.get('/calculus?query=MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk', follow_redirects=True)
        responseJson = json.loads(response.data)
        print(responseJson['message'])
        self.assertEqual(responseJson['error'], True)

if __name__ == "__main__":
    unittest.main()
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 07:42:19 2021

@author: Ahmad
"""
#== API Description ==
# Endpoint:GET /calculus?query=[input]

from flask import Flask, request, jsonify
import base64
import re

app = Flask(__name__)

@app.route('/calculus', methods=['GET'])
def respond():

    # Retrieve the querry from url parameter
    query = request.args.get("query", None)

    try:
        #decode the query string
        base64decodedbytes = base64.b64decode(query)
        
        # decode to utf-8 string
        base64decodedString = base64decodedbytes.decode('UTF-8')

        # verify the math string and check for non math characters and also to counter injection
        # allowedOperations = ['1','2','3','4','5','6','7','8','9','0', '.' , '*', '+', '-','/', '(',')',' ']
        if not bool(re.match('[\d/\-\(\)\*\+\.\W]+$', base64decodedString )):
            return jsonify({'error': 'true', 'message': 'Your query:"'+ base64decodedString +'" contains invalid character please use numbers and allowed operations: +, -, /, *, (, )'})
        
        queryResult = eval(base64decodedString)
        return jsonify({'error': False, 'message': queryResult})

    # handle if length of base64string is not correct
    except base64.binascii.Error as err:
        print('wrong length of base64 string it should be a multiple of 4')
        return jsonify({'error': True, 'message': 'Wrong length of base64 string it should be a multiple of 4; error:' + str(err)})
    
    # handle if string is not a valid utf-8
    except UnicodeDecodeError:
        return jsonify({'error': True, 'message': 'Decoding error while decoding base64 byte to string'})
    
    # handle syntax error in the mathematical expression
    except SyntaxError:
        return jsonify({'error': True, 'message': 'Syntax error in query:'+ base64decodedString})

    # handle general exceptions
    except Exception as err:
        return jsonify({'error': True, 'message': 'An error occured: '+ str(err) })

    # add gunicorn
    # add either nginx load balancer or use from Azure/Heroku

# A test message
@app.route('/')
def index():
    return "<h1>I am a Futuricetic calculator and I work!!!</h1>"

@app.route('/health')
def healthCheck():
    return "<h1>I am a healthy app!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=80)
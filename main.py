from flask import Flask, request, jsonify
from haziri import Haziri
from multiprocessing import Process

app = Flask(__name__)

all = []
processes = []

@app.route('/')
def home():
  return "Haziri API : ERP BITMESRA"

@app.route('/api/v1/resources/haziri', methods=['GET'])
def getTable():

  if 'id' in request.args:
    username = str(request.args['id'])
  else:
    return "errorNoID"
  if 'pwd' in request.args:
    password = str(request.args['pwd'])
  else:
    return "errorNoPwd"

  table = Haziri(username, password)
  return jsonify(table)

if __name__ == '__main__':
  app.run(host = "0.0.0.0", port= '8090',debug = False, threaded = True)

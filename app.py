# Assignmentm part 1
# return a JSON response e.g. {"user": "admin"}. 
#/status endpoint should return similar to :: result: OK - healthy
#/metrics endpoint should return similar to :: data: {UserCount: 140, UserCountActive: 23}
#---------------------
# Assignmentm part 2
# Add logging for each of the routes in the format below
# #"{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached"


from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route('/status')    
def healthcheck():
    response = app.response_class(
        reponse=json.dumps({'result': "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    ### log entry status
    app.logger.info('Status request successfull')

    return response    

@app.route('/metrics')    
def metrics():
    response = app.response_class(
    response=json.dumps({"status":"success","code":0,"data":{"UserCount": 140, "UserCountActive": 23}}),
    status=200,
    mimetype='application/json'
    )

    ### log entry status
    app.logger.info('Status request successfull')

    return response

@app.route("/")
def hello():
       ### log entry 
    app.logger.info('Main request successfull')
    
    return "Hello World!"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
